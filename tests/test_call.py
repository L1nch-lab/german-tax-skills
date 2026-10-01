"""Tests fuer scripts/call.py gegen einen lokalen Nachbau des RapidAPI-Gateways.

Die 429-Texte und Header-Namen folgen dem, was RapidAPI ausliefert
("You have exceeded the DAILY quota ...", x-ratelimit-requests-*).
"""

from __future__ import annotations

import importlib.util
import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import ClassVar

import pytest

SCRIPT = (
    Path(__file__).resolve().parent.parent / "skills" / "steuerrechner-api" / "scripts" / "call.py"
)
spec = importlib.util.spec_from_file_location("call", SCRIPT)
call = importlib.util.module_from_spec(spec)
spec.loader.exec_module(call)

KEY = "geheimer-test-key-123"

SCENARIOS = {
    "/v1/quota": (
        429,
        {
            "message": (
                "You have exceeded the MONTHLY quota for Requests on your current plan, BASIC."
            )
        },
        {
            "x-ratelimit-requests-limit": "100",
            "x-ratelimit-requests-remaining": "0",
            "x-ratelimit-requests-reset": "864000",
        },
    ),
    "/v1/daily": (
        429,
        {"message": "You have exceeded the DAILY quota for Requests on your current plan, BASIC."},
        {
            "x-ratelimit-requests-limit": "50",
            "x-ratelimit-requests-remaining": "0",
            "x-ratelimit-requests-reset": "18000",
        },
    ),
    "/v1/hardlimit": (
        200,
        {"success": True, "data": {}},
        {
            "x-ratelimit-requests-limit": "1000",
            "x-ratelimit-requests-remaining": "900",
            "x-ratelimit-rapid-free-plans-hard-limit-limit": "500000",
            "x-ratelimit-rapid-free-plans-hard-limit-remaining": "4",
            "x-ratelimit-rapid-free-plans-hard-limit-reset": "600",
        },
    ),
    "/v1/rate": (
        429,
        {"message": "You have exceeded the rate limit per second for your plan, BASIC."},
        {},
    ),
    "/v1/low": (
        200,
        {"success": True, "data": {"netto_monat": "2645.12"}},
        {
            "x-ratelimit-requests-limit": "100",
            "x-ratelimit-requests-remaining": "3",
            "x-ratelimit-requests-reset": "7200",
        },
    ),
    "/v1/ok": (
        200,
        {"success": True, "data": {}},
        {"x-ratelimit-requests-limit": "100", "x-ratelimit-requests-remaining": "80"},
    ),
    "/v1/echo-key": (401, {"message": f"Invalid API key {KEY}"}, {}),
}


class Handler(BaseHTTPRequestHandler):
    seen_headers: ClassVar[dict] = {}

    def _answer(self):
        Handler.seen_headers = dict(self.headers)
        # Body vollstaendig lesen: schliesst der Server mit ungelesenen Daten,
        # schickt macOS ein RST und der Client sieht "Connection reset by peer".
        self.rfile.read(int(self.headers.get("Content-Length") or 0))
        status, body, headers = SCENARIOS[self.path.split("?")[0]]
        raw = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        for k, v in headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(raw)

    do_GET = _answer
    do_POST = _answer

    def log_message(self, *args):
        pass


@pytest.fixture()
def gateway(monkeypatch):
    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    monkeypatch.setattr(call, "BASE_URL", f"http://127.0.0.1:{server.server_port}")
    monkeypatch.setenv("RAPIDAPI_KEY", KEY)
    yield
    server.shutdown()


def run(monkeypatch, capsys, *argv):
    monkeypatch.setattr(sys, "argv", ["call.py", *argv])
    code = call.main()
    out = capsys.readouterr()
    return code, out.out, out.err


def test_monatskontingent_aufgebraucht(gateway, monkeypatch, capsys):
    code, _, err = run(monkeypatch, capsys, "GET", "v1/quota")
    assert code == call.EXIT_QUOTA
    assert "Kontingent deines RapidAPI-Plans ist aufgebraucht" in err
    assert "10 Tagen" in err
    assert call.PRICING_URL in err


def test_rate_limit_ist_kein_kontingent(gateway, monkeypatch, capsys):
    code, _, err = run(monkeypatch, capsys, "GET", "v1/rate")
    assert code == call.EXIT_RATE_LIMIT
    assert "Rate-Limit" in err
    assert "aufgebraucht" not in err


def test_warnung_bei_knappem_kontingent(gateway, monkeypatch, capsys):
    code, out, err = run(monkeypatch, capsys, "POST", "v1/low", '{"bruttolohn": 4200}')
    assert code == 0
    assert "2645.12" in out
    assert "WARNUNG: Kontingent fast aufgebraucht" in err
    assert "3 von 100" in err
    assert "2 Stunden" in err


def test_normales_restkontingent_ohne_warnung(gateway, monkeypatch, capsys):
    code, _, err = run(monkeypatch, capsys, "GET", "v1/ok")
    assert code == 0
    assert "Restkontingent: 80 von 100" in err
    assert "WARNUNG" not in err


def test_key_wird_maskiert_und_user_agent_gesetzt(gateway, monkeypatch, capsys):
    code, out, err = run(monkeypatch, capsys, "GET", "v1/echo-key")
    assert code == 1
    assert KEY not in out + err
    assert "***" in out
    assert Handler.seen_headers["User-Agent"].startswith("german-tax-skills/")
    assert Handler.seen_headers["X-Rapidapi-Key"] == KEY


def test_git_bash_pfad_wird_repariert():
    assert call.normalize_path("C:/Program Files/Git/v1/brutto-netto") == "/v1/brutto-netto"
    assert call.normalize_path("v1/hebesaetze") == "/v1/hebesaetze"


def test_tageskontingent_basic(gateway, monkeypatch, capsys):
    code, _, err = run(monkeypatch, capsys, "GET", "v1/daily")
    assert code == call.EXIT_QUOTA
    assert "5 Stunden" in err


@pytest.mark.parametrize(
    ("limit", "remaining", "low"),
    [
        (50, 5, True),  # Basic: Schwelle 5
        (50, 6, False),
        (1000, 100, True),  # Pro: Schwelle 100
        (1000, 101, False),
        (300000, 100, True),  # Ultra: gedeckelt auf 100, nicht 30.000
        (300000, 5000, False),
    ],
)
def test_warnschwelle_je_plan(limit, remaining, low):
    assert call.is_low({"limit": limit, "remaining": remaining}) is low


def test_knapperes_der_beiden_kontingente_gilt(gateway, monkeypatch, capsys):
    code, _, err = run(monkeypatch, capsys, "GET", "v1/hardlimit")
    assert code == 0
    assert "WARNUNG" in err
    assert "4 von 500000" in err


def test_header_wie_im_echten_request_log():
    # Werte aus dem RapidAPI-Request-Log vom 28.09.2026 (Playground-Aufruf).
    headers = {
        "x-ratelimit-rapid-free-plans-hard-limit-limit": "500000",
        "x-ratelimit-rapid-free-plans-hard-limit-remaining": "499999",
        "x-ratelimit-rapid-free-plans-hard-limit-reset": "775574",
        "x-ratelimit-requests-limit": "500000",
        "x-ratelimit-requests-remaining": "499999",
        "x-ratelimit-requests-reset": "775574",
    }
    info = call.quota_info(headers)
    assert info == {"limit": 500000, "remaining": 499999, "reset": 775574}
    assert call.quota_line(info) == (
        "Restkontingent: 499999 von 500000 Anfragen, setzt sich zurueck in 8 Tagen."
    )


def test_version_passt_zur_plugin_json():
    # Die Version steckt im User-Agent, ueber den die Nutzung gemessen wird.
    root = Path(__file__).resolve().parent.parent
    # Zwei Manifeste: .claude-plugin/ fuer Claude Code, plugin.json im Root fuer Copilot.
    for manifest in (root / ".claude-plugin" / "plugin.json", root / "plugin.json"):
        plugin = json.loads(manifest.read_text(encoding="utf-8"))
        assert plugin["version"] == call.VERSION, manifest


@pytest.mark.parametrize("bom", [b"", b"\xef\xbb\xbf"])
def test_key_aus_env_datei_auch_mit_bom(tmp_path, monkeypatch, bom):
    # PowerShell 5.1 schreibt mit Set-Content -Encoding utf8 ein BOM vor die erste Zeile.
    (tmp_path / ".env").write_bytes(bom + f"RAPIDAPI_KEY={KEY}\n".encode())
    monkeypatch.delenv(call.KEY_NAME, raising=False)
    monkeypatch.chdir(tmp_path)
    assert call.find_key() == (KEY, ".env im Arbeitsverzeichnis")
