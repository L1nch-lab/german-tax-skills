# Aktivrente-Freibetrag-Rechner (Aktivrentengesetz 2026)

`POST /v1/aktivrente`

Kategorie: Aktivrente

Berechnet die Steuerersparnis durch den Aktivrente-Freibetrag (§ 3 Nr. 21 EStG, eingefuegt durch das Aktivrentengesetz v. 22.12.2025, BGBl. 2025 I Nr. 361, in Kraft seit 01.01.2026): Arbeitslohn bleibt bis 24.000 EUR/Jahr steuerfrei – KEIN Progressionsvorbehalt. Vergleicht ESt + Soli + KiSt nach altem Recht (ohne Freibetrag) gegen neues Recht (mit Freibetrag) und liefert die monatliche und jaehrliche Ersparnis. Voraussetzung ist Arbeitslohn nach § 19 Abs. 1 S. 1 Nr. 1 EStG ab dem Folgemonat nach Erreichen der Regelaltersgrenze, fuer den der Arbeitgeber RV-Beitraege nach §§ 168/172/172a SGB VI schuldet – Minijob und Selbstaendigkeit sind ausgeschlossen. Ueber `monate_mit_voraussetzungen` wird die Zwoelftelung nach § 3 Nr. 21 S. 3 EStG abgebildet.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_rente_monat` | number | ja |  |  | Monatliche Bruttorente in EUR |
| `zusatzeinkommen_monat` | number | ja |  |  | Monatlicher Brutto-Arbeitslohn aus sozialversicherungspflichtiger Anstellung in EUR. Nur nichtselbstaendige Arbeit nach § 19 Abs. 1 S. 1 Nr. 1 EStG – Selbstaendigkeit, Gewerbe und Minijob fallen nicht unter § 3 Nr. 21 EStG. |
| `monate_mit_voraussetzungen` | integer |  | 12 |  | Kalendermonate, in denen die Voraussetzungen des § 3 Nr. 21 S. 1 EStG vorlagen (Arbeitslohn ab dem Folgemonat nach Erreichen der Regelaltersgrenze + Arbeitgeber-RV-Beitrag). Jeder Monat ohne Voraussetzungen kuerzt den Freibetrag um ein Zwoelftel (S. 3). 12 = ganzjaehrig erfuellt. |
| `kirchensteuer` | boolean |  | false |  | Kirchensteuerpflichtig? |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (fuer KiSt 8 % oder 9 %) |
| `besteuerungsanteil` | number |  | "0.84" |  | Anteil der Rente steuerpflichtig (0.5-1.0, Default 0.84) |

Beispiel:

```json
{
  "brutto_rente_monat": 1800,
  "bundesland": "Nordrhein-Westfalen",
  "zusatzeinkommen_monat": 1500
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_rente_monat` | string | ja |  |  | Monatliche Bruttorente in EUR aus der Eingabe, auf 2 Stellen gerundet. |
| `zusatzeinkommen_monat` | string | ja |  |  | Monatlicher Brutto-Arbeitslohn in EUR aus der Eingabe (nur nichtselbständige Arbeit, die unter § 3 Nr. 21 EStG fällt). |
| `gesamt_brutto_monat` | string | ja |  |  | Summe aus brutto_rente_monat und zusatzeinkommen_monat in EUR pro Monat. |
| `besteuerungsanteil` | string | ja |  |  | Steuerpflichtiger Anteil der Rente als Faktor 0–1 (Standard 0.84), Echo der Eingabe. Wird direkt mit der Jahresbruttorente multipliziert. |
| `kirchensteuer` | boolean | ja |  |  | Echo der Eingabe: true, wenn Kirchensteuer mitgerechnet wird. |
| `bundesland` | string | ja |  |  | Bundesland aus der Eingabe; bestimmt nur den Kirchensteuersatz (8 % oder 9 % der ESt). |
| `monate_mit_voraussetzungen` | integer | ja |  |  | Monate mit Voraussetzungen des § 3 Nr. 21 S. 1 EStG (Zwoelftelung S. 3) |
| `freibetrag_monat` | string | ja |  |  | Genutzter Aktivrente-Freibetrag/Monat |
| `freibetrag_jahr` | string | ja |  |  | Tatsächlich angesetzter Aktivrente-Freibetrag in EUR pro Jahr: Arbeitslohn der Monate mit Voraussetzungen, höchstens 2.000 EUR je solchem Monat (Zwölftelung nach § 3 Nr. 21 S. 3 EStG). |
| `est_ohne` | string | ja |  |  | ESt ohne Aktivrente (altes Recht) |
| `soli_ohne` | string | ja |  |  | Solidaritätszuschlag in EUR pro Jahr ohne Aktivrente-Freibetrag. |
| `kist_ohne` | string | ja |  |  | Kirchensteuer in EUR pro Jahr ohne Aktivrente-Freibetrag; 0, wenn kirchensteuer false ist. |
| `abzuege_ohne_jahr` | string | ja |  |  | ESt + Soli + KiSt in EUR pro Jahr ohne Freibetrag. Das zvE ist steuerpflichtiger Rentenanteil plus Arbeitslohn im Grundtarif, ohne Pauschbeträge, Vorsorgeaufwendungen oder Sozialabgaben. |
| `netto_ohne_monat` | string | ja |  |  | Monatliches Netto in EUR ohne Freibetrag: (Jahresrente + Jahresarbeitslohn − abzuege_ohne_jahr) / 12. Kranken-, Pflege- und Rentenversicherungsbeiträge sind nicht abgezogen. |
| `est_mit` | string | ja |  |  | ESt mit Aktivrente (neues Recht) |
| `soli_mit` | string | ja |  |  | Solidaritätszuschlag in EUR pro Jahr mit Aktivrente-Freibetrag. |
| `kist_mit` | string | ja |  |  | Kirchensteuer in EUR pro Jahr mit Aktivrente-Freibetrag; 0, wenn kirchensteuer false ist. |
| `abzuege_mit_jahr` | string | ja |  |  | ESt + Soli + KiSt in EUR pro Jahr mit Freibetrag (zvE um freibetrag_jahr gemindert, kein Progressionsvorbehalt). Gleiche Vereinfachungen wie abzuege_ohne_jahr. |
| `netto_mit_monat` | string | ja |  |  | Monatliches Netto in EUR mit Freibetrag: (Jahresrente + Jahresarbeitslohn − abzuege_mit_jahr) / 12, ohne Sozialabgaben. |
| `ersparnis_jahr` | string | ja |  |  | Steuerersparnis pro Jahr durch Aktivrente |
| `ersparnis_monat` | string | ja |  |  | Steuerersparnis durch den Aktivrente-Freibetrag in EUR pro Monat: (abzuege_ohne_jahr − abzuege_mit_jahr) / 12. |
