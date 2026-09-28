# Krypto-Steuer-Rechner (§ 23 EStG Spot + § 32d KapESt Futures)

`POST /v1/krypto`

Kategorie: Krypto-Steuer

Berechnet die deutsche Krypto-Steuer fuer eine Single-Transaktion. Spot (priv. Veraeusserungsgeschaeft § 23 EStG): Haltefrist-Pruefung (>12 Monate = steuerfrei), Freigrenze 1.000 EUR ab 2024 (600 EUR bis 2023), bei Ueberschreitung progressive ESt via Differenzmethode (mit/ohne Krypto-Gewinn) plus Soli und ggf. Kirchensteuer. Futures/Derivate (§ 32d EStG): pauschale KapESt 25 % + Soli + KiSt, keine Haltefrist, keine Freigrenze; Verluste voll mit Kapitalertraegen verrechenbar – die fruehere 20.000-EUR-Grenze (§ 20 Abs. 6 Satz 5 EStG a.F.) wurde durch das Jahressteuergesetz 2024 abgeschafft.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `kaufdatum` | string | ja |  |  | Datum des Kaufs |
| `verkaufsdatum` | string | ja |  |  | Datum des Verkaufs |
| `kaufpreis` | number | ja |  |  | Anschaffungskosten in EUR |
| `verkaufspreis` | number | ja |  |  | Veraeusserungserloes in EUR |
| `gebuehren_kauf` | number |  | "0" |  | Transaktionsgebuehren beim Kauf |
| `gebuehren_verkauf` | number |  | "0" |  | Transaktionsgebuehren beim Verkauf |
| `steuerjahr` | integer |  | 2026 |  | Steuerjahr 2024-2026 |
| `transaktionsart` | enum | ja |  | spot, futures | 'spot' (§23 EStG) oder 'futures' (§32d KapESt) |
| `jahreseinkommen` | number |  | "0" |  | zvE OHNE Krypto-Gewinn (fuer Differenzmethode bei Spot) |
| `zusammenveranlagung` | boolean |  | false |  | Ehegatten-Splitting? (nur Spot relevant) |
| `kirchensteuer_ja` | boolean |  | false |  | Kirchensteuerpflichtig? |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (KiSt 8 % BY/BW, 9 % uebrige) |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "jahreseinkommen": 45000,
  "kaufdatum": "2023-06-15",
  "kaufpreis": 5000,
  "transaktionsart": "spot",
  "verkaufsdatum": "2024-08-20",
  "verkaufspreis": 8000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `gewinn` | string | ja |  |  |  |
| `haltefrist` | KryptoHaltefristInfo |  |  |  | Nur bei Spot – bei Futures null |
| `steuer` | KryptoSteuerSpot \| KryptoSteuerFutures | ja |  |  | Spot- oder Futures-Steuer-Aufschluesselung |
| `transaktionsart` | string | ja |  |  |  |
| `zusammenfassung` | KryptoZusammenfassung | ja |  |  |  |
