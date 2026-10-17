# Riester – Mindesteigenbeitrag, Zulagen, Günstigerprüfung

`POST /v1/riester`

Kategorie: Altersvorsorgedepot

Riester-Förderung eines Bestandsvertrags für das Beitragsjahr: Mindesteigenbeitrag für die volle Zulage (4 % der beitragspflichtigen Vorjahres-Einnahmen, höchstens 2.100 EUR, minus Zulagen, mindestens 60 EUR), Grundzulage 175 EUR, einmalig +200 EUR für Berufseinsteiger, Kinderzulage 185/300 EUR je Kind vor/ab 2008, Grundzulage des mittelbar berechtigten Ehegatten, Sonderausgabenabzug § 10a EStG mit Günstigerprüfung. Verträge von vor 2027 behalten dieses Recht bis zur Auszahlungsphase (§ 52 Abs. 50a EStG n.F.); für neue Verträge ab 2027 siehe /v1/altersvorsorgedepot.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `vorjahreseinkommen` | number | ja |  |  | Beitragspflichtige Einnahmen des Vorjahres in EUR (§ 86 Abs. 1 S. 2 EStG), bei Arbeitnehmern das Vorjahresbrutto. Daraus folgen Mindesteigenbeitrag und die Schaetzung des zu versteuernden Einkommens. |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Steuerklasse 1-6, nur fuer die Schaetzung des zu versteuernden Einkommens. |
| `kinder_ab_2008` | integer |  | 0 |  | Kinder mit Kinderzulage, geboren nach dem 31.12.2007 (300 EUR je Kind). |
| `kinder_vor_2008` | integer |  | 0 |  | Kinder mit Kinderzulage, geboren vor dem 01.01.2008 (185 EUR je Kind). |
| `berufseinsteiger` | boolean |  | false |  | Zu Beginn des Beitragsjahres unter 25 und erstes Zulagejahr: einmalig 200 EUR mehr Grundzulage (§ 84 S. 2 EStG). |
| `zusammenveranlagung` | boolean |  | false |  | Verheiratet und zusammen veranlagt: Steuervorteil im Splittingtarif. |
| `ehepartner_mittelbar` | boolean |  | false |  | Ehegatte ist mittelbar zulageberechtigt (§ 79 S. 2 EStG): eigener Vertrag, 60 EUR Mindestbeitrag, eigene Grundzulage 175 EUR. Nur zusammen mit zusammenveranlagung. |

Beispiel:

```json
{
  "kinder_ab_2008": 1,
  "vorjahreseinkommen": 45000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `grundzulage` | string | ja |  |  | Grundzulage in EUR: 175 EUR, mit berufseinsteiger 375 EUR (§ 84 EStG). |
| `berufseinsteiger_bonus` | string | ja |  |  | Einmalige Erhöhung um 200 EUR (§ 84 S. 2 EStG), sonst 0. |
| `kinderzulage` | string | ja |  |  | Kinderzulage in EUR: 300 je Kind ab 2008, 185 je Kind vor 2008 (§ 85 Abs. 1 EStG). |
| `zulage_eigen` | string | ja |  |  | grundzulage plus kinderzulage in EUR. |
| `zulage_partner` | string | ja |  |  | Grundzulage des mittelbar berechtigten Ehegatten in EUR (175 oder 0). |
| `zulage_gesamt` | string | ja |  |  | Alle Zulagen des Haushalts in EUR pro Jahr. |
| `zulage_anrechenbar` | string | ja |  |  | Zulage, die in Sonderausgabenabzug und Günstigerprüfung zählt: zulage_gesamt ohne Berufseinsteiger-Bonus (§ 10a Abs. 1 S. 5 EStG; BMF-Schreiben vom 05.10.2023, Rn. 92, 103 und 106). |
| `mindesteigenbeitrag` | string | ja |  |  | Eigenbeitrag in EUR pro Jahr für die volle Zulage: 4 % von vorjahreseinkommen, höchstens 2.100 EUR, minus zulage_gesamt, mindestens 60 EUR Sockel (§ 86 Abs. 1). |
| `partner_eigenbeitrag` | string | ja |  |  | Mindestbeitrag des mittelbar berechtigten Ehegatten in EUR (60 oder 0). |
| `sockel_greift` | boolean | ja |  |  | true, wenn der Sockelbetrag von 60 EUR den Mindesteigenbeitrag bestimmt. |
| `gesamtbeitrag_jahr` | string | ja |  |  | mindesteigenbeitrag plus partner_eigenbeitrag plus zulage_gesamt, in EUR. |
| `gesamtbeitrag_monat` | string | ja |  |  | gesamtbeitrag_jahr geteilt durch 12. |
| `zve_geschaetzt` | string | ja |  |  | Geschätztes zu versteuerndes Einkommen in EUR: vorjahreseinkommen minus Pauschbeträge und Vorsorgepauschale nach Steuerklasse. |
| `sonderausgaben` | string | ja |  |  | Sonderausgabenabzug § 10a EStG in EUR: Beiträge plus zulage_anrechenbar, höchstens hoechstbetrag. |
| `steuervorteil` | string | ja |  |  | Einkommensteuer-Ersparnis durch sonderausgaben in EUR (ohne Soli/KiSt). |
| `zusatz_erstattung` | string | ja |  |  | Erstattung über die Steuererklärung in EUR: steuervorteil minus zulage_anrechenbar, mindestens 0 (§ 10a Abs. 2 EStG). |
| `sonderausgaben_guenstiger` | boolean | ja |  |  | true, wenn der Sonderausgabenabzug mehr bringt als die anrechenbare Zulage. |
| `gesamtfoerderung` | string | ja |  |  | zulage_gesamt plus zusatz_erstattung in EUR pro Jahr. |
| `foerderquote` | string | ja |  |  | gesamtfoerderung in Prozent von gesamtbeitrag_jahr. |
| `hoechstbetrag` | string | ja |  |  | Höchstbetrag des Sonderausgabenabzugs in EUR: 2.100, mit mittelbar berechtigtem Ehegatten 2.160 (§ 10a Abs. 1 S. 1 und Abs. 3 S. 3 EStG). |
