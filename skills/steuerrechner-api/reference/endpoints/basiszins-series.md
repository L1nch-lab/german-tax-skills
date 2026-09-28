# Komplette Basiszinssatz-Reihe seit 2002

`GET /v1/basiszins/series`

Kategorie: Basiszinssatz

Liefert alle halbjaehrlichen Eintraege ab 2002-01-01 sortiert (alt -> neu). Cache-Control: public, max-age=86400.

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<BasiszinsItem> | ja |  |  | Komplette Reihe sortiert alt -> neu |
| `erster_eintrag` | string | ja |  |  |  |
| `letzter_eintrag` | string | ja |  |  |  |
| `anzahl_eintraege` | integer | ja |  |  |  |
| `rechtsgrundlage` | string |  | "§247 Abs. 1 Satz 1 BGB" |  |  |
