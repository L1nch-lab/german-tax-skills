# Verpflegungsmehraufwand-Rechner (§ 9 Abs. 4a EStG, Inland)

`POST /v1/verpflegungsmehraufwand`

Kategorie: Verpflegungsmehraufwand

Berechnet die als Werbungskosten abziehbaren Verpflegungspauschalen fuer Dienstreisen im Inland: 28 EUR je 24h-Abwesenheitstag, je 14 EUR fuer An-/Abreisetage mit Uebernachtung und Eintages-Reisen ueber 8 Stunden. Vom Arbeitgeber gestellte Mahlzeiten kuerzen die Pauschalen (20/40/40 % der 24h-Pauschale = 5,60/11,20/11,20 EUR), gedeckelt auf die Summe der Pauschalen. Steuerfreie AG-Erstattungen mindern den abzugsfaehigen Betrag; bis zum Doppelten der Pauschalen ist Pauschalversteuerung mit 25 % moeglich (§ 40 Abs. 2 S. 1 Nr. 4 EStG).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `volle_tage` | integer | ja |  |  | Kalendertage mit 24h-Abwesenheit (volle Reisetage) |
| `an_abreise_tage` | integer |  | 0 |  | An-/Abreisetage mit Uebernachtung (je 14 EUR) |
| `tage_ueber_8h` | integer |  | 0 |  | Eintages-Reisen mit mehr als 8 Stunden Abwesenheit (je 14 EUR) |
| `fruehstuecke` | integer |  | 0 |  | Anzahl vom Arbeitgeber gestellter Fruehstuecke (Kuerzung je 5,60 EUR) |
| `mittagessen` | integer |  | 0 |  | Anzahl gestellter Mittagessen (Kuerzung je 11,20 EUR) |
| `abendessen` | integer |  | 0 |  | Anzahl gestellter Abendessen (Kuerzung je 11,20 EUR) |
| `erstattung` | number |  | "0" |  | Steuerfreie Arbeitgeber-Erstattung fuer Verpflegung in EUR |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `pauschale_voll` | string | ja |  |  | 24h-Pauschale (28 EUR) |
| `pauschale_teil` | string | ja |  |  | An-/Abreise- bzw. >8h-Pauschale (14 EUR) |
| `summe_pauschalen` | string | ja |  |  | Summe aller Tagespauschalen in EUR |
| `kuerzung_fruehstueck` | string | ja |  |  | Kuerzung gestellte Fruehstuecke (je 5,60) |
| `kuerzung_mittag` | string | ja |  |  | Kuerzung gestellte Mittagessen (je 11,20) |
| `kuerzung_abend` | string | ja |  |  | Kuerzung gestellte Abendessen (je 11,20) |
| `kuerzung_gesamt` | string | ja |  |  | Gesamt-Kuerzung, gedeckelt auf die Pauschalen |
| `kuerzung_gekappt` | boolean | ja |  |  | True wenn die Kuerzung die Pauschalen ueberstieg |
| `werbungskosten` | string | ja |  |  | Pauschalen minus Kuerzung in EUR |
| `abzugsfaehig` | string | ja |  |  | Werbungskosten minus steuerfreie AG-Erstattung |
| `erstattung_uebersteigt` | boolean | ja |  |  | True wenn die AG-Erstattung die Werbungskosten uebersteigt |
| `pauschalversteuerung_max` | string | ja |  |  | AG darf bis zum Doppelten der Pauschalen mit 25 % pauschal versteuern |
