# Vorfaelligkeitsentschaedigung (VFE) – BGH-Aktiv-Passiv-Methode

`POST /v1/vorfaelligkeitsentschaedigung`

Kategorie: Vorfaelligkeitsentschaedigung

Berechnet die Vorfaelligkeitsentschaedigung bei vorzeitiger Rueckzahlung eines Hypothekendarlehens nach BGH XI ZR 27/00 (Aktiv-Passiv-Methode). Beruecksichtigt §502 BGB-Cap fuer Verbraucherkredite (max 1 % bzw 0,5 % Restschuld), §489 BGB-Sonderkuendigungsrecht nach 10 J Volltransfer (OHNE VFE), Sondertilgungsrechte, ersparte Verwaltungs- und Risikokosten. Liefert Empfehlung zur Steuer-Absetzbarkeit (§9 EStG bei Vermietung).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `restschuld_eur` | number | ja |  |  | Aktuelle Restschuld vor Sondertilgung in EUR |
| `sollzins_prozent` | number |  | "3.5" |  | Vertraglich vereinbarter Sollzins (% p.a.) |
| `wiederanlagezins_prozent` | number |  | "2.6" |  | Wiederanlagezins der Bank (% p.a.) – Bundesbank-Pfandbrief |
| `restlaufzeit_monate` | integer |  | 60 |  | Verbleibende Zinsbindung in Monaten |
| `sondertilgung_prozent_p_a` | number |  | "5.0" |  | Vertraglich vereinbartes jaehrl. Sondertilgungsrecht (%) |
| `verwaltungskosten_eur_p_a` | number |  | "50" |  | Ersparte Verwaltungskosten der Bank (EUR p.a.) |
| `risikokosten_prozent_p_a` | number |  | "0.06" |  | Ersparte Risikokosten der Bank (% p.a. der Restschuld) |
| `ist_allgemein_verbraucherkredit` | boolean |  | false |  | True = Allgemein-Verbraucherdarlehen (nicht immobilienbesichert) -> §502 Abs. 3 BGB-Deckel greift. False (Standard) = Immobiliar-Verbraucherdarlehen oder Geschaeftskredit -> kein Deckel. |
| `ist_vermietetes_objekt` | boolean |  | false |  | True = VFE als Werbungskosten absetzbar |
| `monate_seit_volltransfer` | integer |  | 0 |  | Monate seit Volltransfer (ab 120 = §489 BGB-Sonderkuendigung) |

Beispiel:

```json
{
  "restschuld_eur": 250000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `restschuld_eur` | string | ja |  |  |  |
| `sollzins_prozent` | string | ja |  |  |  |
| `wiederanlagezins_prozent` | string | ja |  |  |  |
| `restlaufzeit_monate` | integer | ja |  |  |  |
| `sondertilgung_prozent_p_a` | string | ja |  |  |  |
| `verwaltungskosten_eur_p_a` | string | ja |  |  |  |
| `risikokosten_prozent_p_a` | string | ja |  |  |  |
| `ist_allgemein_verbraucherkredit` | boolean | ja |  |  |  |
| `ist_vermietetes_objekt` | boolean | ja |  |  |  |
| `monate_seit_volltransfer` | integer | ja |  |  |  |
| `sondertilgung_summe_eur` | string | ja |  |  |  |
| `restschuld_nach_sondertilgung_eur` | string | ja |  |  |  |
| `bemessungsgrundlage_eur` | string | ja |  |  | Durchschnittlicher Kapitalbestand ueber die anrechenbare Laufzeit |
| `anrechenbare_monate` | integer | ja |  |  | §489 Abs. 1 Nr. 2 BGB: ersatzfaehige Restlaufzeit (max. 120 + 6 Monate) |
| `zinserwartung_gekappt` | boolean | ja |  |  | True, wenn die Restlaufzeit die geschuetzte Zinserwartung uebersteigt |
| `zinsdifferenz_prozent` | string | ja |  |  |  |
| `barwertfaktor` | string | ja |  |  | Abzinsungsfaktor auf den Abloesezeitpunkt |
| `refinanzierungsschaden_eur` | string | ja |  |  |  |
| `ersparte_verwaltungskosten_eur` | string | ja |  |  |  |
| `ersparte_risikokosten_eur` | string | ja |  |  |  |
| `vfe_brutto_eur` | string | ja |  |  |  |
| `cap_eur` | string |  |  |  |  |
| `cap_zinsen_eur` | string |  |  |  | §502 Abs. 3 Nr. 2 BGB: Betrag der entfallenden Sollzinsen |
| `cap_greift` | boolean | ja |  |  |  |
| `vfe_final_eur` | string | ja |  |  |  |
| `steuerlich_absetzbar` | boolean | ja |  |  |  |
| `werbungskosten_eur` | string | ja |  |  |  |
| `sonderkuendigung_moeglich` | boolean | ja |  |  |  |
| `monate_bis_sonderkuendigung` | integer | ja |  |  |  |
| `empfehlung` | string | ja |  |  |  |
| `sonderkuendigung_nach_monate` | integer | ja |  |  | §489 BGB: 120 Monate |
| `sonderkuendigungs_frist_monate` | integer | ja |  |  | §489 BGB: 6 Monate |
| `cap_prozent_ueber_1j` | string | ja |  |  | §502 BGB Cap: 1 % Restschuld |
| `cap_prozent_unter_1j` | string | ja |  |  | §502 BGB Cap: 0,5 % Restschuld |
