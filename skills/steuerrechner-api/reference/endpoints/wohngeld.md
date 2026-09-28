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
| `wohngeld_jahr` | string | ja |  |  |  |
| `anrechenbare_miete` | string | ja |  |  |  |
| `anrechenbares_einkommen` | string | ja |  |  |  |
| `max_miete` | string | ja |  |  | Hoechstbetrag nach § 12 Abs. 1 WoGG (Anlage 1) |
| `heizkosten_komponente` | string | ja |  |  | Gesamtbetrag zur Entlastung bei den Heizkosten (§ 12 Abs. 6 WoGG) |
| `klima_komponente` | string | ja |  |  | Klimakomponente (§ 12 Abs. 7 WoGG) – Zuschlag zum Hoechstbetrag |
| `miet_obergrenze` | string | ja |  |  | Obergrenze der anzusetzenden Miete (§ 11 Abs. 1 Nr. 1 WoGG): Hoechstbetrag + Klimakomponente |
| `angesetzte_miete` | string | ja |  |  | Kaltmiete, gekappt auf die Mietobergrenze (ohne Heizkostenentlastung) |
| `werbungskosten_pauschbetrag` | string | ja |  |  | Angesetzter Werbungskosten-Pauschbetrag pro Monat (§ 9a EStG) |
| `heiz_klima_zuschlag` | string | ja |  |  |  |
| `miete_mit_zuschlag` | string | ja |  |  |  |
| `kaltmiete` | string | ja |  |  |  |
| `mietstufe` | integer | ja |  |  |  |
| `mietstufe_label` | string | ja |  |  |  |
| `haushaltsgroesse` | integer | ja |  |  |  |
| `bruttoeinkommen` | string | ja |  |  |  |
| `wohnflaeche` | string | ja |  |  |  |
| `schwerbehindert` | boolean | ja |  |  |  |
| `vermoegensgrenze` | string | ja |  |  |  |
| `has_anspruch` | boolean | ja |  |  |  |
| `grund_kein_anspruch` | string |  |  |  |  |
| `formel_details` | WohngeldFormelDetails | ja |  |  |  |
