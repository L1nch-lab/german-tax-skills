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
| `sanierungskosten` | string | ja |  |  | Kosten der energetischen Maßnahmen in EUR aus der Anfrage, auf 2 Nachkommastellen gerundet. |
| `gebaeude_alter_jahre` | integer | ja |  |  | Gebäudealter in ganzen Jahren aus der Anfrage. Unter 10 nicht berechtigt; bei genau 10 berechtigt mit Grenzfall-Hinweis. |
| `eigennutzung` | boolean | ja |  |  | Echo: true, wenn das Gebäude ausschließlich selbst bewohnt wird. Bei false nicht berechtigt. |
| `andere_foerderung` | boolean | ja |  |  | Echo des Flags für andere Förderung (BAFA, KfW, § 10f, § 35a); bei true nicht berechtigt. Auch im Ausschlussfall und bei sanierungskosten 0 die Eingabe. |
| `berechtigt` | boolean | ja |  |  | True, wenn Mindestalter, Eigennutzung und keine andere Förderung erfüllt sind und sanierungskosten größer 0 ist. |
| `grund` | string | ja |  |  | Text mit allen nicht erfüllten Voraussetzungen, "Alle Voraussetzungen erfuellt." oder bei sanierungskosten 0 eine Eingabeaufforderung. |
| `details_pruefung` | array<string> | ja |  |  | Liste der einzelnen Ausschlussgründe als Text. Leer, wenn berechtigt. |
| `grenzfall_hinweis` | string |  | "" |  | Bei genau 10 Jahren Gebaeudealter: Hinweis, dass der Tag des Baubeginns entscheidet (§ 35c Abs. 1 Satz 2 EStG). Leer, sofern nicht der Grenzfall. |
| `ermaessigung_jahr_1` | string | ja |  |  | 7 % vom Kosten, Cap 14.000 EUR |
| `ermaessigung_jahr_2` | string | ja |  |  | 7 % vom Kosten, Cap 14.000 EUR |
| `ermaessigung_jahr_3` | string | ja |  |  | 6 % vom Kosten, Cap 12.000 EUR |
| `total_ermaessigung` | string | ja |  |  | Summe der Steuerermäßigung über 3 Jahre in EUR nach den Jahres-Caps (höchstens 40.000). 0, wenn nicht berechtigt. Keine Kürzung auf die tatsächliche Steuerschuld modelliert. |
| `ist_gekappt` | boolean | ja |  |  | True wenn 40.000-EUR-Objekt-Cap erreicht |
| `total_ungekappt` | string | ja |  |  | Ermäßigung ohne Caps in EUR = 20 % der sanierungskosten. Vergleichswert für ist_gekappt; 0, wenn nicht berechtigt. |
| `optimale_sanierungssumme` | string | ja |  |  | 200.000 EUR = 40k / 20 % |
| `empfehlung` | string | ja |  |  | Text: bei Kappung Hinweis auf die 200.000-EUR-Grenze, bei Kosten unter 5.000 EUR Verweis auf § 35a, sonst Jahresaufteilung; bei fehlender Berechtigung eine Alternative je Ausschlussgrund. |
| `max_gesamt` | string | ja |  |  | 40.000 EUR pro Objekt |
| `max_j1_j2` | string | ja |  |  | 14.000 EUR Jahres-Cap J1 + J2 |
| `max_j3` | string | ja |  |  | 12.000 EUR Jahres-Cap J3 |
| `prozent_gesamt` | string | ja |  |  | Konstante: Gesamtsatz der Ermäßigung in Prozent der Kosten (20). |
| `prozent_j1` | string | ja |  |  | Konstante: Ermäßigungssatz im 1. Jahr in Prozent der Kosten (7). |
| `prozent_j2` | string | ja |  |  | Konstante: Ermäßigungssatz im 2. Jahr in Prozent der Kosten (7). |
| `prozent_j3` | string | ja |  |  | Konstante: Ermäßigungssatz im 3. Jahr in Prozent der Kosten (6). |
| `min_gebaeude_alter` | integer | ja |  |  | 10 Jahre Mindestalter |
| `programm_bis_jahr` | integer | ja |  |  | Programmlaufzeit bis 2029 |
