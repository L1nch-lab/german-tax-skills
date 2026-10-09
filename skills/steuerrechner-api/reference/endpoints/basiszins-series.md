# Komplette Basiszinssatz-Reihe seit 2002

`GET /v1/basiszins/series`

Kategorie: Basiszinssatz

Liefert alle halbjaehrlichen Eintraege ab 2002-01-01 sortiert (alt -> neu). Cache-Control: public, max-age=86400.

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<BasiszinsItem> | ja |  |  | Komplette Reihe sortiert alt -> neu |
| `erster_eintrag` | string | ja |  |  | Geltungsbeginn des ältesten Eintrags der Reihe (ISO-Datum), derzeit 2002-01-01. |
| `letzter_eintrag` | string | ja |  |  | Geltungsbeginn des jüngsten Eintrags der Reihe (ISO-Datum, 1.1. oder 1.7.). |
| `anzahl_eintraege` | integer | ja |  |  | Anzahl der Halbjahres-Einträge in items. |
| `rechtsgrundlage` | string |  | "§247 Abs. 1 Satz 1 BGB" |  | Rechtsgrundlage der Reihe als fester Text "§247 Abs. 1 Satz 1 BGB". |
