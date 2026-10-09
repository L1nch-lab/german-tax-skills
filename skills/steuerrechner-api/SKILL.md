---
name: steuerrechner-api
description: Calculate German taxes, social security contributions and social benefits through the rechner-hub.de API (RapidAPI "German Tax Calculator", 120 endpoints) instead of estimating them. Use for Brutto-Netto / net salary, Lohnsteuer, Einkommensteuer, Minijob/Midijob, employer costs, Abfindung, Firmenwagen, Kapitalertragsteuer, Krypto-Steuer, Grunderwerbsteuer, Erbschaft-/Schenkungsteuer, Gewerbesteuer and municipal Hebesätze, Rente, Elterngeld, ALG I, Bürgergeld, Wohngeld, Kindergeld, Kindesunterhalt, GKV-Zusatzbeitrag, Basiszinssatz and similar German figures, and for integrating these calculations into code. Requires a RapidAPI key in RAPIDAPI_KEY.
license: MIT
compatibility: Needs Python 3.10+ and outbound HTTPS to german-tax-calculator.p.rapidapi.com. Built for Claude Code; claude.ai sandboxes usually block the network call.
allowed-tools: Read Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/call.py *) Bash(python ${CLAUDE_SKILL_DIR}/scripts/call.py *)
---

# Steuerrechner-API

This skill answers German tax, social security and benefit questions by calling the rechner-hub.de API. The API implements the official formulas (BMF Programmablaufplan, SGB, EStG) and cites its sources. Your job is to pick the right endpoint, collect the inputs, call it, and report what it returned.

Reply in the user's language. Field names and API responses are German.

## Hard rules

1. **Never calculate a tax, contribution or benefit yourself**, not even as a "rough estimate" and not as a fallback when a call fails. This includes partial figures and impact estimates such as "Kirchensteuer would be about 40 € a month" or "that is a spread of roughly 46 €". Only report euro amounts the API returned. When explaining why an input matters, say *what* it affects, not *by how much*. If the user wants a variant (other Steuerklasse, other salary), make another call.
2. **Never guess field names or values.** Read the endpoint's reference file before the first call to that endpoint.
3. **Never print, log or echo the API key.** Never ask the user to paste it into the chat. If they paste it anyway, tell them to rotate it in the RapidAPI dashboard.
4. **Say how many calls you will make before making more than three.** Every call counts against the user's RapidAPI quota. For many rows (payroll lists, salary tables) use the `/batch` endpoint (up to 1,000 items in one call) instead of looping.
5. The results are calculations, not tax advice. Say so once, in one sentence, when you present a result that someone might act on.

## Workflow

The commands below call `scripts/call.py` inside this skill's folder. Claude Code fills in `${CLAUDE_SKILL_DIR}` by itself. In any other agent (Codex, Cursor, Copilot, Gemini CLI and others), replace `${CLAUDE_SKILL_DIR}` with the absolute path of the folder that contains this `SKILL.md`, because the shell would otherwise expand it to an empty string.

### 1. Check the key

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/call.py --check
```

(Use `python` instead of `python3` if `python3` is not found.)

Run the script from the project folder and do not `cd` into the skill folder first: the `.env` is looked up in the current working directory.

If no key is found, stop and explain, without asking for the key itself:
- Subscribe to the API on RapidAPI (the free plan is enough to start): https://rapidapi.com/rechnerhub/api/german-tax-calculator
- Put the key into a `.env` file in the project folder (`RAPIDAPI_KEY=...`) or set it as an environment variable, then restart Claude Code if it was set in the shell profile.

### 2. Find the endpoint

Read [reference/INDEX.md](reference/INDEX.md). It lists every endpoint by category with a one-line purpose. Then read the linked file in `reference/endpoints/`. It has the full field table (type, required, default, allowed values), an example body and the response fields.

Common starting points:

| Question | Endpoint | Calculator on rechner-hub.de |
|---|---|---|
| Net salary from gross | `POST v1/brutto-netto` | https://rechner-hub.de/brutto-netto/ |
| Gross needed for a target net | `POST v1/netto-brutto` | https://rechner-hub.de/netto-brutto-rechner/ |
| What an employee costs the employer | `POST v1/arbeitgeber-kosten` | https://rechner-hub.de/arbeitgeberkosten-rechner/ |
| Income tax on annual taxable income (zvE) | `POST v1/einkommensteuer` | https://rechner-hub.de/einkommensteuer-rechner/ |
| Minijob / Midijob | `POST v1/minijob`, `POST v1/midijob` | https://rechner-hub.de/minijob-rechner/, https://rechner-hub.de/midijob-rechner/ |
| Severance pay | `POST v1/abfindung` | https://rechner-hub.de/abfindungsrechner/ |
| Company car | `POST v1/firmenwagen` | https://rechner-hub.de/firmenwagen-rechner/ |
| Capital gains / crypto | `POST v1/kapitalertragsteuer`, `POST v1/krypto` | https://rechner-hub.de/krypto-steuer/ (crypto only) |
| Real estate transfer tax | `POST v1/grunderwerbsteuer` | https://rechner-hub.de/grunderwerbsteuer/ |
| Municipal trade/property tax rates | `GET v1/hebesaetze?plz=...` | https://rechner-hub.de/gewerbesteuer-hebesatz-ranking/ |
| Current statutory values (Grundfreibetrag, BBG, ...) | `GET v1/werte/current` | |

Only link calculator URLs from this table. For anything else link https://rechner-hub.de/ and do not construct a URL yourself.

If the question does not match any endpoint, say so. Do not answer it from your own knowledge as if the API had.

### 3. Collect the inputs

- **Required fields:** ask for every required field you cannot take from the conversation. Ask all missing ones in one message.
- **Fields with defaults:** do not interrogate the user. Use the default, but name the assumptions that change the result noticeably. For salary endpoints these are usually Bundesland, Kirchensteuer, Kinder, Geburtsjahr (childless surcharge in Pflegeversicherung), KV-Zusatzbeitrag and the tax year.
- Money values are EUR. Check in the reference whether a field is monthly or annual; `bruttolohn` in `brutto-netto` is **monthly**.

### 4. Call

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/call.py POST v1/brutto-netto '{"bruttolohn": 4200, "steuerklasse": 1, "bundesland": "Bayern"}'
python3 ${CLAUDE_SKILL_DIR}/scripts/call.py GET v1/hebesaetze --query plz=80331
```

- Write the path **without a leading slash** (`v1/...`). Git Bash on Windows rewrites `/v1/...` into a file path.
- For long bodies write the JSON to a temporary file and pass `--body-file <file>`.
- `--dry-run` shows the request without sending it (the key is masked).
- After a successful call the script prints the remaining quota to stderr. If it prints `WARNUNG: Kontingent fast aufgebraucht`, pass that on to the user together with the result, and before any further calls say how many are left.

### 5. Report

Every response has the same envelope: `success`, `data`, `input_echo`, `meta`.

- Lead with the numbers the user asked for, from `data`, with units and period (monthly / annual).
- State the inputs that were used, from `input_echo`, including defaults the user did not set.
- Pass on anything in `data.hinweise`. These notes flag edge cases, such as a value that is not comparable or an input that was capped.
- Mention the tax year from `meta.tax_year`.
- If the user wants to check the result interactively, link the calculator from the table in step 2 (or https://rechner-hub.de/ if none is listed).

## Errors

| Exit / status | Meaning | What to do |
|---|---|---|
| exit 2 | No key found | Step 1 |
| HTTP 401 | Key invalid | Ask the user to check the key in the RapidAPI dashboard |
| HTTP 403 "not subscribed" | Key valid, but no plan for this API | Subscribe to the free plan (link above) |
| HTTP 422 | Input rejected | Read the error detail, fix field names/values against the reference, retry once |
| HTTP 409 `PLZ_AMBIGUOUS` | The postal code belongs to several municipalities | Show the user the candidates from `error.details` (name, Bundesland) and ask which one is meant, unless the conversation already names it. Then repeat the call with that 8-digit `ags`. Never pick the first candidate |
| HTTP 409 `GEMEINDE_AMBIGUOUS` | The municipality name (`gemeinde` on `gewerbesteuer`, its batch, `koerperschaftsteuer`) matches several municipalities and none exactly, e.g. `Frankfurt` | Same as above: show the candidates from `error.details` (name, Bundesland), ask which one is meant, then repeat with that 8-digit `ags`. An exact name such as `Berlin` or `München` needs no AGS |
| exit 4 (HTTP 429) | The request quota of the user's RapidAPI plan is used up (daily on Basic and Pro, monthly on Ultra) | Stop. Tell the user plainly that the RapidAPI request limit is exceeded, when it resets (the script prints it) and that a bigger plan is available (the script prints the link). Do not retry |
| exit 5 (HTTP 429) | Rate limit: too many requests in a short time | Tell the user. Retry at most once after a short pause, and for many rows switch to the `/batch` endpoint |
| exit 3 | Network error | Report it. In a sandbox without internet the skill cannot work |

## RapidAPI plans

| Plan | Requests |
|---|---|
| Basic (free) | 50 per day |
| Pro | 1,000 per day |
| Ultra | 300,000 per month |

Use this when the quota runs out or gets low: name the plan that would cover the user's volume. Do not quote prices; they are on the pricing page the script links to.

## Integrating into code

When the user wants the calculation inside their own application, show a request against `https://german-tax-calculator.p.rapidapi.com` with the headers `X-RapidAPI-Key` (read from an environment variable, never hard-coded) and `X-RapidAPI-Host: german-tax-calculator.p.rapidapi.com`. Take field names from the reference file. For income tax only (Lohnsteuer/Einkommensteuer) there is also an offline Python package: `pip install lohnsteuer-bmf`.
