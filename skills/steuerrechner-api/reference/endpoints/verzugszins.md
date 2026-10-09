# Verzugszinsen §288 BGB pro Halbjahres-Fenster

`POST /v1/verzugszins`

Kategorie: Verzugszinsen

Berechnet Verzugszinsen auf eine ueberfaellige Forderung. Verzugsbeginn ist der Tag NACH Faelligkeit (§286 Abs. 1 BGB), Endpunkt das Zahlungsdatum (zaehlt MIT). actual/365. Wechselt der Basiszinssatz §247 BGB innerhalb des Verzugszeitraums (halbjaehrlich 1.1./1.7.), wird pro Halbjahres-Fenster gerechnet – keine Mischzinsen. Aufschlag: +5 Pkt (b2c §288 Abs. 1 BGB) oder +9 Pkt (b2b §288 Abs. 2 BGB). Optional 40-EUR-Schadenersatzpauschale §288 Abs. 5 BGB (B2B-only, separat ausgewiesen, NICHT in Summe enthalten).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `forderung_eur` | number | ja |  |  | Hauptforderung in EUR (mind. 0,01) |
| `faelligkeit` | string | ja |  |  | Faelligkeitstag – Tag selbst zaehlt NICHT als Verzugstag (§286 Abs. 1 BGB) |
| `zahlungsdatum` | string |  |  |  | Tag der Zahlung (zaehlt MIT). Default: heute. |
| `geschaeftsverkehr` | enum |  | "b2c" | b2c, b2b | b2c = Verbraucher (Aufschlag +5 Pkt §288 Abs. 1 BGB), b2b = Geschaeftsverkehr (+9 Pkt §288 Abs. 2 BGB) |
| `pauschale_anwenden` | boolean |  | false |  | Wenn True und b2b: weist die 40-EUR-Schadenersatzpauschale §288 Abs. 5 BGB separat aus. Bei b2c immer ohne Wirkung (Pauschale gilt nur fuer B2B). |

Beispiel:

```json
{
  "faelligkeit": "2025-03-15",
  "forderung_eur": "1500",
  "geschaeftsverkehr": "b2c",
  "zahlungsdatum": "2025-09-30"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `forderung_eur` | string | ja |  |  | Hauptforderung in EUR |
| `faelligkeit` | string | ja |  |  | Fälligkeitsdatum der Forderung (ISO-Datum) aus der Anfrage. Der Tag selbst zählt nicht als Verzugstag. |
| `zahlungsdatum` | string | ja |  |  | Zahlungsdatum (ISO-Datum); zählt als letzter Verzugstag mit. Fehlt es in der Anfrage, wird das heutige Datum verwendet. |
| `geschaeftsverkehr` | enum | ja |  | b2c, b2b | "b2c" (Aufschlag 5 Prozentpunkte) oder "b2b" (9 Prozentpunkte). Bei b2b ist zusätzlich die 40-EUR-Pauschale möglich. |
| `aufschlag_prozent` | string | ja |  |  | +5 (b2c) oder +9 (b2b) Prozentpunkte |
| `verzugsbeginn` | string | ja |  |  | Tag NACH Faelligkeit (§286 Abs. 1 BGB) |
| `verzugstage_gesamt` | integer | ja |  |  | Tage von verzugsbeginn bis zahlungsdatum (inkl.) |
| `posten` | array<VerzugszinsPostenModel> | ja |  |  | Pro Halbjahres-Fenster ein Posten – keine Mischzinsen |
| `verzugszinsen_summe_eur` | string | ja |  |  | Summe aller Posten-Zinsen in EUR (auf 2 Nachkommastellen gerundet) |
| `pauschale_288_abs_5_eur` | string |  |  |  | 40-EUR-Pauschale §288 Abs. 5 BGB – nur fuer b2b und nur wenn pauschale_anwenden=True. Wird NICHT in verzugszinsen_summe_eur addiert. |
| `rechtsgrundlage` | string | ja |  |  | Fester Text je Geschäftsverkehr: § 288 Abs. 1 BGB bei b2c, § 288 Abs. 2 BGB bei b2b, jeweils mit Höhe des Aufschlags. |
