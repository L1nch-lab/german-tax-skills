# Ungewichteter Jahresdurchschnitt aller Zusatzbeitragssaetze

`GET /v1/gkv-zusatzbeitrag/durchschnitt`

Kategorie: GKV-Zusatzbeitrag

Durchschnitt ueber alle PDF-Snapshots im angegebenen Jahr. Hinweis: nicht gewichtet nach Mitgliederzahl.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `jahr` | query | integer | ja | Berichtsjahr (Coverage 2021-2026 mit guter Snapshot-Dichte) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `jahr` | integer | ja |  |  |  |
| `durchschnitt_prozent` | string | ja |  |  | Ungewichteter Mittelwert aller Snapshots |
| `snapshot_count` | integer | ja |  |  | Anzahl Snapshots im Jahr |
