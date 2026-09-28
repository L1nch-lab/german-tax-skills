# Urlaubsanspruchsrechner (§§ 3-5 BUrlG)

`POST /v1/urlaubsanspruch`

Kategorie: Urlaubsanspruch

Berechnet den Urlaubsanspruch in Tagen bei abweichender Arbeitstage-Woche (Teilzeit-Umrechnung: vereinbarter 5-Tage-Urlaub × eigene Tage / 5) und bei unterjaehrigem Ein-/Austritt (Zwoelftelung nach § 5 Abs. 1 BUrlG, 1/12 je vollem Beschaeftigungsmonat). Bruchteile ab einem halben Tag werden nach § 5 Abs. 2 BUrlG aufgerundet. Das gesetzliche Minimum (§ 3 BUrlG: 24 Werktage auf 6-Tage-Basis) wird nie unterschritten.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `arbeitstage_woche` | integer | ja |  |  | Arbeitstage pro Woche (1-6) |
| `jahresurlaub_vollzeit` | number | ja |  |  | Vereinbarter Jahresurlaub in Tagen auf 5-Tage-Wochen-Basis (gesetzliches Minimum bei 5-Tage-Woche: 20 Tage) |
| `beschaeftigungsmonate` | integer |  | 12 |  | Volle Beschaeftigungsmonate im Kalenderjahr; unter 12 greift die Zwoelftelung nach § 5 Abs. 1 BUrlG |

Beispiel:

```json
{
  "arbeitstage_woche": 4,
  "beschaeftigungsmonate": 12,
  "jahresurlaub_vollzeit": 30
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `arbeitstage_woche` | integer | ja |  |  |  |
| `jahresurlaub_vollzeit` | number | ja |  |  | Eingabe auf 5-Tage-Basis, gerundet 1 NK |
| `beschaeftigungsmonate` | integer | ja |  |  |  |
| `gezwoelftelt` | boolean | ja |  |  | True wenn § 5 Abs. 1 BUrlG (Zwoelftelung) angewendet |
| `urlaub_voll` | number | ja |  |  | Vertraglicher Urlaub umgerechnet auf die eigene Woche |
| `gesetzliches_minimum` | number | ja |  |  | Gesetzliches Minimum fuer diese Arbeitstage-Woche (§ 3 BUrlG, ungerundet) |
| `gesetzliches_minimum_gerundet` | number | ja |  |  | Gesetzliches Minimum nach § 5 Abs. 2 BUrlG gerundet |
| `anspruch_roh` | number | ja |  |  | Anspruch vor Rundung (2 NK) |
| `urlaubsanspruch` | number | ja |  |  | Finaler Urlaubsanspruch in Tagen (gerundet, nie unter dem Minimum) |
| `ueber_minimum` | boolean | ja |  |  | True wenn der Anspruch ueber dem Minimum liegt |
