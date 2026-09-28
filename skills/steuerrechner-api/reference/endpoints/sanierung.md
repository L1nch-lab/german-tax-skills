# Energetische Sanierung § 35c EStG (3-Jahres-Plan)

`POST /v1/sanierung`

Kategorie: Sanierung

Berechnet die Steuerermaessigung fuer energetische Massnahmen an eigengenutzten Wohngebaeuden nach § 35c EStG: 20 % der Kosten ueber 3 Jahre verteilt (7/7/6 %), max 40.000 EUR pro Objekt mit Jahres-Caps 14.000/14.000/12.000 EUR. Voraussetzungen: Gebaeude >= 10 Jahre alt, ausschliesslich eigene Wohnzwecke, kein Doppel- mit § 35a/§ 10f/BAFA/KfW. Programmlaufzeit 2020-2029.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `sanierungskosten` | number | ja |  |  | Gesamtkosten der energetischen Massnahmen in EUR |
| `gebaeude_alter_jahre` | integer |  | 30 |  | Gebaeude-Alter (Baubeginn massgeblich), Mindestalter 10 Jahre |
| `eigennutzung` | boolean |  | true |  | Ausschliesslich eigene Wohnzwecke? |
| `andere_foerderung` | boolean |  | false |  | BAFA-/KfW-/§ 10f-/§ 35a-Foerderung in Anspruch (Doppelfoerderverbot)? |

Beispiel:

```json
{
  "gebaeude_alter_jahre": 30,
  "sanierungskosten": 50000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `sanierungskosten` | string | ja |  |  |  |
| `gebaeude_alter_jahre` | integer | ja |  |  |  |
| `eigennutzung` | boolean | ja |  |  |  |
| `andere_foerderung` | boolean | ja |  |  |  |
| `berechtigt` | boolean | ja |  |  |  |
| `grund` | string | ja |  |  |  |
| `details_pruefung` | array<string> | ja |  |  |  |
| `grenzfall_hinweis` | string |  | "" |  | Bei genau 10 Jahren Gebaeudealter: Hinweis, dass der Tag des Baubeginns entscheidet (§ 35c Abs. 1 Satz 2 EStG). Leer, sofern nicht der Grenzfall. |
| `ermaessigung_jahr_1` | string | ja |  |  | 7 % vom Kosten, Cap 14.000 EUR |
| `ermaessigung_jahr_2` | string | ja |  |  | 7 % vom Kosten, Cap 14.000 EUR |
| `ermaessigung_jahr_3` | string | ja |  |  | 6 % vom Kosten, Cap 12.000 EUR |
| `total_ermaessigung` | string | ja |  |  |  |
| `ist_gekappt` | boolean | ja |  |  | True wenn 40.000-EUR-Objekt-Cap erreicht |
| `total_ungekappt` | string | ja |  |  |  |
| `optimale_sanierungssumme` | string | ja |  |  | 200.000 EUR = 40k / 20 % |
| `empfehlung` | string | ja |  |  |  |
| `max_gesamt` | string | ja |  |  | 40.000 EUR pro Objekt |
| `max_j1_j2` | string | ja |  |  | 14.000 EUR Jahres-Cap J1 + J2 |
| `max_j3` | string | ja |  |  | 12.000 EUR Jahres-Cap J3 |
| `prozent_gesamt` | string | ja |  |  |  |
| `prozent_j1` | string | ja |  |  |  |
| `prozent_j2` | string | ja |  |  |  |
| `prozent_j3` | string | ja |  |  |  |
| `min_gebaeude_alter` | integer | ja |  |  | 10 Jahre Mindestalter |
| `programm_bis_jahr` | integer | ja |  |  | Programmlaufzeit bis 2029 |
