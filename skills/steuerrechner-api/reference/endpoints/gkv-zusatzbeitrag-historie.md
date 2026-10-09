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
| `ik_nummer` | string | ja |  |  | Kennung der Kasse (meist synthetischer Slug), zu der die Historie gehört. |
| `name` | string | ja |  |  | Name der Kasse. |
| `eintraege` | array<GkvHistorieItem> | ja |  |  | Alle Snapshots des Zusatzbeitrags dieser Kasse, aufsteigend nach snapshot_datum. Aufeinanderfolgende Einträge können denselben Satz tragen. |
