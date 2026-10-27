# Changelog

## [0.2.6] - 2026-10-27

### Changed

- Endpoint reference regenerated against the live API (version 2026.52). `fruehstartrente` now cites the FrühStRG as passed by the Bundestag on 16.10.2026 (BT-Drs. 21/7864, 21/8606) instead of the ministry draft; the Bundesrat's consent is still pending.

### Fixed

- `tools/build_reference.py` labels decimal fields as `number` again. Since pydantic 2.14 the API schema drops the pattern on the string branch of decimal fields, and the generator only folded that branch away when the pattern was present, so 70 endpoint files would have shown `number | string`.

## [0.2.5] - 2026-10-17

### Added

- Two endpoints, now 122: `riester` computes the subsidy of an existing Riester contract for one contribution year (minimum own contribution from the previous year's income, basic and child allowances, the spouse's allowance, special-expenses deduction with the most-favourable test), and `policenvergleich` compares a gross-premium against a net-premium private pension policy at equal contributions.

### Changed

- Endpoint reference regenerated against the live API (version 2026.52, addendum). `altersvorsorgedepot` takes `zve`, `zusammenveranlagung`, `ehepartner_mittelbar` and `vorjahreseinkommen`, returns `zve_angesetzt` and the spouse's allowance, and compares against a Riester contract that stays under the old law. `minijob` is pension-insured by default with the employee's share and takes `rv_befreit` for the exemption.
- CI runs the tests on Ubuntu only.

## [0.2.4] - 2026-10-09

### Changed

- Endpoint reference regenerated for API version 2026.52. `rente` and `rentenluecke` return the net pension after health and long-term care insurance and income tax instead of a flat 85 %, `rente` computes pension points per § 70 SGB VI (lower pension when `lohnwachstum` > 0), `szenario/jobwechsel` takes `versicherungsmonate`, `altersvorsorgedepot` takes `kinder_vor_2008`, and `krankenkassenbeitrag` accepts `kv_zusatzbeitrag` as an alias. Four response fields carry a new name and the old one is marked deprecated in the reference (`stkl_vergleich_netto`, `mehrkapital_eigenbeitraege_rente`, `ohne_kest`, `preis_mit_regulaerer_ust`).

### Added

- A municipality name that matches several municipalities and none exactly answers with HTTP 409 `GEMEINDE_AMBIGUOUS` and the list of candidates (`gewerbesteuer`, its batch, `koerperschaftsteuer`). `SKILL.md` tells the agent to show the candidates and repeat the call with the chosen AGS; `call.py` names the municipality case in its hint instead of the postal-code text.

## [0.2.3] - 2026-10-05

### Changed

- Endpoint reference regenerated for API version 2026.51. The municipal endpoints (`mietstufe`, `einkommen`, `schulden`, `finanzamt`, `grundsteuer-monitor`, `pv-ertrag`, `bauland`, `zensus/wohnungen`) take a 5-digit postal code in place of the AGS, `hebesaetze-historie` takes `plz` as an alternative to `ags`, and `gewerbesteuer` and `koerperschaftsteuer` accept `plz` to look up the Hebesatz.

### Added

- A postal code that belongs to several municipalities answers with HTTP 409 `PLZ_AMBIGUOUS` and the list of candidates. `SKILL.md` tells the agent to show the candidates and repeat the call with the chosen AGS; `call.py` prints the same hint.

## [0.2.2] - 2026-10-01

### Fixed

- `call.py` finds `RAPIDAPI_KEY` in a `.env` written by PowerShell 5.1 (UTF-8 with BOM). Before, the BOM hid the key on the first line.
- `call.py` writes UTF-8 on Windows. Piped output used cp1252, so agents saw `�247 BGB` instead of `§247 BGB` and broken umlauts.
- An agent that changed into the skill folder before calling `call.py` got "no API key" although the project had a `.env`. `SKILL.md` now says not to `cd`, and `call.py` names the cause when it happens.

## [0.2.1] - 2026-10-01

### Added

- `plugin.json` at the repository root in the Agent Plugins format, so the plugin installs in the GitHub Copilot CLI. The Claude Code manifest in `.claude-plugin/` stays the source; CI checks that both agree.

## [0.2.0] - 2026-09-28

### Added

- Claude Code plugin: a one-time hint at session start when no `RAPIDAPI_KEY` is found in the environment or the project's `.env` (`hooks/key-hinweis.sh`). It never reads or prints the key itself.

### Fixed

- `SKILL.md` tells agents other than Claude Code (Codex, Cursor, Copilot, Gemini CLI …) to replace `${CLAUDE_SKILL_DIR}` with the skill folder. Before, the shell expanded it to an empty string and the script call failed.

## [0.1.0] - 2026-09-28

### Added

- Skill `steuerrechner-api`: routes German tax, social security and benefit questions to the rechner-hub.de API on RapidAPI.
- Endpoint reference for 120 endpoints, generated from the OpenAPI spec.
- `call.py`: reads `RAPIDAPI_KEY` from the environment or `.env`, masks the key in all output, reports remaining quota and tells a used-up plan quota apart from a short-term rate limit.
- Claude Code plugin and marketplace manifests.
