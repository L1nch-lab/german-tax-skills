# Frühstart-Rente – Kinderdepot (Referentenentwurf FrühStRG)

`POST /v1/fruehstartrente`

Kategorie: Fruehstartrente

Berechnet die Kapitalprojektion der Frühstartrente (staatlich 10 EUR/Monat, § 2 Abs. 1 FrühStRG-E) und optional den Aufbau ueber 18 hinaus mit Eigen-beitraegen (Eltern bis 18, Kind ab 18) bis Renteneintritt. Grundlage ist der BMF-Referentenentwurf vom 21.07.2026 – Modellrechnung, kein geltendes Recht. Der Anspruch haengt am Geburtsjahrgang: erster berechtigter Jahrgang ist 2020, danach kommt jaehrlich der Jahrgang der Sechsjaehrigen dazu (§ 30 Abs. 1 S. 2). Fruehere Jahrgaenge erhalten 0 EUR, koennen aber einen Vertrag schliessen (§ 3 Abs. 4). Einzahlungen daneben sind auf 6.840 EUR je Kalenderjahr begrenzt (§ 3 Abs. 3) und werden sonst gekappt. Liefert Kapitalstock bei 18 und bei Renteneintritt, monatliche Auszahlung fuer 25-J-Annuitaet, Vorteil mit Eltern-Beitrag vs nur Staat, Wachstumsfaktor.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `geburtsjahr` | integer |  |  |  | Geburtsjahr des Kindes. Anspruch auf die staatliche Zahlung besteht erst ab Jahrgang 2020 (§ 30 Abs. 1 S. 2 FrühStRG-E); frühere Jahrgänge können einen Vertrag schließen, erhalten aber 0 EUR. |
| `alter_kind` | integer |  |  |  | Abgelöst durch geburtsjahr. Wird nur ausgewertet, wenn geburtsjahr fehlt, und dann als Bezugsjahr minus Alter interpretiert. |
| `eigenbeitrag_eltern_monat` | number |  | "0" |  | Eltern-Eigenbeitrag pro Monat bis 18. § 3 Abs. 3 FrühStRG-E deckelt Einzahlungen neben der Förderung auf 6.840 EUR im Kalenderjahr (570 EUR/Monat); höhere Werte werden gekappt und im Feld eigenbeitrag_gekappt ausgewiesen. |
| `eigenbeitrag_ab_18_monat` | number |  | "0" |  | Kind-Eigenbeitrag ab 18 bis Renteneintritt. Ebenfalls auf 570 EUR/Monat gekappt (§ 3 Abs. 3 FrühStRG-E). |
| `renteneintritt` | integer |  | 67 |  | Renteneintrittsalter |
| `rendite_prozent` | number |  | "6.0" |  | Jaehrl. Renditeannahme in % |

Beispiel:

```json
{
  "geburtsjahr": 2020
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `geburtsjahr` | integer | ja |  |  | Geburtsjahr des Kindes; fehlt es in der Eingabe, wird es als Bezugsjahr minus alter_kind abgeleitet. Ab Jahrgang 2020 besteht Anspruch auf die staatliche Zahlung (Modellrechnung nach Referentenentwurf FrühStRG-E). |
| `alter_kind` | integer | ja |  |  | Alter des Kindes in Jahren als bezugsjahr minus geburtsjahr, ohne Geburtstag im Jahr. Bestimmt nur, wie lange Eltern bis 18 noch einzahlen können. |
| `bezugsjahr` | integer | ja |  |  | Kalenderjahr, gegen das das Alter gerechnet wurde |
| `eigenbeitrag_eltern_monat` | string | ja |  |  | Monatlicher Eltern- bzw. Drittbeitrag bis zum 18. Lebensjahr in EUR, nach Kappung auf eigenbeitrag_max_monat. |
| `eigenbeitrag_ab_18_monat` | string | ja |  |  | Monatlicher Eigenbeitrag des Kindes ab 18 bis zum Renteneintritt in EUR, nach Kappung auf eigenbeitrag_max_monat. |
| `renteneintritt` | integer | ja |  |  | Renteneintrittsalter in Jahren aus der Eingabe (Standard 67); Ende der Wachstumsphase und Beginn der Auszahlung. |
| `rendite_prozent` | string | ja |  |  | Angenommene Rendite in Prozent p. a. (6.0 = 6 %). Wird als Jahressatz / 12 monatlich verzinst und gilt für Spar-, Wachstums- und Auszahlphase gleichermaßen. |
| `foerderberechtigt` | boolean | ja |  |  | Anspruch auf die staatliche Zahlung (§ 30 Abs. 1 S. 2 FrühStRG-E) |
| `foerder_start_jahrgang` | integer | ja |  |  | Erster anspruchsberechtigter Geburtsjahrgang |
| `eigenbeitrag_gekappt` | boolean | ja |  |  | Eingabe lag über 570 EUR/Monat und wurde auf § 3 Abs. 3 gekappt |
| `eigenbeitrag_max_monat` | string | ja |  |  | Monatliche Obergrenze für Eigenbeiträge in EUR (570), abgeleitet aus 6.840 EUR je Kalenderjahr nach § 3 Abs. 3 FrühStRG-E. |
| `eigenbeitrag_max_jahr` | string | ja |  |  | Obergrenze für Einzahlungen neben der Förderung, § 3 Abs. 3 FrühStRG-E |
| `monate_staat` | integer | ja |  |  | Monate mit staatlicher Zahlung, 0 ohne Anspruch |
| `monate_eltern` | integer | ja |  |  | Monate, in denen Eigenbeiträge bis 18 möglich sind |
| `monate_wachstumsphase` | integer | ja |  |  | Monate vom 18. Lebensjahr bis zum Renteneintritt: (renteneintritt − 18) × 12. In dieser Phase gibt es keinen Staatsbeitrag mehr. |
| `jahre_staat` | string | ja |  |  | Dauer der staatlichen Zahlung in Jahren (monate_staat / 12, eine Nachkommastelle): 12.0 bei Anspruch, sonst 0.0. |
| `jahre_eltern` | string | ja |  |  | Jahre, in denen Eltern bis 18 noch einzahlen können: ab dem höheren Wert aus heutigem Alter und 6 bis 18. Wird auch bei Eigenbeitrag 0 ausgewiesen. |
| `jahre_wachstumsphase` | string | ja |  |  | monate_wachstumsphase in Jahren, eine Nachkommastelle. |
| `summe_staat` | string | ja |  |  | Summe der staatlichen Einzahlungen in EUR ohne Rendite: 10 EUR × monate_staat; 0 ohne Anspruch. |
| `summe_eltern` | string | ja |  |  | Summe der Eltern-Einzahlungen bis 18 in EUR ohne Rendite. |
| `summe_kind_eigen` | string | ja |  |  | Summe der Eigenbeiträge des Kindes ab 18 bis Renteneintritt in EUR ohne Rendite. |
| `summe_eingezahlt_gesamt` | string | ja |  |  | Summe aller Einzahlungen (Staat, Eltern, Kind) in EUR ohne Rendite. |
| `endwert_staat_18` | string | ja |  |  | Kapital aus den staatlichen 10 EUR/Monat mit 18 Jahren in EUR, inklusive Zinseszins; 0 ohne Anspruch. |
| `endwert_eltern_18` | string | ja |  |  | Kapital aus den Eltern-Einzahlungen mit 18 Jahren in EUR, inklusive Zinseszins. |
| `kapitalstock_18` | string | ja |  |  | Gesamtkapital mit 18 Jahren in EUR: endwert_staat_18 plus endwert_eltern_18. |
| `kapitalstock_18_gewachsen` | string | ja |  |  | kapitalstock_18 ohne weitere Einzahlungen bis zum Renteneintritt verzinst, in EUR. |
| `endwert_kind_eigen_rente` | string | ja |  |  | Kapital bei Renteneintritt in EUR aus den Eigenbeiträgen des Kindes ab 18, inklusive Zinseszins. |
| `kapitalstock_renteneintritt` | string | ja |  |  | Gesamtkapital bei Renteneintritt in EUR: kapitalstock_18_gewachsen plus endwert_kind_eigen_rente. Nominal, ohne Kosten und Inflationsbereinigung. |
| `nur_staat_kapital_18` | string | ja |  |  | Kapital mit 18 Jahren in EUR, wenn nur der Staatsbeitrag eingezahlt wird; identisch mit endwert_staat_18. |
| `nur_staat_kapital_rente` | string | ja |  |  | Kapital bei Renteneintritt in EUR, wenn nur der Staatsbeitrag eingezahlt und bis dahin verzinst wird; 0 ohne Anspruch. |
| `vorteil_eltern_rente` | string | ja |  |  | DEPRECATED (2026.52): irrefuehrend benannt, enthaelt auch die Eigenbeitraege des Kindes ab 18. Identisch mit mehrkapital_eigenbeitraege_rente. Wird in einer kuenftigen API-Version entfernt. |
| `mehrkapital_eigenbeitraege_rente` | string | ja |  |  | Mehrkapital bei Renteneintritt in EUR gegenüber der reinen Staatsförderung: kapitalstock_renteneintritt minus nur_staat_kapital_rente, also was die Beiträge der Eltern und die Eigenbeiträge des Kindes ab 18 bis zur Rente zusätzlich bringen. |
| `auszahlphase_jahre` | integer | ja |  |  | Angenommene Dauer der Auszahlphase in Jahren, fest 25. |
| `monatliche_rente` | string | ja |  |  | Monatliche Auszahlung in EUR, die kapitalstock_renteneintritt über 25 Jahre bei weiterer Verzinsung mit rendite_prozent vollständig aufzehrt (Annuität). Nominal, ohne Kosten. |
| `monatliche_rente_nur_staat` | string | ja |  |  | Monatliche Auszahlung in EUR über 25 Jahre aus nur_staat_kapital_rente, also nur aus dem Staatsbeitrag; 0 ohne Anspruch. |
| `wachstumsfaktor` | string | ja |  |  | Endkapital / eingezahlt Summe |
