"""Ruft einen Endpoint der Steuerrechner-API ueber RapidAPI auf.

Usage:
    python call.py POST v1/brutto-netto '{"bruttolohn": 3500, "steuerklasse": 1}'
    python call.py POST v1/brutto-netto --body-file anfrage.json
    python call.py GET v1/hebesaetze --query plz=50667
    python call.py GET v1/basiszins/current
    python call.py --check            # prueft nur, ob ein Key gefunden wird
    python call.py ... --dry-run      # zeigt die Anfrage, ohne sie zu senden

Den Pfad ohne fuehrenden Schraegstrich angeben: Git Bash unter Windows wuerde
/v1/... sonst in einen Windows-Pfad umschreiben (wird trotzdem repariert).

Exit-Codes: 0 ok, 1 HTTP-Fehler, 2 kein Key, 3 Netzwerkfehler,
4 Kontingent des RapidAPI-Plans aufgebraucht, 5 Rate-Limit (zu viele Anfragen kurz hintereinander).

Der Key kommt aus der Umgebungsvariable RAPIDAPI_KEY oder aus einer .env-Datei
im aktuellen Verzeichnis. Er wird nie ausgegeben, auch nicht in Fehlermeldungen.
Nur Standardbibliothek, damit der Skill ohne pip install laeuft.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

VERSION = "0.1.0"
HOST = "german-tax-calculator.p.rapidapi.com"
BASE_URL = f"https://{HOST}"
USER_AGENT = f"german-tax-skills/{VERSION}"
KEY_NAME = "RAPIDAPI_KEY"
SUBSCRIBE_URL = "https://rapidapi.com/rechnerhub/api/german-tax-calculator"
PRICING_URL = f"{SUBSCRIBE_URL}/pricing"
# Ab diesem Restkontingent warnt das Skript nach einem erfolgreichen Aufruf:
# 10 % des Plans, mindestens 5, hoechstens 100 Anfragen. Plaene (Stand 28.09.2026):
# Basic 50/Tag -> 5, Pro 1.000/Tag -> 100, Ultra 300.000/Monat -> 100.
LOW_QUOTA_SHARE = 0.1
LOW_QUOTA_MIN = 5
LOW_QUOTA_MAX = 100

EXIT_QUOTA = 4
EXIT_RATE_LIMIT = 5


def find_key() -> tuple[str | None, str]:
    key = os.environ.get(KEY_NAME, "").strip()
    if key:
        return key, "Umgebungsvariable"
    env_file = Path.cwd() / ".env"
    if env_file.is_file():
        for line in env_file.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if line.startswith("export "):
                line = line[len("export ") :].lstrip()
            if line.startswith(f"{KEY_NAME}="):
                value = line.split("=", 1)[1].strip().strip('"').strip("'")
                if value:
                    return value, ".env im Arbeitsverzeichnis"
    return None, ""


def mask(text: str, key: str | None) -> str:
    return text.replace(key, "***") if key else text


def missing_key_message() -> str:
    return (
        f"Kein API-Key gefunden. Setze {KEY_NAME} als Umgebungsvariable oder in einer "
        f".env-Datei im Projektordner ({KEY_NAME}=...). Den Key gibt es nach dem Abonnieren "
        f"(Free-Plan reicht) unter {SUBSCRIBE_URL}. Den Key nicht in den Chat einfuegen."
    )


QUOTA_HEADER_PREFIXES = (
    # Kontingent des gebuchten Plans (Basic/Pro/Ultra).
    "x-ratelimit-requests",
    # Zusaetzliche Obergrenze, die RapidAPI selbst auf Free-Plaene legt
    # (im Request-Log vom 28.09.2026 gesehen).
    "x-ratelimit-rapid-free-plans-hard-limit",
)


def quota_info(headers) -> dict[str, int]:
    """Liest die Kontingent-Header von RapidAPI und gibt das knappere Kontingent zurueck."""
    candidates = []
    for prefix in QUOTA_HEADER_PREFIXES:
        info = {}
        for suffix in ("limit", "remaining", "reset"):
            value = headers.get(f"{prefix}-{suffix}") if headers is not None else None
            if value is not None:
                try:
                    info[suffix] = int(value)
                except ValueError:
                    pass
        if "remaining" in info:
            candidates.append(info)
    if not candidates:
        return {}
    return min(candidates, key=lambda i: i["remaining"])


def format_duration(seconds: int) -> str:
    if seconds < 3600:
        return f"{max(1, seconds // 60)} Minuten"
    if seconds < 2 * 86400:
        return f"{seconds // 3600} Stunden"
    return f"{seconds // 86400} Tagen"


def quota_line(info: dict[str, int]) -> str:
    if "remaining" not in info:
        return ""
    text = f"Restkontingent: {info['remaining']}"
    if "limit" in info:
        text += f" von {info['limit']} Anfragen"
    if "reset" in info:
        text += f", setzt sich zurueck in {format_duration(info['reset'])}"
    return text + "."


def is_low(info: dict[str, int]) -> bool:
    if "remaining" not in info:
        return False
    threshold = LOW_QUOTA_MIN
    if "limit" in info:
        share = int(info["limit"] * LOW_QUOTA_SHARE)
        threshold = max(LOW_QUOTA_MIN, min(share, LOW_QUOTA_MAX))
    return info["remaining"] <= threshold


def too_many_requests(payload: str, info: dict[str, int]) -> tuple[int, str]:
    """Unterscheidet aufgebrauchtes Plan-Kontingent von einem kurzfristigen Rate-Limit.

    RapidAPI antwortet in beiden Faellen mit HTTP 429; nur der Text sagt, welcher
    Fall vorliegt ("exceeded the DAILY/MONTHLY quota" gegen "exceeded the rate limit").
    """
    text = payload.lower()
    if "quota" in text or info.get("remaining") == 0:
        msg = "Das Anfrage-Kontingent deines RapidAPI-Plans ist aufgebraucht."
        if "reset" in info:
            msg += f" Es setzt sich in {format_duration(info['reset'])} zurueck."
        msg += f" Fuer mehr Anfragen den Plan wechseln: {PRICING_URL}"
        return EXIT_QUOTA, msg
    return EXIT_RATE_LIMIT, (
        "Zu viele Anfragen kurz hintereinander (Rate-Limit deines RapidAPI-Plans). "
        "Einen Moment warten und dann einzeln weitermachen, "
        "bei vielen Zeilen den /batch-Endpoint nutzen."
    )


def normalize_path(raw: str) -> str:
    # Git Bash unter Windows schreibt ein Argument wie /v1/brutto-netto zu
    # C:/Program Files/Git/v1/brutto-netto um. Alles ab "v1/" ist der echte Pfad.
    raw = raw.replace("\\", "/")
    idx = raw.find("v1/")
    if idx == -1:
        raise SystemExit(f"Pfad muss mit v1/ beginnen, bekommen: {raw}")
    return "/" + raw[idx:]


def build_request(args: argparse.Namespace, key: str | None) -> urllib.request.Request:
    url = BASE_URL + normalize_path(args.path)
    if args.query:
        pairs = []
        for item in args.query:
            if "=" not in item:
                raise SystemExit(f"--query erwartet name=wert, bekommen: {item}")
            pairs.append(tuple(item.split("=", 1)))
        url += "?" + urllib.parse.urlencode(pairs)

    data = None
    if args.body_file == "-":
        body_text = sys.stdin.read()
    elif args.body_file:
        # utf-8-sig: PowerShell 5.1 schreibt mit Set-Content -Encoding utf8 ein BOM.
        body_text = Path(args.body_file).read_text(encoding="utf-8-sig")
    else:
        body_text = args.body
    if body_text:
        try:
            parsed = json.loads(body_text)
        except json.JSONDecodeError as exc:
            hint = ""
            if not args.body_file and '"' not in body_text:
                hint = (
                    " Die Anfuehrungszeichen fehlen: PowerShell entfernt sie beim Aufruf"
                    " von python. Den Body in eine Datei schreiben und --body-file <datei> nutzen."
                )
            raise SystemExit(f"Body ist kein gueltiges JSON: {exc}.{hint}") from exc
        data = json.dumps(parsed, ensure_ascii=False).encode("utf-8")

    headers = {
        "X-RapidAPI-Host": HOST,
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    if key:
        headers["X-RapidAPI-Key"] = key
    if data is not None:
        headers["Content-Type"] = "application/json"
    return urllib.request.Request(url, data=data, headers=headers, method=args.method.upper())


def main() -> int:
    parser = argparse.ArgumentParser(description="Steuerrechner-API ueber RapidAPI aufrufen")
    parser.add_argument("method", nargs="?", choices=["GET", "POST", "get", "post"])
    parser.add_argument("path", nargs="?", help="z. B. /v1/brutto-netto")
    parser.add_argument("body", nargs="?", help="JSON-Body als String")
    parser.add_argument("--body-file", help="JSON-Body aus Datei, - fuer stdin")
    parser.add_argument("--query", action="append", help="Query-Parameter name=wert (mehrfach)")
    parser.add_argument("--dry-run", action="store_true", help="Anfrage zeigen, nicht senden")
    parser.add_argument("--check", action="store_true", help="nur pruefen, ob ein Key da ist")
    args = parser.parse_args()

    key, source = find_key()
    if args.check:
        if key:
            print(f"Key gefunden ({source}).")
            return 0
        print(missing_key_message(), file=sys.stderr)
        return 2

    if not args.method or not args.path:
        parser.error("Methode und Pfad fehlen")

    request = build_request(args, key)
    if args.dry_run:
        shown = {k: ("***" if k == "X-rapidapi-key" else v) for k, v in request.header_items()}
        print(
            json.dumps(
                {
                    "method": request.get_method(),
                    "url": request.full_url,
                    "headers": shown,
                    "body": json.loads(request.data) if request.data else None,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    if not key:
        print(missing_key_message(), file=sys.stderr)
        return 2

    try:
        with urllib.request.urlopen(request, timeout=30) as resp:
            payload = resp.read().decode("utf-8")
            status = resp.status
            headers = resp.headers
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        status = exc.code
        headers = exc.headers
    except urllib.error.URLError as exc:
        print(mask(f"Netzwerkfehler: {exc.reason}", key), file=sys.stderr)
        return 3

    try:
        out = json.dumps(json.loads(payload), ensure_ascii=False, indent=2)
    except json.JSONDecodeError:
        out = payload
    print(mask(out, key))
    info = quota_info(headers)

    if status == 429:
        code, msg = too_many_requests(payload, info)
        print(mask(f"HTTP 429. {msg}", key), file=sys.stderr)
        return code

    if status >= 400:
        hint = {
            401: "Key ungueltig oder fehlt.",
            403: f"Kein Abo fuer diese API. Free-Plan abonnieren: {SUBSCRIBE_URL}",
            422: "Eingabe ungueltig. Feldnamen und Werte gegen die Endpoint-Referenz pruefen.",
        }.get(status, "")
        print(mask(f"HTTP {status}. {hint}".strip(), key), file=sys.stderr)
        return 1

    line = quota_line(info)
    if line:
        if is_low(info):
            line = f"WARNUNG: Kontingent fast aufgebraucht. {line} Mehr Anfragen: {PRICING_URL}"
        print(line, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
