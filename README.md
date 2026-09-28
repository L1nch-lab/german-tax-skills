<div align="center">

<img src="https://raw.githubusercontent.com/L1nch-lab/german-tax-skills/main/assets/banner.svg" alt="german-tax-skills" width="100%">

**German taxes, social security contributions and social benefits for AI agents: calculated by the [rechner-hub.de API](https://rechner-hub.de/steuerrechner-api/), not guessed by the model.**

[![RapidAPI](https://img.shields.io/badge/RapidAPI-German%20Tax%20Calculator-0055DA.svg)](https://rapidapi.com/rechnerhub/api/german-tax-calculator)
[![skills.sh](https://skills.sh/b/L1nch-lab/german-tax-skills)](https://skills.sh/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/L1nch-lab/german-tax-skills/blob/main/LICENSE)
[![CI](https://github.com/L1nch-lab/german-tax-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/L1nch-lab/german-tax-skills/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Dependencies: 0](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](https://github.com/L1nch-lab/german-tax-skills/blob/main/pyproject.toml)

[Install](#install) · [Quickstart](#quickstart) · [Get an API key on RapidAPI](https://rapidapi.com/rechnerhub/api/german-tax-calculator) · [API docs](https://rechner-hub.de/steuerrechner-api/)

</div>

# german-tax-skills

- 🧮 **120 endpoints**: payroll, income and capital taxes, property, social benefits, reference data
- 🚫 **No guessing**: the agent never estimates a tax figure, it calls the API or says it can't
- 🔑 **Key stays local**: read from `.env` or the environment, masked in every output, never asked for in the chat
- 📉 **Quota-aware**: warns before your RapidAPI plan runs out and stops cleanly when it has
- 🪶 **Zero dependencies**: Python standard library only
- 🐍 **Python 3.10 – 3.14**: tested on Linux, Windows and macOS

> 🇩🇪 **Deutsch:** weiter unten gibt es eine [Kurzfassung auf Deutsch](#deutsch).

---

## Quickstart

After [installing](#install) and [setting your key](#set-your-api-key), just ask:

> *My employer can spend 6,000 € a month on me in total. What gross salary is that, and how much do I keep? Tax class 1, North Rhine-Westphalia.*

The skill reads the endpoint reference, then runs:

```bash
python3 scripts/call.py POST v1/lohnkosten-netto   '{"lohnkosten_ziel": 6000, "steuerklasse": 1, "bundesland": "Nordrhein-Westfalen"}'
```

and gets back (real response, shortened):

```json
{
  "success": true,
  "data": {
    "brutto_monat": "4888.38",
    "netto_monat": "3072.91",
    "lohnsteuer_monat": "752.25",
    "soli_monat": "0.0",
    "sv_gesamt_monat": "1063.22",
    "ag_gesamt": "1111.62"
  },
  "input_echo": {
    "kirchensteuer": false,
    "kinder": 0,
    "geburtsjahr": 1985,
    "kv_zusatzbeitrag": "2.9"
  },
  "meta": { "tax_year": 2026 }
}
```

The answer leads with the numbers: 6,000 € of employer costs mean 4,888.38 € gross and 3,072.91 € net, after 752.25 € income tax and 1,063.22 € social security. It also says which defaults it assumed (no church tax, no children, born 1985, average health insurance surcharge of 2.9 %), because each of them changes the result, and it mentions the tax year.

## What it covers

120 endpoints, including:

- **Payroll:** Brutto-Netto, Netto-Brutto, employer costs, Minijob, Midijob, company car, Christmas bonus, severance pay
- **Income and capital taxes:** Einkommensteuer, Kapitalertragsteuer, crypto, Vorabpauschale, Progressionsvorbehalt
- **Property and business:** Grunderwerbsteuer, Grundsteuer, Gewerbesteuer, municipal Hebesätze, AfA, Kleinunternehmer
- **Social benefits:** Elterngeld, ALG I, Kurzarbeitergeld, Bürgergeld, Wohngeld, Kindergeld, Kinderzuschlag, BAföG
- **Reference data:** current statutory values, GKV-Zusatzbeitrag per health insurer, Basiszinssatz, Düsseldorfer Tabelle

The full list is in [`skills/steuerrechner-api/reference/INDEX.md`](skills/steuerrechner-api/reference/INDEX.md).

## Requirements

- A RapidAPI key with a subscription to the **[German Tax Calculator on RapidAPI](https://rapidapi.com/rechnerhub/api/german-tax-calculator)**. The free Basic plan (50 requests per day) is enough to try it.
- Python 3.10 or newer. The skill only uses the standard library.
- Outbound HTTPS to `german-tax-calculator.p.rapidapi.com`. This works in Claude Code. The claude.ai web sandbox usually blocks it.

## Install

**Claude Code plugin:**

```text
/plugin marketplace add L1nch-lab/german-tax-skills
/plugin install german-tax-skills@l1nch-lab
```

**Any agent that reads the Agent Skills format** (Claude Code, Cursor, Codex and others):

```bash
npx skills add L1nch-lab/german-tax-skills
```

**By hand:** copy `skills/steuerrechner-api/` to `~/.claude/skills/`.

## Set your API key

Put the key in a `.env` file in your project folder:

```text
RAPIDAPI_KEY=your-key-here
```

or export it as an environment variable. The skill reads it from there, never prints it and never asks you to paste it into the chat. Keep `.env` out of version control.

If you installed the Claude Code plugin and no key is set, Claude Code shows a one-time hint with these steps when a session starts.

A key in `userConfig` would not work here: Claude Code does not pass plugin options to commands run through the Bash tool.

## Quota

| Plan | Requests |
| --- | --- |
| Basic (free) | 50 per day |
| Pro | 1,000 per day |
| Ultra | 300,000 per month |

Plans and prices: [rapidapi.com/rechnerhub/api/german-tax-calculator/pricing](https://rapidapi.com/rechnerhub/api/german-tax-calculator/pricing)

After each call the script checks RapidAPI's rate limit headers. When the quota is nearly used up, Claude tells you with the result. When it is exhausted, Claude says so, tells you when it resets and does not retry.

## How it works

```text
skills/steuerrechner-api/
├── SKILL.md              rules and workflow for the agent
├── reference/            one file per endpoint, generated from the OpenAPI spec
└── scripts/call.py       calls the API through RapidAPI
```

The rules that matter most:

1. Never calculate a tax, contribution or benefit itself, not even as a rough estimate.
2. Read the endpoint reference before the first call. Never guess field names.
3. Say how many calls it will make before making more than three.
4. Report the assumptions from `input_echo` and the notes from `data.hinweise`.

## Development

```bash
pip install --group dev      # pip >= 25.1
pytest
ruff check . && ruff format --check .
python tools/build_reference.py    # regenerate the reference from the live API spec
```

`tools/build_reference.py` also fails if `SKILL.md` mentions an endpoint that does not exist. A weekly workflow flags when the reference no longer matches the live API.

## Background

The calculations come from the [rechner-hub.de API](https://rechner-hub.de/steuerrechner-api/). The same calculators are available in the browser on [rechner-hub.de](https://rechner-hub.de/). For income tax only, without an API, see [`lohnsteuer-bmf`](https://github.com/L1nch-lab/lohnsteuer-bmf).

## Disclaimer

The results are calculations based on current German law, not tax advice. Provided as is, without warranty.

## Deutsch

Agent-Skill für deutsche Steuern, Sozialabgaben und Sozialleistungen. Claude Code und andere Agenten rechnen damit nicht selbst, sondern fragen die [Steuerrechner-API von rechner-hub.de](https://rechner-hub.de/steuerrechner-api/) ab: 120 Endpoints von Brutto-Netto über Abfindung und Elterngeld bis zu den Hebesätzen deiner Gemeinde.

- **Installieren:** `/plugin marketplace add L1nch-lab/german-tax-skills`, dann `/plugin install german-tax-skills@l1nch-lab`
- **Key:** [German Tax Calculator auf RapidAPI](https://rapidapi.com/rechnerhub/api/german-tax-calculator) abonnieren (Basic mit 50 Anfragen am Tag ist kostenlos) und `RAPIDAPI_KEY=...` in die `.env` im Projektordner schreiben
- **Ohne Key im Browser rechnen:** [rechner-hub.de](https://rechner-hub.de/)

Die Ergebnisse sind Berechnungen, keine Steuerberatung.

## License

The code and the generated endpoint reference in this repository are licensed under [MIT](LICENSE).

The license does not cover the rechner-hub.de API itself, its calculations or data, or the names "rechner-hub" and "rechner-hub.de". Using the API is subject to the plan you subscribe to on [RapidAPI](https://rapidapi.com/rechnerhub/api/german-tax-calculator) and RapidAPI's terms.
