"""Erzeugt die Endpoint-Referenz des Skills aus der OpenAPI-Spezifikation.

Usage:
    python tools/build_reference.py                      # holt https://api.rechner-hub.de/openapi.json
    python tools/build_reference.py path/to/openapi.json # lokale Datei

Schreibt skills/steuerrechner-api/reference/INDEX.md und eine Datei je Endpoint
nach reference/endpoints/. Die Referenz wird nie von Hand gepflegt: nach jeder
API-Aenderung neu erzeugen, damit Skill und API nicht auseinanderlaufen.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import urllib.request
from pathlib import Path

SPEC_URL = "https://api.rechner-hub.de/openapi.json"
ROOT = Path(__file__).resolve().parent.parent
REF_DIR = ROOT / "skills" / "steuerrechner-api" / "reference"
METHODS = ("get", "post", "put", "delete")


def load_spec(source: str | None) -> dict:
    if source:
        return json.loads(Path(source).read_text(encoding="utf-8"))
    with urllib.request.urlopen(SPEC_URL, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def resolve(spec: dict, schema: dict) -> dict:
    ref = schema.get("$ref")
    if ref:
        return spec["components"]["schemas"][ref.split("/")[-1]]
    return schema


def type_label(schema: dict) -> str:
    if "$ref" in schema:
        return schema["$ref"].split("/")[-1]
    if "enum" in schema:
        return "enum"
    variants = schema.get("anyOf") or schema.get("oneOf") or schema.get("allOf")
    if variants:
        labels = []
        for v in variants:
            if v.get("type") == "null":
                continue
            # Dezimalzahlen erlaubt die API auch als String, das ist ein Detail der
            # Eingabe-Toleranz, kein eigener Typ.
            if v.get("type") == "string" and "pattern" in v and labels == ["number"]:
                continue
            labels.append(type_label(v))
        return " | ".join(dict.fromkeys(labels)) or "any"
    t = schema.get("type", "any")
    if t == "array":
        return f"array<{type_label(schema.get('items', {}))}>"
    return t


def enum_values(schema: dict) -> list:
    if "enum" in schema:
        return schema["enum"]
    for v in schema.get("anyOf") or schema.get("allOf") or []:
        if "enum" in v:
            return v["enum"]
    return []


def cell(text: object) -> str:
    s = "" if text is None else str(text)
    s = re.sub(r"\s+", " ", s).strip()
    return s.replace("|", "\\|")


def fmt_default(schema: dict) -> str:
    if "default" not in schema:
        return ""
    return json.dumps(schema["default"], ensure_ascii=False)


def field_table(spec: dict, schema: dict) -> list[str]:
    schema = resolve(spec, schema)
    props = schema.get("properties", {})
    if not props:
        return []
    required = set(schema.get("required", []))
    rows = [
        "| Feld | Typ | Pflicht | Default | Werte | Beschreibung |",
        "|---|---|---|---|---|---|",
    ]
    for name, prop in props.items():
        enum = enum_values(prop)
        rows.append(
            "| `{}` | {} | {} | {} | {} | {} |".format(
                name,
                cell(type_label(prop)),
                "ja" if name in required else "",
                cell(fmt_default(prop)),
                cell(", ".join(map(str, enum))) if enum else "",
                cell(prop.get("description", "")),
            )
        )
    return rows


def param_table(params: list[dict]) -> list[str]:
    rows = [
        "| Parameter | Ort | Typ | Pflicht | Beschreibung |",
        "|---|---|---|---|---|",
    ]
    for p in params:
        schema = p.get("schema", {})
        enum = enum_values(schema)
        desc = p.get("description") or schema.get("description", "")
        if enum:
            desc = f"{desc} Werte: {', '.join(map(str, enum))}"
        rows.append(
            "| `{}` | {} | {} | {} | {} |".format(
                p["name"],
                p["in"],
                cell(type_label(schema)),
                "ja" if p.get("required") else "",
                cell(desc),
            )
        )
    return rows


def slug_for(method: str, path: str, taken: set[str]) -> str:
    base = path.removeprefix("/v1/").replace("{", "").replace("}", "")
    base = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-") or "root"
    slug = base if base not in taken else f"{base}-{method}"
    taken.add(slug)
    return slug


def render_endpoint(spec: dict, method: str, path: str, op: dict) -> str:
    lines = [f"# {op.get('summary') or path}", "", f"`{method.upper()} {path}`", ""]
    tags = op.get("tags") or []
    if tags:
        lines += [f"Kategorie: {', '.join(tags)}", ""]
    if op.get("description"):
        lines += [op["description"].strip(), ""]

    params = op.get("parameters") or []
    if params:
        lines += ["## Parameter", "", *param_table(params), ""]

    body = op.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema")
    if body:
        resolved = resolve(spec, body)
        table = field_table(spec, body)
        if table:
            lines += ["## Request-Body (JSON)", "", *table, ""]
        example = resolved.get("example")
        if example is not None:
            lines += [
                "Beispiel:",
                "",
                "```json",
                json.dumps(example, ensure_ascii=False, indent=2),
                "```",
                "",
            ]

    ok = (
        op.get("responses", {})
        .get("200", {})
        .get("content", {})
        .get("application/json", {})
        .get("schema")
    )
    if ok:
        envelope = resolve(spec, ok)
        data = envelope.get("properties", {}).get("data")
        if data:
            table = field_table(spec, data)
            if table:
                lines += ["## Antwort: Felder in `data`", "", *table, ""]
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    spec = load_spec(sys.argv[1] if len(sys.argv) > 1 else None)
    endpoints_dir = REF_DIR / "endpoints"
    if endpoints_dir.exists():
        shutil.rmtree(endpoints_dir)
    endpoints_dir.mkdir(parents=True)

    taken: set[str] = set()
    index_rows: list[tuple[str, str, str, str, str]] = []
    for path, ops in spec["paths"].items():
        if not path.startswith("/v1/"):
            continue
        for method in METHODS:
            op = ops.get(method)
            if not op:
                continue
            slug = slug_for(method, path, taken)
            (endpoints_dir / f"{slug}.md").write_text(
                render_endpoint(spec, method, path, op), encoding="utf-8", newline="\n"
            )
            tag = (op.get("tags") or ["Sonstiges"])[0]
            index_rows.append((tag, method.upper(), path, cell(op.get("summary", "")), slug))

    index_rows.sort(key=lambda r: (r[0].lower(), r[2], r[1]))
    version = spec.get("info", {}).get("version", "?")
    out = [
        "# Endpoint-Index",
        "",
        f"Erzeugt aus der OpenAPI-Spezifikation (API-Version {version})"
        " mit `tools/build_reference.py`.",
        "Nicht von Hand bearbeiten.",
        "",
        "| Kategorie | Methode | Pfad | Zweck | Referenz |",
        "|---|---|---|---|---|",
    ]
    out += [
        f"| {t} | {m} | `{p}` | {s} | [endpoints/{slug}.md](endpoints/{slug}.md) |"
        for t, m, p, s, slug in index_rows
    ]
    (REF_DIR / "INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(index_rows)} Endpoints geschrieben nach {REF_DIR}")
    return check_skill_paths({(m, p) for _, m, p, _, _ in index_rows})


def check_skill_paths(known: set[tuple[str, str]]) -> int:
    """Jeder Pfad, den SKILL.md von Hand nennt, muss in der Spezifikation existieren."""
    skill_md = (REF_DIR.parent / "SKILL.md").read_text(encoding="utf-8")
    known_paths = {p for _, p in known}
    missing = []
    for method, path in re.findall(r"`(GET|POST) (v1/[a-z0-9/{}_-]+)", skill_md):
        if (method, "/" + path) not in known:
            missing.append(f"{method} {path}")
    for path in re.findall(r"call\.py (?:GET|POST) (v1/[a-z0-9/{}_-]+)", skill_md):
        if "/" + path not in known_paths:
            missing.append(path)
    for item in missing:
        print(
            f"FEHLER: SKILL.md nennt {item}, das gibt es in der Spezifikation nicht",
            file=sys.stderr,
        )
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
