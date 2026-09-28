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
| `jahresbrutto` | string | ja |  |  |  |
| `eigenanteil_monat` | string | ja |  |  |  |
| `eigenanteil_jahr` | string | ja |  |  |  |
| `anzahl_kinder` | integer | ja |  |  |  |
| `alter` | integer | ja |  |  |  |
| `renteneintritt` | integer | ja |  |  |  |
| `jahre_bis_rente` | integer | ja |  |  |  |
| `rendite_prozent` | string | ja |  |  |  |
| `grundzulage` | string | ja |  |  |  |
| `zulage_stufe_1` | string | ja |  |  | 50 % auf erste 360 EUR |
| `zulage_stufe_2` | string | ja |  |  | 25 % auf 360-1.800 EUR |
| `kinderzulage` | string | ja |  |  |  |
| `zulagen_gesamt` | string | ja |  |  |  |
| `berufseinsteiger_bonus` | string | ja |  |  | Einmalig 200 EUR fuer unter 25-Jaehrige (§ 84 S. 2 EStG n.F.) |
| `gesamtbeitrag_jahr` | string | ja |  |  |  |
| `sa_abzug` | string | ja |  |  | Sonderausgabenabzug § 10a EStG n.F.: Eigenbeitraege bis 1.800 EUR + Zulagen |
| `steuervorteil` | string | ja |  |  |  |
| `foerderung_gesamt` | string | ja |  |  | Guenstigerpruefung Zulage vs Steuervorteil |
| `effektive_belastung_jahr` | string | ja |  |  |  |
| `effektive_belastung_monat` | string | ja |  |  |  |
| `riester_grundzulage` | string | ja |  |  |  |
| `riester_kinderzulage` | string | ja |  |  |  |
| `riester_zulagen_gesamt` | string | ja |  |  |  |
| `riester_steuervorteil` | string | ja |  |  |  |
| `riester_foerderung` | string | ja |  |  |  |
| `vorteil_vs_riester` | string | ja |  |  |  |
| `depot_bei_rente` | string | ja |  |  |  |
| `depot_riester_bei_rente` | string | ja |  |  |  |
| `depot_nur_eigen` | string | ja |  |  |  |
| `depot_vorteil_zulagen` | string | ja |  |  |  |
