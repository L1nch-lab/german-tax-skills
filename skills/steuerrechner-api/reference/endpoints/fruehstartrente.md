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
| `geburtsjahr` | integer | ja |  |  |  |
| `alter_kind` | integer | ja |  |  |  |
| `bezugsjahr` | integer | ja |  |  | Kalenderjahr, gegen das das Alter gerechnet wurde |
| `eigenbeitrag_eltern_monat` | string | ja |  |  |  |
| `eigenbeitrag_ab_18_monat` | string | ja |  |  |  |
| `renteneintritt` | integer | ja |  |  |  |
| `rendite_prozent` | string | ja |  |  |  |
| `foerderberechtigt` | boolean | ja |  |  | Anspruch auf die staatliche Zahlung (§ 30 Abs. 1 S. 2 FrühStRG-E) |
| `foerder_start_jahrgang` | integer | ja |  |  | Erster anspruchsberechtigter Geburtsjahrgang |
| `eigenbeitrag_gekappt` | boolean | ja |  |  | Eingabe lag über 570 EUR/Monat und wurde auf § 3 Abs. 3 gekappt |
| `eigenbeitrag_max_monat` | string | ja |  |  |  |
| `eigenbeitrag_max_jahr` | string | ja |  |  | Obergrenze für Einzahlungen neben der Förderung, § 3 Abs. 3 FrühStRG-E |
| `monate_staat` | integer | ja |  |  | Monate mit staatlicher Zahlung, 0 ohne Anspruch |
| `monate_eltern` | integer | ja |  |  | Monate, in denen Eigenbeiträge bis 18 möglich sind |
| `monate_wachstumsphase` | integer | ja |  |  |  |
| `jahre_staat` | string | ja |  |  |  |
| `jahre_eltern` | string | ja |  |  |  |
| `jahre_wachstumsphase` | string | ja |  |  |  |
| `summe_staat` | string | ja |  |  |  |
| `summe_eltern` | string | ja |  |  |  |
| `summe_kind_eigen` | string | ja |  |  |  |
| `summe_eingezahlt_gesamt` | string | ja |  |  |  |
| `endwert_staat_18` | string | ja |  |  |  |
| `endwert_eltern_18` | string | ja |  |  |  |
| `kapitalstock_18` | string | ja |  |  |  |
| `kapitalstock_18_gewachsen` | string | ja |  |  |  |
| `endwert_kind_eigen_rente` | string | ja |  |  |  |
| `kapitalstock_renteneintritt` | string | ja |  |  |  |
| `nur_staat_kapital_18` | string | ja |  |  |  |
| `nur_staat_kapital_rente` | string | ja |  |  |  |
| `vorteil_eltern_rente` | string | ja |  |  |  |
| `auszahlphase_jahre` | integer | ja |  |  |  |
| `monatliche_rente` | string | ja |  |  |  |
| `monatliche_rente_nur_staat` | string | ja |  |  |  |
| `wachstumsfaktor` | string | ja |  |  | Endkapital / eingezahlt Summe |
