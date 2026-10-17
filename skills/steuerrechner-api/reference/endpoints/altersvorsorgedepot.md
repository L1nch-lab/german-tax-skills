# Altersvorsorgedepot – Riester-Nachfolger (ab 2027)

`POST /v1/altersvorsorgedepot`

Kategorie: Altersvorsorgedepot

Berechnet Zulagen, Steuervorteil und Projektion des neuen Altersvorsorge-depots (Altersvorsorgereformgesetz v. 26.05.2026, BGBl. I 2026 Nr. 156, Start 01.01.2027). Zulagen-Staffelung § 84 EStG n.F.: 50 % auf erste 360 EUR (max 180), 25 % auf 360-1.800 EUR (max 360), Kinderzulage 100 % bis 300 EUR/Kind, einmalig +200 EUR fuer unter 25-Jaehrige. Mindesteigenbeitrag 120 EUR/Jahr (§ 86). Sonderausgabenabzug § 10a EStG n.F.: Eigenbeitraege bis 1.800 EUR zuzueglich Zulagen. Mittelbar zulageberechtigter Ehegatte (§ 84 S. 3/4 n.F.): Grundzulage bis 175 EUR. Steuervorteil auf dem zu versteuernden Einkommen (Eingabe 'zve' oder Schaetzung aus Brutto und Steuerklasse), Splitting bei Zusammenveranlagung. Vergleich gegen einen Riester-Bestandsvertrag, der nach § 52 Abs. 50a EStG n.F. im alten Recht bleibt (175 EUR Grund, 185/300 EUR je Kind vor/ab 2008, Mindesteigenbeitrag 4 % vom Vorjahreseinkommen, 2.100 EUR SA-Abzug).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `jahresbrutto` | number | ja |  |  | Jahresbruttoeinkommen in EUR |
| `eigenanteil_monat` | number | ja |  |  | Monatlicher Eigenbeitrag in EUR |
| `anzahl_kinder` | integer | ja |  |  | Kindergeldberechtigte Kinder |
| `kinder_vor_2008` | integer |  | 0 |  | Davon vor dem 01.01.2008 geboren. Nur fuer den Riester-Vergleich: Kinderzulage 185 statt 300 EUR (§ 85 Abs. 1 EStG). Hoechstens anzahl_kinder. |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Steuerklasse 1-6. Bestimmt die Schaetzung des zu versteuernden Einkommens (Pauschbetraege, Vorsorgepauschale), wenn kein 'zve' uebergeben wird. |
| `kirchensteuer` | boolean |  | false |  | Ohne Wirkung auf das Ergebnis, nur aus Kompatibilitaet angenommen: die Guenstigerpruefung (§ 10a Abs. 2 EStG) vergleicht die Zulage nur mit der Einkommensteuer-Ersparnis. |
| `alter` | integer |  | 35 |  | Aktuelles Alter |
| `zve` | number |  |  |  | Zu versteuerndes Einkommen in EUR fuer die Guenstigerpruefung, bei Zusammenveranlagung das gemeinsame beider Ehegatten. Ohne Angabe wird es aus jahresbrutto und steuerklasse geschaetzt wie im Lohnsteuerabzug. |
| `zusammenveranlagung` | boolean |  | false |  | Zusammenveranlagung mit dem Ehegatten (§ 26b EStG): Steuervorteil im Splittingtarif. Ohne 'zve' wird angenommen, dass der Ehegatte kein eigenes Einkommen hat. |
| `ehepartner_mittelbar` | boolean |  | false |  | Der Ehegatte ist selbst nicht foerderberechtigt, hat aber einen eigenen Vertrag und ist darueber mittelbar zulageberechtigt (§ 79 S. 2 EStG). Er zahlt dafuer mindestens 120 EUR im Jahr ein (Riester-Bestandsvertrag: 60 EUR) und bekommt eine eigene Grundzulage, siehe ehepartner_grundzulage. Die Kinderzulagen stehen in 'anzahl_kinder' gleich, egal welchem Ehegatten sie zugeordnet sind. |
| `vorjahreseinkommen` | number |  |  |  | Nur fuer den Riester-Vergleich: beitragspflichtige Einnahmen des Vorjahres in EUR, aus denen der Mindesteigenbeitrag (4 %) berechnet wird (§ 86 Abs. 1 EStG a.F.). Ohne Angabe gilt jahresbrutto. |
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
| `jahresbrutto` | string | ja |  |  | Jahresbruttoeinkommen in EUR aus der Eingabe. Grundlage für zve_angesetzt, wenn kein zve übergeben wird, und für den Riester-Mindesteigenbeitrag, wenn kein vorjahreseinkommen übergeben wird. |
| `zve_angesetzt` | string | ja |  |  | Zu versteuerndes Einkommen in EUR, auf dem steuervorteil und riester_steuervorteil gerechnet werden: das übergebene zve oder, ohne Angabe, jahresbrutto minus Arbeitnehmer- und Sonderausgaben-Pauschbetrag und Vorsorgepauschale nach Steuerklasse (wie im Lohnsteuerabzug). |
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
| `ehepartner_grundzulage` | string | ja |  |  | Grundzulage des mittelbar zulageberechtigten Ehepartners in EUR pro Jahr (§ 84 S. 3 und 4 EStG n.F.): dieselbe Staffel auf den Eigenbeitrag des unmittelbar Berechtigten, höchstens 175 EUR. Fließt in den Vertrag des Ehepartners, nicht in gesamtbeitrag_jahr. 0 ohne ehepartner_mittelbar. |
| `gesamtbeitrag_jahr` | string | ja |  |  | Jährliche Einzahlung ins Depot in EUR: eigenanteil_jahr plus zulagen_gesamt. Ein Steuervorteil über die Zulagen hinaus fließt nicht ein. |
| `sa_abzug` | string | ja |  |  | Sonderausgabenabzug § 10a EStG n.F. in EUR: Eigenbeiträge bis 1.800 EUR plus Zulagen. Mit ehepartner_mittelbar zusätzlich 120 EUR Beitrag und die Zulage des Ehepartners (§ 10a Abs. 3 S. 2 bis 4). |
| `steuervorteil` | string | ja |  |  | Einkommensteuer-Ersparnis in EUR pro Jahr durch sa_abzug, gerechnet auf zve_angesetzt (Splittingtarif bei zusammenveranlagung). Nur Einkommensteuer: die Günstigerprüfung nach § 10a Abs. 2 EStG vergleicht die Zulage mit der Einkommensteuer-Ersparnis, Soli und Kirchensteuer zählen dafür nicht. |
| `foerderung_gesamt` | string | ja |  |  | Förderung in EUR pro Jahr nach Günstigerprüfung: der höhere Wert aus den Zulagen (zulagen_gesamt plus ehepartner_grundzulage) und steuervorteil. |
| `effektive_belastung_jahr` | string | ja |  |  | Netto-Aufwand in EUR pro Jahr: eigenanteil_jahr minus den Teil des Steuervorteils, der die Zulagen übersteigt (Günstigerprüfung). Gleich eigenanteil_jahr, wenn die Zulagen höher sind. |
| `effektive_belastung_monat` | string | ja |  |  | effektive_belastung_jahr geteilt durch 12, in EUR pro Monat. |
| `riester_grundzulage` | string | ja |  |  | Riester-Grundzulage eines Bestandsvertrags (Recht bis 31.12.2026, gilt für Verträge von vor 2027 weiter, § 52 Abs. 50a EStG n.F.) in EUR pro Jahr: 175 EUR, anteilig gekürzt, wenn der Eigenbeitrag unter riester_mindesteigenbeitrag liegt. |
| `riester_kinderzulage` | string | ja |  |  | Riester-Kinderzulage in EUR pro Jahr: 300 EUR je ab 2008 geborenem Kind, 185 EUR je Kind aus kinder_vor_2008, mit demselben Kürzungsfaktor wie die Grundzulage. |
| `riester_zulagen_gesamt` | string | ja |  |  | Summe aus riester_grundzulage und riester_kinderzulage in EUR pro Jahr, ohne Berufseinsteiger-Bonus und ohne Zulage des Ehepartners. |
| `riester_berufseinsteiger_bonus` | string | ja |  |  | Einmalige Erhöhung der Riester-Grundzulage um 200 EUR für unter 25-Jährige (§ 84 S. 2 EStG a.F.), mit demselben Kürzungsfaktor. |
| `riester_ehepartner_grundzulage` | string | ja |  |  | Riester-Grundzulage des mittelbar zulageberechtigten Ehepartners in EUR pro Jahr: 175 EUR, gekürzt im Verhältnis des Eigenbeitrags zum Mindesteigenbeitrag (§ 86 Abs. 2 S. 1 EStG a.F.). 0 ohne ehepartner_mittelbar. |
| `riester_mindesteigenbeitrag` | string | ja |  |  | Riester-Mindesteigenbeitrag in EUR pro Jahr (§ 86 Abs. 1 EStG a.F.): 4 % von vorjahreseinkommen (ersatzweise jahresbrutto), höchstens 2.100 EUR, minus alle Zulagen inklusive Bonus und Ehepartner, mindestens 60 EUR. |
| `riester_steuervorteil` | string | ja |  |  | Einkommensteuer-Ersparnis nach altem Riester-Recht in EUR pro Jahr: Abzug von Eigenbeitrag plus Zulagen, höchstens 2.100 EUR (mit ehepartner_mittelbar 2.160 EUR), auf zve_angesetzt. |
| `riester_foerderung` | string | ja |  |  | Riester-Förderung in EUR pro Jahr nach Günstigerprüfung: der höhere Wert aus den Zulagen (riester_zulagen_gesamt plus riester_ehepartner_grundzulage) und riester_steuervorteil. |
| `vorteil_vs_riester` | string | ja |  |  | Jährliche Mehrförderung in EUR des neuen Depots gegenüber Riester (Förderung neu minus riester_foerderung); negativ, wenn Riester günstiger wäre. |
| `depot_bei_rente` | string | ja |  |  | Projiziertes Depotvermögen bei Renteneintritt in EUR: gesamtbeitrag_jahr jährlich nachschüssig mit rendite_prozent über jahre_bis_rente verzinst, plus verzinster Berufseinsteiger-Bonus. Nominal, ohne Kosten und Steuern. |
| `depot_riester_bei_rente` | string | ja |  |  | Vergleichswert: Depotvermögen bei Renteneintritt in EUR, wenn Eigenbeitrag plus Riester-Zulagen und riester_berufseinsteiger_bonus mit derselben Rendite angelegt würden. |
| `depot_nur_eigen` | string | ja |  |  | Depotvermögen bei Renteneintritt in EUR nur aus den Eigenbeiträgen, ohne Zulagen, mit derselben Rendite. |
| `depot_vorteil_zulagen` | string | ja |  |  | Mehrvermögen bei Renteneintritt in EUR durch Zulagen und Bonus: depot_bei_rente minus depot_nur_eigen. |
