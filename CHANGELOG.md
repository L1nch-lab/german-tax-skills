# Changelog

## [0.1.0] - 2026-09-28

### Added

- Skill `steuerrechner-api`: routes German tax, social security and benefit questions to the rechner-hub.de API on RapidAPI.
- Endpoint reference for 120 endpoints, generated from the OpenAPI spec.
- `call.py`: reads `RAPIDAPI_KEY` from the environment or `.env`, masks the key in all output, reports remaining quota and tells a used-up plan quota apart from a short-term rate limit.
- Claude Code plugin and marketplace manifests.
