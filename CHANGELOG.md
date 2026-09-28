# Changelog

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
