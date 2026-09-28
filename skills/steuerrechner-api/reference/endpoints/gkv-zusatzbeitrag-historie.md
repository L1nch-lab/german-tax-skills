# Time-Series aller Zusatzbeitragsstaende einer Kasse

`GET /v1/gkv-zusatzbeitrag/historie`

Kategorie: GKV-Zusatzbeitrag

Komplette Snapshot-Liste fuer eine Kasse, sortiert chronologisch.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ik` | query | string | ja | IK-Nummer oder synthetischer Slug |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ik_nummer` | string | ja |  |  |  |
| `name` | string | ja |  |  |  |
| `eintraege` | array<GkvHistorieItem> | ja |  |  |  |
