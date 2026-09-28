# Steuerklassen-Vergleich

`POST /v1/steuerklassen`

Kategorie: Steuerklassen

Vergleicht Steuerklassenkombinationen III/V vs. IV/IV fuer Ehepaare nach §38b EStG. Berechnet monatliches Netto fuer beide Partner in jeder Variante, inklusive SV-Beitraege und Kirchensteuer. Liefert Jahresvergleich und Empfehlung.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_partner_1` | number | ja |  |  | Monatliches Bruttogehalt Partner 1 in EUR |
| `brutto_partner_2` | number | ja |  |  | Monatliches Bruttogehalt Partner 2 in EUR |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (relevant fuer Kirchensteuer + PV-Sachsen) |
| `kinder` | integer |  | 0 |  | Anzahl Kinder (relevant fuer PV-Kinderlos-Zuschlag) |
| `kirchensteuer` | boolean |  | false |  | True wenn Kirchensteuer abzufuehren ist |

Beispiel:

```json
{
  "brutto_partner_1": 5000,
  "brutto_partner_2": 3000,
  "bundesland": "Nordrhein-Westfalen"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `variante_3_5` | SteuerklassenVarianteData | ja |  |  | SK III/V Kombination |
| `variante_4_4` | SteuerklassenVarianteData | ja |  |  | SK IV/IV Kombination |
| `differenz_monat` | string | ja |  |  | Netto-Differenz pro Monat in EUR (positiv = III/V besser) |
| `differenz_jahr` | string | ja |  |  | Netto-Differenz pro Jahr in EUR |
| `empfehlung` | string | ja |  |  | Empfehlungstext |
| `warnungen` | array<string> | ja |  |  | Warnhinweise |
