# Zusatzbeitrag einer Krankenkasse (aktuell oder per Stichtag)

`GET /v1/gkv-zusatzbeitrag`

Kategorie: GKV-Zusatzbeitrag

Liefert den Zusatzbeitragssatz einer GKV-Kasse. Lookup via IK-Nummer (echte oder synthetischer Slug) ODER via Name-Substring (fuzzy). Optional Stichtag fuer historischen Lookup. Coverage ab 2021-10.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ik` | query | string |  | IK-Nummer oder synthetischer Slug (z.B. 'techniker-krankenkasse') |
| `name` | query | string |  | Name-Substring (fuzzy, mind. 2 Zeichen). Liefert ersten Treffer. |
| `stichtag` | query | string |  | Historischer Stichtag (YYYY-MM-DD). Default: aktueller Snapshot. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ik_nummer` | string | ja |  |  | Kennung der gefundenen Kasse: synthetischer Slug aus dem Namen (z. B. "techniker-krankenkasse"); bei Suche per name die ID des ersten Treffers. |
| `name` | string | ja |  |  | Name der Kasse aus der Kassen-Tabelle. |
| `zusatzbeitrag_prozent` | string | ja |  |  | Zusatzbeitragssatz in Prozent |
| `snapshot_datum` | string | ja |  |  | Aufnahmedatum des PDF-Snapshots |
| `quelle_url` | string | ja |  |  | Quelle (gkv:current oder wayback:TIMESTAMP) |
