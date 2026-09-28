# Progressionsvorbehalt-Rechner (§32b EStG)

`POST /v1/progressionsvorbehalt`

Kategorie: Progressionsvorbehalt

Berechnet die steuerliche Mehrbelastung durch den Progressionsvorbehalt bei Lohnersatzleistungen (ALG I, Kurzarbeitergeld, Elterngeld, Krankengeld). Die Leistungen sind steuerfrei, erhoehen aber den Steuersatz auf das uebrige Einkommen.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `einkommen` | number | ja |  |  | Zu versteuerndes Einkommen in EUR (ohne Lohnersatzleistung) |
| `lohnersatzleistung` | number | ja |  |  | Steuerfreie Lohnersatzleistung in EUR (ALG I, KUG, Elterngeld, Krankengeld). Negativ moeglich fuer negativen Progressionsvorbehalt. |
| `zusammenveranlagung` | boolean |  | false |  | True fuer Ehegattensplitting |
| `kirchensteuer` | boolean |  | false |  | True wenn kirchensteuerpflichtig |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (fuer Kirchensteuersatz 8%/9%) |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "einkommen": 40000,
  "lohnersatzleistung": 10000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `einkommen` | string | ja |  |  | Zu versteuerndes Einkommen in EUR |
| `lohnersatzleistung` | string | ja |  |  | Steuerfreie Lohnersatzleistung in EUR |
| `est_ohne` | string | ja |  |  | Einkommensteuer ohne Progressionsvorbehalt |
| `soli_ohne` | string | ja |  |  | Soli ohne Progressionsvorbehalt |
| `kist_ohne` | string | ja |  |  | Kirchensteuer ohne Progressionsvorbehalt |
| `gesamt_ohne` | string | ja |  |  | Gesamtsteuer ohne Progressionsvorbehalt |
| `steuersatz_ohne` | string | ja |  |  | Durchschnitts-Steuersatz ohne Progression in % |
| `est_mit_progression` | string | ja |  |  | ESt mit Progressionsvorbehalt |
| `soli_mit` | string | ja |  |  | Soli mit Progressionsvorbehalt |
| `kist_mit` | string | ja |  |  | Kirchensteuer mit Progressionsvorbehalt |
| `gesamt_mit` | string | ja |  |  | Gesamtsteuer mit Progressionsvorbehalt |
| `steuersatz_mit` | string | ja |  |  | Durchschnitts-Steuersatz mit Progression in % |
| `mehrbelastung_est` | string | ja |  |  | ESt-Mehrbelastung durch Progression |
| `mehrbelastung_soli` | string | ja |  |  | Soli-Mehrbelastung |
| `mehrbelastung_kist` | string | ja |  |  | KiSt-Mehrbelastung |
| `mehrbelastung_gesamt` | string | ja |  |  | Gesamte Mehrbelastung in EUR |
