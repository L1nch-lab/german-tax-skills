# Arbeitslosengeld-I-Rechner

`POST /v1/alg1`

Kategorie: ALG I

Berechnet ALG I nach SGB III: Bemessungsentgelt, pauschalierte Abzuege (§153 SGB III), Leistungsentgelt und Leistungssatz (60% ohne / 67% mit Kind). Ermittelt Bezugsdauer nach §147 SGB III (abhaengig von Alter und Versicherungsmonaten).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bruttogehalt_monat` | number | ja |  |  | Letztes monatliches Bruttogehalt in EUR |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) fuer den pauschalierten Lohnsteuerabzug im Leistungsentgelt (§ 153 SGB III) |
| `kinder` | boolean |  | false |  | Kindergeldberechtigt (67% statt 60% Leistungssatz) |
| `alter` | integer |  | 35 |  | Alter bei Entstehung des Anspruchs |
| `versicherungsmonate` | integer |  | 24 |  | Versicherungspflichtige Monate in den letzten 5 Jahren (min. 12) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland – relevant fuer Kirchensteuer und die Sachsen-Sonderregel beim PV-Beitrag im Leistungsentgelt |
| `kirchenmitglied` | boolean |  | false |  | Kirchensteuerpflichtig – fliesst in die pauschalierte Lohnsteuer-Berechnung des Leistungsentgelts ein |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |

Beispiel:

```json
{
  "bruttogehalt_monat": 4000,
  "bundesland": "Nordrhein-Westfalen",
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bemessungsentgelt_monat` | string | ja |  |  | Bemessungsentgelt monatlich |
| `bemessungsentgelt_tag` | string | ja |  |  | Bemessungsentgelt taeglich |
| `sv_pauschale_tag` | string | ja |  |  | SV-Pauschale 20% pro Tag |
| `lohnsteuer_tag` | string | ja |  |  | Pauschalierte Lohnsteuer pro Tag |
| `soli_tag` | string | ja |  |  | Solidaritaetszuschlag pro Tag |
| `leistungsentgelt_tag` | string | ja |  |  | Leistungsentgelt (Netto) pro Tag |
| `leistungssatz_prozent` | string | ja |  |  | Leistungssatz (60% oder 67%) |
| `alg1_tag` | string | ja |  |  | ALG I pro Tag in EUR |
| `alg1_monat` | string | ja |  |  | ALG I pro Monat (30 Tage) in EUR |
| `bezugsdauer_monate` | integer | ja |  |  | Bezugsdauer in Monaten (§147 SGB III) |
| `gesamtanspruch` | string | ja |  |  | Gesamtanspruch (ALG I x Bezugsmonate) in EUR |
