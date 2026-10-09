# 10-Jahres-Reihe Hebesaetze-Aggregat per Bundesland (2016-2025)

`GET /v1/hebesaetze-aggregat`

Kategorie: Hebesaetze-Historie

Liefert den gewogenen Durchschnittssatz der Gewerbesteuer in Gemeinden ab 20.000 Einwohnern. Aggregat per Bundesland-Jahr-Kombination. 16 Bundeslaender x 10 Jahre = 160 Datenpunkte. Quelle: VdF/DIHK Daten und Fakten Realsteuer-Hebesaetze (Stand 01.09.2025).

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `bundesland` | query | string |  | Bundesland-Name (exakt, mit Umlauten, z.B. 'Baden-Württemberg'). Optional. |
| `jahr` | query | integer |  | Berichtsjahr 2016-2025. Optional. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `eintraege` | array<HebesatzAggregatItem> | ja |  |  | Durchschnittliche Gewerbesteuer-Hebesätze je Bundesland und Jahr (2016 bis 2025), sortiert nach Bundesland und Jahr; optional per bundesland oder jahr gefiltert. |
| `quelle` | string |  | "VdF Daten und Fakten Realsteuer-Hebesaetze (Stand 01.09.2025)" |  | Quellenangabe als fester Text "VdF Daten und Fakten Realsteuer-Hebesaetze (Stand 01.09.2025)". |
