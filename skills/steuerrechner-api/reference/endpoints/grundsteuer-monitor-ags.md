# Grundsteuerreform-Monitor 2025 einer Gemeinde (SH/NRW)

`GET /v1/grundsteuer-monitor/{ags}`

Kategorie: Grundsteuer-Monitor

Liefert Hebesatz-Fakten zur Grundsteuerreform 2025: fuer Schleswig-Holstein die Ist-Hebesaetze 2024/2025 (2025 vorlaeufig) samt Delta, fuer Nordrhein-Westfalen die aufkommensneutralen Referenz-Hebesaetze des Landes (Stand 18.06.2024) – plus, falls gemeldet, den tatsaechlich beschlossenen GrSt-B-Hebesatz 2025 aus der Hebesatz-Aenderungsstatistik. Andere Bundeslaender: 404.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | path | string | ja | 8-stelliger Amtlicher Gemeindeschluessel oder 5-stellige Postleitzahl. Gehoert die PLZ zu mehreren Gemeinden, kommt 409 mit den Kandidaten. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  | Amtlicher Gemeindeschluessel (8-stellig) |
| `land` | enum | ja |  | SH, NW | Bundesland-Kuerzel der Datenquelle |
| `gemeinde_name` | string | ja |  |  | Gemeindename laut Quelle |
| `hinweis` | string | ja |  |  | YMYL-Einordnung der Werte (vorlaeufig / Referenz, je nach Land) |
| `grundsteuer_a_2024` | integer |  |  |  | Grundsteuer A 2024 (SH, endgueltig), Prozent |
| `grundsteuer_a_2025` | integer |  |  |  | Grundsteuer A 2025 (SH, VORLAEUFIG), Prozent |
| `grundsteuer_b_2024` | integer |  |  |  | Grundsteuer B 2024 (SH, endgueltig), Prozent |
| `grundsteuer_b_2025` | integer |  |  |  | Grundsteuer B 2025 (SH, VORLAEUFIG; bei differenzierten Hebesaetzen der Wohngrundstuecke-Satz), Prozent |
| `grundsteuer_b_nichtwohn_2025` | integer |  |  |  | Grundsteuer B 2025 fuer Nichtwohngrundstuecke (SH, nur bei differenzierten Hebesaetzen), Prozent |
| `delta_a_2025_vs_2024` | integer |  |  |  | Grundsteuer A: 2025 minus 2024 (nur SH), Prozentpunkte |
| `delta_b_2025_vs_2024` | integer |  |  |  | Grundsteuer B: 2025 minus 2024 (nur SH), Prozentpunkte |
| `grst_a_neutral` | integer |  |  |  | Aufkommensneutraler Referenz-Hebesatz GrSt A (NRW), Prozent |
| `grst_b_neutral` | integer |  |  |  | Aufkommensneutraler Referenz-Hebesatz GrSt B einheitlich (NRW), Prozent |
| `grst_b_wohn_neutral` | integer |  |  |  | Aufkommensneutraler Referenz-Hebesatz GrSt B Wohngrundstuecke (NRW, Optionsmodell), Prozent |
| `grst_b_nichtwohn_neutral` | integer |  |  |  | Aufkommensneutraler Referenz-Hebesatz GrSt B Nichtwohngrundstuecke (NRW, Optionsmodell), Prozent |
| `grundsteuer_b_2025_beschlossen` | integer |  |  |  | Tatsaechlich beschlossener GrSt-B-Hebesatz 2025 (NRW, aus der Hebesatz-Aenderungsstatistik Stichtag 30.06.2025, falls gemeldet), Prozent |
| `delta_b_beschlossen_vs_neutral` | integer |  |  |  | GrSt B: beschlossen 2025 minus aufkommensneutrale Referenz (nur NRW, falls beschlossener Wert vorliegt), Prozentpunkte |
| `quelle` | string | ja |  |  | Quellen-Kennung der Datenzeile |
| `stand` | string | ja |  |  | Abruf-/Standsdatum der Quelle (YYYY-MM-DD) |
