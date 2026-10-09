# Altersvorsorgedepot – Riester-Nachfolger (ab 2027)

`POST /v1/altersvorsorgedepot`

Kategorie: Altersvorsorgedepot

Berechnet Zulagen, Steuervorteil und Projektion des neuen Altersvorsorge-depots (Altersvorsorgereformgesetz v. 26.05.2026, BGBl. I 2026 Nr. 156, Start 01.01.2027). Zulagen-Staffelung § 84 EStG n.F.: 50 % auf erste 360 EUR (max 180), 25 % auf 360-1.800 EUR (max 360), Kinderzulage 100 % bis 300 EUR/Kind, einmalig +200 EUR fuer unter 25-Jaehrige. Mindesteigenbeitrag 120 EUR/Jahr (§ 86). Sonderausgabenabzug § 10a EStG n.F.: Eigenbeitraege bis 1.800 EUR zuzueglich Zulagen. Vergleich gegen alte Riester-Rente (175 EUR Grund + 300 EUR/Kind, 2.100 EUR SA-Abzug).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `jahresbrutto` | number | ja |  |  | Jahresbruttoeinkommen in EUR |
| `eigenanteil_monat` | number | ja |  |  | Monatlicher Eigenbeitrag in EUR |
| `anzahl_kinder` | integer | ja |  |  | Kindergeldberechtigte Kinder |
| `kinder_vor_2008` | integer |  | 0 |  | Davon vor dem 01.01.2008 geboren. Nur fuer den Riester-Vergleich: Kinderzulage 185 statt 300 EUR (§ 85 Abs. 1 EStG). Hoechstens anzahl_kinder. |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Steuerklasse 1-6 |
| `kirchensteuer` | boolean |  | false |  | Kirchensteuerpflichtig? |
| `alter` | integer |  | 35 |  | Aktuelles Alter |
| `renteneintritt` | integer |  | 67 |  | Geplantes Rentenalter |
| `rendite_prozent` | number |  | "6.0" |  | Erwartete jaehrl. Rendite in % |

Beispiel:

```json
{
  "anzahl_kinder": 2,
  "eigenanteil_monat": 150,
  "jahresbrutto": 55000,
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `jahresbrutto` | string | ja |  |  | Jahresbruttoeinkommen in EUR aus der Eingabe. Wird für die Steuervorteils-Rechnung direkt als zu versteuerndes Einkommen angesetzt, ohne Abzüge. |
| `eigenanteil_monat` | string | ja |  |  | Monatlicher Eigenbeitrag in EUR aus der Eingabe. |
| `eigenanteil_jahr` | string | ja |  |  | Jährlicher Eigenbeitrag in EUR, eigenanteil_monat mal 12. |
| `anzahl_kinder` | integer | ja |  |  | Anzahl zulageberechtigter Kinder aus der Eingabe; für jedes Kind wird eine Kinderzulage angesetzt. |
| `alter` | integer | ja |  |  | Aktuelles Alter in Jahren aus der Eingabe. Unter 25 gibt es den einmaligen Berufseinsteiger-Bonus, sofern Zulagen gewährt werden. |
| `renteneintritt` | integer | ja |  |  | Geplantes Rentenalter in Jahren aus der Eingabe; Ende der Ansparphase. |
| `jahre_bis_rente` | integer | ja |  |  | Ansparjahre bis zur Rente: renteneintritt minus alter, mindestens 0. |
| `rendite_prozent` | string | ja |  |  | Angenommene Rendite in Prozent p. a. (6.0 = 6 %), Echo der Eingabe. Gilt für alle Depot-Projektionen, jährlich verzinst und ohne Kosten. |
| `grundzulage` | string | ja |  |  | Grundzulage neues Recht in EUR pro Jahr: 50 % auf die ersten 360 EUR plus 25 % auf den Eigenbeitrag zwischen 360 und 1.800 EUR. 0 unter dem Mindesteigenbeitrag von 120 EUR/Jahr; ohne Berufseinsteiger-Bonus. |
| `zulage_stufe_1` | string | ja |  |  | 50 % auf erste 360 EUR |
| `zulage_stufe_2` | string | ja |  |  | 25 % auf 360-1.800 EUR |
| `kinderzulage` | string | ja |  |  | Kinderzulage neues Recht in EUR pro Jahr für alle Kinder zusammen: je Kind 100 % des Eigenbeitrags, höchstens 300 EUR. 0 unter dem Mindesteigenbeitrag. |
| `zulagen_gesamt` | string | ja |  |  | Summe aus grundzulage und kinderzulage in EUR pro Jahr, ohne Berufseinsteiger-Bonus. |
| `berufseinsteiger_bonus` | string | ja |  |  | Einmalig 200 EUR fuer unter 25-Jaehrige (§ 84 S. 2 EStG n.F.) |
| `gesamtbeitrag_jahr` | string | ja |  |  | Jährliche Einzahlung ins Depot in EUR: eigenanteil_jahr plus zulagen_gesamt. Ein Steuervorteil über die Zulagen hinaus fließt nicht ein. |
| `sa_abzug` | string | ja |  |  | Sonderausgabenabzug § 10a EStG n.F.: Eigenbeitraege bis 1.800 EUR + Zulagen |
| `steuervorteil` | string | ja |  |  | Einkommensteuer-Ersparnis in EUR pro Jahr durch den Sonderausgabenabzug (Eigenbeitrag bis 1.800 EUR plus Zulagen), Grundtarif auf jahresbrutto als zvE. Nur ESt, ohne Soli und KiSt; steuerklasse und kirchensteuer der Eingabe wirken nicht. |
| `foerderung_gesamt` | string | ja |  |  | Guenstigerpruefung Zulage vs Steuervorteil |
| `effektive_belastung_jahr` | string | ja |  |  | Netto-Aufwand in EUR pro Jahr: eigenanteil_jahr minus den Teil des Steuervorteils, der die Zulagen übersteigt (Günstigerprüfung). Gleich eigenanteil_jahr, wenn die Zulagen höher sind. |
| `effektive_belastung_monat` | string | ja |  |  | effektive_belastung_jahr geteilt durch 12, in EUR pro Monat. |
| `riester_grundzulage` | string | ja |  |  | Vergleichswert alte Riester-Grundzulage in EUR pro Jahr: 175 EUR, anteilig gekürzt, wenn der Eigenbeitrag unter dem Mindesteigenbeitrag liegt (4 % von jahresbrutto minus Zulagen, mindestens 60 EUR). |
| `riester_kinderzulage` | string | ja |  |  | Vergleichswert alte Riester-Kinderzulage in EUR pro Jahr: einheitlich 300 EUR je Kind, mit demselben Kürzungsfaktor wie die Grundzulage. |
| `riester_zulagen_gesamt` | string | ja |  |  | Summe der Riester-Zulagen (Grund- plus Kinderzulage) in EUR pro Jahr. |
| `riester_steuervorteil` | string | ja |  |  | ESt-Ersparnis nach altem Riester-Recht in EUR pro Jahr: Sonderausgabenabzug von Eigenbeitrag plus Zulagen, höchstens 2.100 EUR; gleiche Vereinfachungen wie steuervorteil. |
| `riester_foerderung` | string | ja |  |  | Riester-Förderung in EUR pro Jahr nach Günstigerprüfung: der höhere Wert aus riester_zulagen_gesamt und riester_steuervorteil. |
| `vorteil_vs_riester` | string | ja |  |  | Jährliche Mehrförderung in EUR des neuen Depots gegenüber Riester (Förderung neu minus riester_foerderung); negativ, wenn Riester günstiger wäre. |
| `depot_bei_rente` | string | ja |  |  | Projiziertes Depotvermögen bei Renteneintritt in EUR: gesamtbeitrag_jahr jährlich nachschüssig mit rendite_prozent über jahre_bis_rente verzinst, plus verzinster Berufseinsteiger-Bonus. Nominal, ohne Kosten und Steuern. |
| `depot_riester_bei_rente` | string | ja |  |  | Vergleichswert: Depotvermögen bei Renteneintritt in EUR, wenn Eigenbeitrag plus Riester-Zulagen mit derselben Rendite angelegt würden. |
| `depot_nur_eigen` | string | ja |  |  | Depotvermögen bei Renteneintritt in EUR nur aus den Eigenbeiträgen, ohne Zulagen, mit derselben Rendite. |
| `depot_vorteil_zulagen` | string | ja |  |  | Mehrvermögen bei Renteneintritt in EUR durch Zulagen und Bonus: depot_bei_rente minus depot_nur_eigen. |
