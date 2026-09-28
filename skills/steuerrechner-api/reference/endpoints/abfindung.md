# Abfindungsrechner

`POST /v1/abfindung`

Kategorie: Abfindung

Berechnet die Steuer auf eine Abfindung mit und ohne Fuenftelregelung nach §34 EStG. Zeigt die Steuerersparnis durch die ermaessigte Besteuerung. Ab 2025 nur noch ueber die Einkommensteuererklaerung anwendbar (nicht im Lohnsteuerabzug).

**Veranlagungsart (seit 2026.41):** `zusammenveranlagung=true` rechnet nach dem Splitting-Verfahren (§32a Abs. 5 EStG) statt nach dem Grundtarif. Weil §32a Abs. 5 auf dem *gemeinsam* zu versteuernden Einkommen rechnet, gehoert dann auch `partner_jahresbrutto` in die Anfrage – fehlt es, wird unterstellt der Partner verdiene nichts und der Splitting-Vorteil faellt zu gross aus.

⚠️ `steuerklasse` steuert den Tarif hier **nicht**. Sie wirkt nur ueber die Tabellenfreibetraege (Klasse 2 = Entlastungsbetrag, Klasse 6 = kein Arbeitnehmer-/Sonderausgaben-Pauschbetrag); der Tarif haengt an `zusammenveranlagung`. Die Fuenftelregelung ist ein Verfahren der Veranlagung, die Steuerklasse eines des Lohnsteuerabzugs.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `abfindung` | number | ja |  |  | Abfindungsbetrag in EUR |
| `jahresbrutto` | number | ja |  |  | Regulaeres Jahresbrutto (ohne Abfindung) in EUR |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (relevant fuer Kirchensteuer-Satz) |
| `kirchenmitglied` | boolean |  | false |  | True wenn Kirchensteuer abzufuehren ist |
| `kinder` | number |  | "0" |  | Anzahl Kinderfreibetraege (0, 0.5, 1, 1.5, ...) |
| `zusammenveranlagung` | boolean |  | false |  | True = Splitting-Verfahren (§32a Abs. 5 EStG), False = Grundtarif (§32a Abs. 1 EStG). ⚠️ Der Tarif haengt hieran, NICHT an der Steuerklasse – der Rechner modelliert die Veranlagung, nicht den Lohnsteuerabzug. |
| `partner_jahresbrutto` | number |  | "0" |  | Jahresbrutto des Ehepartners in EUR. Nur wirksam bei zusammenveranlagung=true. §32a Abs. 5 rechnet auf dem GEMEINSAM zu versteuernden Einkommen – ohne diesen Wert wird unterstellt, der Partner verdiene nichts, und der Splitting-Vorteil faellt zu gross aus. |

Beispiel:

```json
{
  "abfindung": 50000,
  "bundesland": "Nordrhein-Westfalen",
  "jahresbrutto": 60000,
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `fuenftelregel` | AbfindungVariante | ja |  |  | Besteuerung mit Fuenftelregelung (§34 EStG) |
| `normal` | AbfindungVariante | ja |  |  | Besteuerung ohne Fuenftelregelung |
| `ersparnis` | string | ja |  |  | Steuerersparnis durch Fuenftelregelung in EUR |
