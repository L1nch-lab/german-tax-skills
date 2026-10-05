# Hebesatz-Historie einer Gemeinde

`GET /v1/hebesaetze-historie`

Kategorie: Hebesaetze-Historie

Liefert alle historisch gespeicherten Hebesatz-Staende fuer eine Gemeinde (AGS 8-stellig oder PLZ 5-stellig, genau einer von beiden). Coverage stand=2024 als Baseline; aeltere Jahre nach Manuel-Drop von hebesaetze_YYYY.csv ins data-Verzeichnis.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | query | string |  | 8-stelliger Amtlicher Gemeindeschluessel |
| `plz` | query | string |  | 5-stellige PLZ; bei mehreren Gemeinden 409 mit Kandidaten |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  |  |
| `eintraege` | array<HebesatzHistorieItem> | ja |  |  |  |
