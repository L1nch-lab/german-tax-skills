# Hebesatz-Lookup nach AGS, PLZ oder Gemeindename

`GET /v1/hebesaetze`

Kategorie: Hebesaetze

Liefert Gewerbesteuer- und Grundsteuer-Hebesaetze, Einwohnerzahl und (ab Phase 5) Mietniveaustufe fuer eine oder mehrere Gemeinden. Genau einer der Parameter 'ags', 'plz', 'gemeinde' oder 'q' ist Pflicht. 'q' ist ein deprecated Alias fuer 'gemeinde'. Datenquelle: Destatis Realsteuervergleich 2024 (dl-de/by-2-0).

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | query | string |  | 8-stelliger Amtlicher Gemeindeschluessel |
| `plz` | query | string |  | 5-stellige Postleitzahl (ab Phase 5 verfuegbar) |
| `gemeinde` | query | string |  | Gemeindename (Substring-Match) |
| `bundesland` | query | string |  | Bundesland zum Filtern bei gemeinde-Suche |
| `q` | query | string |  | [deprecated] Alias fuer 'gemeinde', bleibt fuer Backward-Compat |
