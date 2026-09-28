"""Tests fuer den SessionStart-Hook hooks/key-hinweis.sh."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "hooks" / "key-hinweis.sh"
BASH = shutil.which("bash")

pytestmark = pytest.mark.skipif(BASH is None, reason="bash nicht gefunden")


def run_hook(tmp_path: Path, env_extra: dict[str, str], env_file: str | None = None) -> str:
    project = tmp_path / "project"
    project.mkdir(exist_ok=True)
    if env_file is not None:
        (project / ".env").write_text(env_file, encoding="utf-8")
    env = {k: v for k, v in os.environ.items() if k != "RAPIDAPI_KEY"}
    env.update({"CLAUDE_PROJECT_DIR": str(project), "CLAUDE_PLUGIN_DATA": str(tmp_path / "data")})
    env.update(env_extra)
    result = subprocess.run(
        [BASH, str(SCRIPT)], env=env, capture_output=True, text=True, timeout=30, check=True
    )
    return result.stdout.strip()


def test_hinweis_ohne_key_einmalig(tmp_path):
    first = run_hook(tmp_path, {})
    message = json.loads(first)["systemMessage"]
    assert "RAPIDAPI_KEY" in message
    assert "rapidapi.com/rechnerhub/api/german-tax-calculator" in message
    assert run_hook(tmp_path, {}) == ""


def test_still_mit_key_in_der_umgebung(tmp_path):
    assert run_hook(tmp_path, {"RAPIDAPI_KEY": "abc123"}) == ""


@pytest.mark.parametrize(
    "zeile", ["RAPIDAPI_KEY=abc123", 'export RAPIDAPI_KEY="abc123"', "  RAPIDAPI_KEY='abc'"]
)
def test_still_mit_key_in_der_env_datei(tmp_path, zeile):
    assert run_hook(tmp_path, {}, env_file=f"OTHER=1\n{zeile}\n") == ""


def test_leerer_key_in_env_datei_zaehlt_nicht(tmp_path):
    out = run_hook(tmp_path, {}, env_file="RAPIDAPI_KEY=\n")
    assert "systemMessage" in out


def test_hooks_json_zeigt_auf_das_skript():
    config = json.loads((ROOT / "hooks" / "hooks.json").read_text(encoding="utf-8"))
    handler = config["hooks"]["SessionStart"][0]["hooks"][0]
    assert "${CLAUDE_PLUGIN_ROOT}/hooks/key-hinweis.sh" in handler["command"]
