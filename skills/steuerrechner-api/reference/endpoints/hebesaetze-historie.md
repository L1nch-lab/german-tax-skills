# Hebesatz-Historie einer Gemeinde

`GET /v1/hebesaetze-historie`

Kategorie: Hebesaetze-Historie

Liefert alle historisch gespeicherten Hebesatz-Staende fuer eine Gemeinde (AGS 8-stellig oder PLZ 5-stellig, genau einer von beiden). Coverage stand 2016 bis 2024, je Jahr rund 10.750 bis 11.060 Gemeinden.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | query | string |  | 8-stelliger Amtlicher Gemeindeschluessel |
| `plz` | query | string |  | 5-stellige PLZ; bei mehreren Gemeinden 409 mit Kandidaten |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  | 8-stelliger Amtlicher Gemeindeschlüssel der Gemeinde; bei Anfrage per plz die daraus aufgelöste AGS. |
| `eintraege` | array<HebesatzHistorieItem> | ja |  |  | Hebesatz-Stände der Gemeinde je Berichtsjahr, aufsteigend nach stand (Datenbestand ab 2016). |
