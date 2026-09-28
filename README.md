<div align="center">

# german-tax-skills

**Agent skills that calculate German taxes, social security contributions and social benefits through the [rechner-hub.de API](https://rechner-hub.de/steuerrechner-api/) instead of letting the model guess.**

[![RapidAPI](https://img.shields.io/badge/RapidAPI-German%20Tax%20Calculator-0055DA.svg)](https://rapidapi.com/rechnerhub/api/german-tax-calculator)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/L1nch-lab/german-tax-skills/blob/main/LICENSE)
[![CI](https://github.com/L1nch-lab/german-tax-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/L1nch-lab/german-tax-skills/actions/workflows/ci.yml)
[![Dependencies: 0](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](https://github.com/L1nch-lab/german-tax-skills/blob/main/pyproject.toml)

[Install](#install) · [Get an API key on RapidAPI](https://rapidapi.com/rechnerhub/api/german-tax-calculator) · [API docs](https://rechner-hub.de/steuerrechner-api/) · [rechner-hub.de](https://rechner-hub.de/)

</div>

Ask Claude Code *"How much net do I keep from 4,200 € gross, tax class 1, Bavaria?"* and the skill picks the right endpoint, asks for missing required inputs, calls the API and reports the result together with the assumptions it used. It never estimates a tax figure itself.

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
pip install -e ".[dev]"
pytest
ruff check . && ruff format --check .
python tools/build_reference.py    # regenerate the reference from the live API spec
```

`tools/build_reference.py` also fails if `SKILL.md` mentions an endpoint that does not exist. A weekly workflow flags when the reference no longer matches the live API.

## Background

The calculations come from the [rechner-hub.de API](https://rechner-hub.de/steuerrechner-api/). The same calculators are available in the browser on [rechner-hub.de](https://rechner-hub.de/). For income tax only, without an API, see [`lohnsteuer-bmf`](https://github.com/L1nch-lab/lohnsteuer-bmf).

## Disclaimer

The results are calculations based on current German law, not tax advice. Provided as is, without warranty.

## License

The code and the generated endpoint reference in this repository are licensed under [MIT](LICENSE).

The license does not cover the rechner-hub.de API itself, its calculations or data, or the names "rechner-hub" and "rechner-hub.de". Using the API is subject to the plan you subscribe to on [RapidAPI](https://rapidapi.com/rechnerhub/api/german-tax-calculator) and RapidAPI's terms.
