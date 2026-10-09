# Kleinunternehmer-Grenze-Rechner (§ 19 UStG, JStG 2024)

`POST /v1/kleinunternehmer`

Kategorie: Kleinunternehmer

Prueft Kleinunternehmer-Status und liefert Jahres-Hochrechnung. Seit JStG 2024: Vorjahresgrenze 25.000 EUR, laufende Grenze 100.000 EUR. Ampel-Status: gruen (alles ok), gelb (Hochrechnung >= 80.000 EUR), rot (Vorjahr oder laufendes Jahr ueberschritten). Liefert Warn-Monat ab dem die 100k-Grenze voraussichtlich erreicht wird.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bisheriger_umsatz` | number | ja |  |  | Umsatz im laufenden Jahr bis einschl. aktueller_monat in EUR |
| `aktueller_monat` | integer | ja |  |  | Aktueller Monat (1=Januar, 12=Dezember) |
| `vorjahresumsatz` | number | ja |  |  | Gesamtumsatz des Vorjahres in EUR |

Beispiel:

```json
{
  "aktueller_monat": 6,
  "bisheriger_umsatz": 40000,
  "vorjahresumsatz": 20000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bisheriger_umsatz` | string | ja |  |  | Echo des Umsatzes im laufenden Jahr bis einschließlich aktueller_monat in EUR. Wird gegen die 100.000-EUR-Grenze geprüft. |
| `aktueller_monat` | integer | ja |  |  | Echo des aktuellen Monats (1 = Januar bis 12 = Dezember), Divisor für durchschnitt_monat. |
| `vorjahresumsatz` | string | ja |  |  | Echo des Gesamtumsatzes im Vorjahr in EUR. Wird gegen die 25.000-EUR-Grenze geprüft. |
| `durchschnitt_monat` | string | ja |  |  | Durchschnittlicher Monatsumsatz in EUR = bisheriger_umsatz / aktueller_monat. Grundlage von hochrechnung und warnmonat. |
| `hochrechnung` | string | ja |  |  | Jahres-Hochrechnung aus bisherigem Umsatz |
| `restpuffer_laufend` | string | ja |  |  | Verbleibend bis 100.000 EUR-Grenze |
| `restpuffer_vorjahr` | string | ja |  |  | Verbleibend bis 25.000 EUR-Grenze |
| `ampel` | string | ja |  |  | 'gruen' / 'gelb' / 'rot' |
| `vorjahr_status` | string | ja |  |  | 'ok' / 'ueberschritten' |
| `laufend_status` | string | ja |  |  | 'ok' / 'warnung' / 'ueberschritten' |
| `warnmonat` | integer |  |  |  | Monat (1-12) ab dem 100k erreicht wird |
| `warnmonat_name` | string |  |  |  | Deutscher Monatsname |
| `verbleibende_monate` | string |  |  |  | Bis Grenze-Erreichen |
| `empfehlung` | string | ja |  |  | Deutscher Hinweistext in Du-Form zum Status (Vorjahr überschritten, laufendes Jahr überschritten, Prognose-Warnung oder alles in Ordnung). Nicht maschinenlesbar. |
