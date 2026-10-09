# Wohngeld-Rechner nach WoGG (Wohngeld-Plus 2023+)

`POST /v1/wohngeld`

Kategorie: Wohngeld

Berechnet den Wohngeld-Anspruch nach § 19 WoGG mit der Formel W = 1,15 * (M - (a + b*M + c*Y) * Y). Beruecksichtigt Mietstufe (1-7), Haushaltsgroesse (1-12), Heizkostenentlastung (§ 12 Abs. 6) und Klimakomponente (§ 12 Abs. 7, hebt die Mietobergrenze nach § 11 Abs. 1 Nr. 1), Werbungskosten-Pauschbetrag (§ 9a EStG), Pauschalabzug 30 % (§ 16) und ggf. den Schwerbehinderten-Freibetrag (§ 17). Mindestwerte fuer M und Y sowie Rundung nach Anlage 3. Liefert auch Vermoegensgrenze und Anspruchspruefung.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `haushaltsgroesse` | integer | ja |  |  | Anzahl Personen im Haushalt (1-12) |
| `mietstufe` | enum | ja |  | 1, 2, 3, 4, 5, 6, 7 | Mietstufe der Gemeinde (1-7) |
| `bruttoeinkommen` | number | ja |  |  | Monatliches Brutto-Haushaltseinkommen in EUR |
| `kaltmiete` | number | ja |  |  | Monatliche Kaltmiete in EUR |
| `wohnflaeche` | number | ja |  |  | Wohnflaeche in Quadratmetern |
| `schwerbehindert` | boolean |  | false |  | Schwerbehinderung im Haushalt? |

Beispiel:

```json
{
  "bruttoeinkommen": 2200,
  "haushaltsgroesse": 2,
  "kaltmiete": 700,
  "mietstufe": 4,
  "wohnflaeche": 65
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `wohngeld_monat` | string | ja |  |  | Wohngeld pro Monat in EUR |
| `wohngeld_jahr` | string | ja |  |  | Wohngeld pro Jahr in EUR (wohngeld_monat × 12); 0, wenn kein Anspruch besteht. |
| `anrechenbare_miete` | string | ja |  |  | Miete, die in die Wohngeldformel eingeht, in EUR pro Monat: Kaltmiete gekappt auf miet_obergrenze plus heizkosten_komponente. Wert vor Anwendung des Mindestwerts; der tatsächlich verwendete Wert steht in formel_details.M. |
| `anrechenbares_einkommen` | string | ja |  |  | Monatliches Einkommen für die Formel in EUR: Bruttoeinkommen minus Werbungskosten-Pauschbetrag, davon 30 % Pauschalabzug, bei schwerbehindert=true zusätzlich minus Freibetrag, nie unter 0. Wert vor Mindestwert; der verwendete Wert steht in formel_details.Y. |
| `max_miete` | string | ja |  |  | Hoechstbetrag nach § 12 Abs. 1 WoGG (Anlage 1) |
| `heizkosten_komponente` | string | ja |  |  | Gesamtbetrag zur Entlastung bei den Heizkosten (§ 12 Abs. 6 WoGG) |
| `klima_komponente` | string | ja |  |  | Klimakomponente (§ 12 Abs. 7 WoGG) – Zuschlag zum Hoechstbetrag |
| `miet_obergrenze` | string | ja |  |  | Obergrenze der anzusetzenden Miete (§ 11 Abs. 1 Nr. 1 WoGG): Hoechstbetrag + Klimakomponente |
| `angesetzte_miete` | string | ja |  |  | Kaltmiete, gekappt auf die Mietobergrenze (ohne Heizkostenentlastung) |
| `werbungskosten_pauschbetrag` | string | ja |  |  | Angesetzter Werbungskosten-Pauschbetrag pro Monat (§ 9a EStG) |
| `heiz_klima_zuschlag` | string | ja |  |  | Summe aus heizkosten_komponente und klima_komponente in EUR pro Monat. Nur Anzeige: die Klimakomponente hebt die Mietobergrenze, nur die Heizkostenkomponente wird auf die gekappte Miete addiert. |
| `miete_mit_zuschlag` | string | ja |  |  | Identisch mit anrechenbare_miete (gekappte Kaltmiete plus Heizkostenkomponente) in EUR pro Monat. |
| `kaltmiete` | string | ja |  |  | Echo der eingegebenen monatlichen Kaltmiete in EUR, ungekappt. |
| `mietstufe` | integer | ja |  |  | Echo der Mietstufe der Gemeinde (1 bis 7); bestimmt den Höchstbetrag der Miete. |
| `mietstufe_label` | string | ja |  |  | Mietstufe als römische Ziffer, z. B. "IV"; Stufe 1 als "I (niedrig)", Stufe 7 als "VII (hoch)". |
| `haushaltsgroesse` | integer | ja |  |  | Echo der Anzahl Personen im Haushalt (1 bis 12); bestimmt Koeffizienten, Höchstbetrag, Komponenten, Mindestwerte und Vermögensgrenze. |
| `bruttoeinkommen` | string | ja |  |  | Echo des monatlichen Brutto-Haushaltseinkommens in EUR; Ausgangswert für anrechenbares_einkommen. |
| `wohnflaeche` | string | ja |  |  | Echo der Wohnfläche in Quadratmetern; geht in keine Berechnung ein. |
| `schwerbehindert` | boolean | ja |  |  | Echo der Angabe, ob im Haushalt eine Schwerbehinderung vorliegt. Bei true wird vom anrechenbaren Einkommen der Schwerbehinderten-Freibetrag von 150 EUR pro Monat abgezogen. |
| `vermoegensgrenze` | string | ja |  |  | Vermögensgrenze des Haushalts in EUR: 60.000 für die erste und 30.000 für jede weitere Person. Nur Information, die API fragt kein Vermögen ab und has_anspruch prüft sie nicht. |
| `has_anspruch` | boolean | ja |  |  | True, wenn die Wohngeldformel mindestens den Mindestbetrag von 10 EUR pro Monat ergibt. Das Vermögen wird dabei nicht geprüft. |
| `grund_kein_anspruch` | string |  |  |  | Begründung als Text, wenn kein Anspruch besteht (Formelergebnis 0 oder unter 10 EUR); null bei Anspruch. |
| `formel_details` | WohngeldFormelDetails | ja |  |  | Rechenweg der Wohngeldformel W = 1,15 × (M − (a + b·M + c·Y) · Y) mit den tatsächlich eingesetzten Werten. |
