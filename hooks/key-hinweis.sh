#!/usr/bin/env bash
# SessionStart-Hook: weist einmalig darauf hin, dass ein RapidAPI-Key fehlt.
#
# Still, wenn RAPIDAPI_KEY in der Umgebung oder in der .env des Projekts steht.
# Der Hinweis erscheint nur einmal pro Installation (Merker im Plugin-Datenordner),
# damit ein global installiertes Plugin nicht jede Sitzung in jedem Projekt stoert.
# Der Key selbst wird nie gelesen oder ausgegeben, nur geprueft, ob er da ist.

if [ -n "${RAPIDAPI_KEY:-}" ]; then
  exit 0
fi

env_file="${CLAUDE_PROJECT_DIR:-.}/.env"
if [ -f "$env_file" ] && grep -Eq '^[[:space:]]*(export[[:space:]]+)?RAPIDAPI_KEY=["'"'"']?[^"'"'"'[:space:]]' "$env_file"; then
  exit 0
fi

marker=""
if [ -n "${CLAUDE_PLUGIN_DATA:-}" ]; then
  marker="$CLAUDE_PLUGIN_DATA/key-hinweis-gezeigt"
  if [ -f "$marker" ]; then
    exit 0
  fi
fi

cat <<'JSON'
{"systemMessage": "german-tax-skills: No RapidAPI key found. Put RAPIDAPI_KEY=your-key into the .env of your project (or set it as an environment variable) and restart Claude Code. Free key: https://rapidapi.com/rechnerhub/api/german-tax-calculator"}
JSON

if [ -n "$marker" ]; then
  mkdir -p "$CLAUDE_PLUGIN_DATA" && : > "$marker"
fi
exit 0
