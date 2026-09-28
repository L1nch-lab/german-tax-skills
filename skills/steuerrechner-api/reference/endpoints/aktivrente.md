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
| `brutto_rente_monat` | string | ja |  |  |  |
| `zusatzeinkommen_monat` | string | ja |  |  |  |
| `gesamt_brutto_monat` | string | ja |  |  |  |
| `besteuerungsanteil` | string | ja |  |  |  |
| `kirchensteuer` | boolean | ja |  |  |  |
| `bundesland` | string | ja |  |  |  |
| `monate_mit_voraussetzungen` | integer | ja |  |  | Monate mit Voraussetzungen des § 3 Nr. 21 S. 1 EStG (Zwoelftelung S. 3) |
| `freibetrag_monat` | string | ja |  |  | Genutzter Aktivrente-Freibetrag/Monat |
| `freibetrag_jahr` | string | ja |  |  |  |
| `est_ohne` | string | ja |  |  | ESt ohne Aktivrente (altes Recht) |
| `soli_ohne` | string | ja |  |  |  |
| `kist_ohne` | string | ja |  |  |  |
| `abzuege_ohne_jahr` | string | ja |  |  |  |
| `netto_ohne_monat` | string | ja |  |  |  |
| `est_mit` | string | ja |  |  | ESt mit Aktivrente (neues Recht) |
| `soli_mit` | string | ja |  |  |  |
| `kist_mit` | string | ja |  |  |  |
| `abzuege_mit_jahr` | string | ja |  |  |  |
| `netto_mit_monat` | string | ja |  |  |  |
| `ersparnis_jahr` | string | ja |  |  | Steuerersparnis pro Jahr durch Aktivrente |
| `ersparnis_monat` | string | ja |  |  |  |
