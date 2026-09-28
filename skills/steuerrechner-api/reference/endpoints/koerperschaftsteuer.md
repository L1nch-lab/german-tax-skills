# Koerperschaftsteuer / GmbH-Gesamtbelastung

`POST /v1/koerperschaftsteuer`

Kategorie: Koerperschaftsteuer

Berechnet die Gesamtsteuerbelastung einer GmbH: Koerperschaftsteuer (15%), Solidaritaetszuschlag, Gewerbesteuer und bei Ausschuettung Kapitalertragsteuer (25%). Inkl. Vergleich mit Einzelunternehmen (ESt + GewSt nach §35-Anrechnung). Hebesatz direkt oder per AGS/Gemeindename.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `gewinn` | number | ja |  |  | Zu versteuerndes Einkommen der Kapitalgesellschaft in EUR |
| `hebesatz` | integer |  |  |  | Gewerbesteuer-Hebesatz (oder ags/gemeinde zur Ermittlung) |
| `ags` | string |  |  |  | 8-stelliger AGS zur Hebesatz-Ermittlung |
| `gemeinde` | string |  |  |  | Gemeindename zur Hebesatz-Suche |
| `ausschuettung_prozent` | number |  | "100" |  | Anteil des Gewinns nach Steuern, der ausgeschuettet wird (0-100%) |
| `kirchenmitglied` | boolean |  | false |  | Ob der Gesellschafter kirchensteuerpflichtig ist |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland des Gesellschafters – bestimmt den KiSt-Satz auf die Ausschuettung (8% Bayern/Baden-Württemberg, 9% uebrige) |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "gewinn": 100000,
  "hebesatz": 490
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `koerperschaftsteuer` | string | ja |  |  | Koerperschaftsteuer 15% |
| `soli_kst` | string | ja |  |  | Soli auf KSt 5.5% |
| `gewerbesteuer` | string | ja |  |  | Gewerbesteuer |
| `belastung_thesaurierung` | string | ja |  |  | Gesamtbelastung Thesaurierung |
| `ausschuettung` | string | ja |  |  | Ausgeschuetteter Betrag in EUR |
| `kapitalertragsteuer` | string | ja |  |  | KapESt auf Ausschuettung |
| `soli_kapest` | string | ja |  |  | Soli auf KapESt |
| `kirchensteuer_kapest` | string | ja |  |  | Kirchensteuer auf KapESt |
| `belastung_ausschuettung` | string | ja |  |  | Gesamtbelastung inkl. Ausschuettung |
| `effektivbelastung_prozent` | string | ja |  |  | Effektive Gesamtbelastung in Prozent |
| `vergleich_einzelunternehmen` | string | ja |  |  | Steuerbelastung als EU |
| `vergleich_einzelunternehmen_prozent` | string | ja |  |  | EU-Belastung in Prozent |
| `ausschuettung_prozent` | string | ja |  |  | Angewendeter Ausschuettungsanteil |
