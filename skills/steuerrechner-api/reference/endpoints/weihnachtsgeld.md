# Sonderzahlung / 13. Gehalt / Weihnachtsgeld – Netto-Rechner

`POST /v1/weihnachtsgeld`

Kategorie: Weihnachtsgeld

Berechnet die Nettoauszahlung einer Sonderzahlung – egal ob 13. Monatsgehalt, Weihnachtsgeld, Urlaubsgeld oder Bonus. Alle werden steuerlich identisch als sonstiger Bezug (§39b Abs. 3 EStG) behandelt: Lohnsteuer nach der Jahreslohnsteuer-Differenzmethode, ohne Sonder-Ermaessigung (eine 'Sechstelregelung' gibt es im deutschen Recht nicht). Die SV-Beitraege werden als Einmalzahlung nach § 23a Abs. 3 SGB IV bis zur anteiligen Jahres-BBG verbeitragt; der Zahlungsmonat folgt aus sonderzahlung_typ (weihnachtsgeld=November, bonus=Dezember, urlaubsgeld=Juni).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `monatslohn` | number | ja |  |  | Regulaeres monatliches Bruttogehalt in EUR |
| `sonderzahlung` | number | ja |  |  | Brutto-Sonderzahlung (Weihnachtsgeld, Bonus) in EUR |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) |
| `kinder` | number |  | "0" |  | Kinderfreibetraege (0, 0.5, 1, 1.5, ...) |
| `kirchensteuer` | boolean |  | false |  | True wenn Kirchensteuer abzufuehren ist |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (relevant fuer Kirchensteuer-Satz) |
| `sonderzahlung_typ` | enum |  | "weihnachtsgeld" | weihnachtsgeld, bonus, urlaubsgeld | Art der Sonderzahlung – bestimmt den angenommenen Zahlungsmonat fuer die SV-Verbeitragung nach § 23a Abs. 3 SGB IV (anteilige Jahres-BBG): weihnachtsgeld=November, bonus=Dezember, urlaubsgeld=Juni |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "monatslohn": 4000,
  "sonderzahlung": 4000,
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_sonderzahlung` | string | ja |  |  | Brutto-Sonderzahlung in EUR |
| `lohnsteuer` | string | ja |  |  | Lohnsteuer auf die Sonderzahlung in EUR (sonstiger Bezug, §39b Abs. 3 EStG) |
| `soli` | string | ja |  |  | Solidaritaetszuschlag in EUR |
| `kirchensteuer` | string | ja |  |  | Kirchensteuer in EUR |
| `sv_abzuege` | string | ja |  |  | Sozialversicherungsabzuege in EUR (§ 23a Abs. 3 SGB IV, anteilige Jahres-BBG je Versicherungszweig) |
| `netto` | string | ja |  |  | Netto-Sonderzahlung in EUR |
