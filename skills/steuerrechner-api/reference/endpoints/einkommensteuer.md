# Einkommensteuer-Tarif

`POST /v1/einkommensteuer`

Kategorie: Einkommensteuer

Berechnet die Einkommensteuer aus dem zu versteuernden Einkommen (zvE) nach §32a EStG. Liefert ESt, Soli, Kirchensteuer, Grenzsteuersatz, Durchschnittssteuersatz und Tarifzone. Unterstuetzt Ehegattensplitting und Steuerjahre 2024-2026.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `zve` | number | ja |  |  | Zu versteuerndes Einkommen in EUR |
| `zusammenveranlagung` | boolean |  | false |  | True fuer Ehegattensplitting (§32a Abs. 5 EStG) |
| `kirchensteuer` | boolean |  | false |  | True wenn kirchensteuerpflichtig |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (fuer Kirchensteuersatz 8%/9%) |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "zve": 50000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `einkommensteuer` | string | ja |  |  | Einkommensteuer in EUR |
| `solidaritaetszuschlag` | string | ja |  |  | Solidaritaetszuschlag in EUR |
| `kirchensteuer` | string | ja |  |  | Kirchensteuer in EUR |
| `steuer_gesamt` | string | ja |  |  | ESt + Soli + KiSt gesamt in EUR |
| `grenzsteuersatz` | string | ja |  |  | Grenzsteuersatz in Prozent (marginale Belastung) |
| `durchschnittssteuersatz` | string | ja |  |  | Durchschnittssteuersatz in Prozent (nur ESt/zvE) |
| `belastungsquote` | string | ja |  |  | Gesamtbelastung in Prozent (ESt+Soli+KiSt/zvE) |
| `tarifzone` | TarifzoneModel | ja |  |  | Aktuelle Tarifzone |
| `grundfreibetrag` | string | ja |  |  | Grundfreibetrag in EUR (verdoppelt bei Splitting) |
