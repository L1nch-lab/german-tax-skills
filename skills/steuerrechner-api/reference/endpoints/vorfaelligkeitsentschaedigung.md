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
| `restschuld_eur` | string | ja |  |  | Aktuelle Restschuld vor Sondertilgung in EUR aus der Anfrage, negativ wird zu 0. |
| `sollzins_prozent` | string | ja |  |  | Vertraglicher Sollzins in Prozent p. a. (3.5 = 3,5 %), Echo der Anfrage. |
| `wiederanlagezins_prozent` | string | ja |  |  | Wiederanlagezins der Bank in Prozent p. a., Echo der Anfrage. Bestimmt Zinsdifferenz und Abzinsung. |
| `restlaufzeit_monate` | integer | ja |  |  | Verbleibende Zinsbindung in Monaten, Echo der Anfrage. Bei 0 keine VFE. |
| `sondertilgung_prozent_p_a` | string | ja |  |  | Vertragliches Sondertilgungsrecht in Prozent der Restschuld pro Jahr, Echo der Anfrage. Mindert die Bemessungsgrundlage. |
| `verwaltungskosten_eur_p_a` | string | ja |  |  | Ersparte Verwaltungskosten der Bank in EUR pro Jahr, Echo der Anfrage (Default 50). |
| `risikokosten_prozent_p_a` | string | ja |  |  | Ersparte Risikokosten der Bank in Prozent p. a. der Bemessungsgrundlage, Echo der Anfrage (Default 0.06). |
| `ist_allgemein_verbraucherkredit` | boolean | ja |  |  | Echo: true = Allgemein-Verbraucherdarlehen, dann gilt der Deckel nach § 502 Abs. 3 BGB. false (Default) = Immobiliar-Verbraucherdarlehen oder Geschäftskredit ohne Deckel. |
| `ist_vermietetes_objekt` | boolean | ja |  |  | Echo: true = vermietetes Objekt; dann wird die VFE als Werbungskosten ausgewiesen (anlassabhängig, siehe empfehlung). |
| `monate_seit_volltransfer` | integer | ja |  |  | Monate seit vollständiger Auszahlung, Echo der Anfrage. Ab 120 Sonderkündigung ohne VFE; begrenzt außerdem die anrechenbare Laufzeit auf 126 minus diesen Wert. |
| `sondertilgung_summe_eur` | string | ja |  |  | Summe der möglichen Sondertilgungen über die anrechenbare Laufzeit in EUR: Restschuld × Satz × anrechenbare Jahre, höchstens die Restschuld. 0 ohne VFE-Berechnung. |
| `restschuld_nach_sondertilgung_eur` | string | ja |  |  | Restschuld nach allen möglichen Sondertilgungen in EUR (nicht negativ). Mit restschuld_eur gemittelt zur Bemessungsgrundlage. 0 ohne VFE-Berechnung. |
| `bemessungsgrundlage_eur` | string | ja |  |  | Durchschnittlicher Kapitalbestand ueber die anrechenbare Laufzeit |
| `anrechenbare_monate` | integer | ja |  |  | §489 Abs. 1 Nr. 2 BGB: ersatzfaehige Restlaufzeit (max. 120 + 6 Monate) |
| `zinserwartung_gekappt` | boolean | ja |  |  | True, wenn die Restlaufzeit die geschuetzte Zinserwartung uebersteigt |
| `zinsdifferenz_prozent` | string | ja |  |  | Sollzins minus Wiederanlagezins in Prozentpunkten, nicht negativ. |
| `barwertfaktor` | string | ja |  |  | Abzinsungsfaktor auf den Abloesezeitpunkt |
| `refinanzierungsschaden_eur` | string | ja |  |  | Zinsverschlechterungsschaden in EUR: monatliche Zinsdifferenz auf die Bemessungsgrundlage × Barwertfaktor über die anrechenbaren Monate. |
| `ersparte_verwaltungskosten_eur` | string | ja |  |  | Barwert der ersparten Verwaltungskosten in EUR über die anrechenbare Laufzeit, wird vom Schaden abgezogen. |
| `ersparte_risikokosten_eur` | string | ja |  |  | Barwert der ersparten Risikokosten in EUR über die anrechenbare Laufzeit, wird vom Schaden abgezogen. |
| `vfe_brutto_eur` | string | ja |  |  | VFE vor Deckel in EUR: Refinanzierungsschaden minus ersparte Verwaltungs- und Risikokosten, nicht negativ. |
| `cap_eur` | string |  |  |  | Nur Allgemein-Verbraucherdarlehen: Prozentdeckel in EUR, 1 % der Restschuld (0,5 % bei Restlaufzeit bis 12 Monate). Sonst null. |
| `cap_zinsen_eur` | string |  |  |  | §502 Abs. 3 Nr. 2 BGB: Betrag der entfallenden Sollzinsen |
| `cap_greift` | boolean | ja |  |  | True, wenn vfe_brutto_eur über dem kleineren der beiden Deckel (cap_eur, cap_zinsen_eur) liegt und deshalb gekürzt wurde. Nur bei Allgemein-Verbraucherdarlehen möglich. |
| `vfe_final_eur` | string | ja |  |  | Zu zahlende Vorfälligkeitsentschädigung in EUR nach Deckel. 0 bei Sonderkündigungsrecht, abgelaufener Zinsbindung oder Restschuld 0. |
| `steuerlich_absetzbar` | boolean | ja |  |  | Entspricht ist_vermietetes_objekt; die Abzugsfähigkeit hängt laut empfehlung zusätzlich am Anlass der Ablösung, das prüft der Code nicht. |
| `werbungskosten_eur` | string | ja |  |  | vfe_final_eur, wenn steuerlich_absetzbar, sonst 0. Betrag in EUR, keine Steuerersparnis. |
| `sonderkuendigung_moeglich` | boolean | ja |  |  | True, wenn monate_seit_volltransfer mindestens 120 beträgt; dann ist keine VFE fällig und vfe_final_eur 0. |
| `monate_bis_sonderkuendigung` | integer | ja |  |  | Monate bis zum Erreichen der 120-Monats-Grenze: 120 − monate_seit_volltransfer, mindestens 0. Ohne die 6-Monats-Kündigungsfrist. |
| `empfehlung` | string | ja |  |  | Zusammengesetzter Text: VFE in EUR und Prozent der Restschuld, ggf. Deckel- und Sonderkündigungshinweis, steuerliche Einordnung nach Nutzung und Prüfhinweis zur Bankberechnung. |
| `sonderkuendigung_nach_monate` | integer | ja |  |  | §489 BGB: 120 Monate |
| `sonderkuendigungs_frist_monate` | integer | ja |  |  | §489 BGB: 6 Monate |
| `cap_prozent_ueber_1j` | string | ja |  |  | §502 BGB Cap: 1 % Restschuld |
| `cap_prozent_unter_1j` | string | ja |  |  | §502 BGB Cap: 0,5 % Restschuld |
