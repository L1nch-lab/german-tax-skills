# Mieteinnahmen versteuern

`POST /v1/mieteinnahmen`

Kategorie: Mieteinnahmen

Berechnet die Steuer-Mehrbelastung aus Einkuenften aus Vermietung und Verpachtung nach §21 EStG.

**Marginalsteuersatz-Verfahren.** Mieteinkuenfte haben keinen eigenen Steuersatz – sie werden auf das uebrige Einkommen aufgeschlagen und im persoenlichen Tarif versteuert. Ausgewiesen wird deshalb die MEHRBELASTUNG: Steuer auf `anderes_zve` plus Mieteinkuenfte minus Steuer auf `anderes_zve` allein.

⚠️ `anderes_zve` ist das ergebnisentscheidende Feld. Ohne diesen Wert rechnet der Endpoint ab dem Grundfreibetrag und liefert eine deutlich zu niedrige Belastung – bei 12.000 EUR Mieteinkuenften ist der Unterschied zwischen `anderes_zve=0` und `anderes_zve=55000` groesser als der halbe Betrag.

**Werbungskosten.** `afa_jahr`, `schuldzinsen_jahr`, `erhaltungsaufwand_jahr` und `sonstige_wk_jahr` werden nach §9 EStG abgezogen. Bei den Schuldzinsen zaehlt nur der Zinsanteil, nicht die Tilgung.

**Verlust.** Uebersteigen die Werbungskosten die Miete, ist `mieteinkuenfte` negativ und `mehrbelastung_total` sinkt unter null – der Verlust mindert dann das zu versteuernde Einkommen (§2 Abs. 3 EStG). `effektivlast_prozent` ist in dem Fall 0, weil ein Prozentsatz auf einen Verlust nichts aussagt.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_miete_jahr` | number | ja |  |  | Jahres-Kaltmiete in EUR. Umlagefaehige Nebenkosten gehoeren NICHT hierher; nicht umlagefaehige Kosten in `sonstige_wk_jahr`. |
| `afa_jahr` | number |  | "0" |  | Gebaeude-AfA pro Jahr in EUR (§7 Abs. 4/5 EStG). Der Satz haengt am Baujahr: 2 % fuer 1925-2022, 2,5 % fuer vor 1925, 3 % ab Fertigstellung 2023. |
| `schuldzinsen_jahr` | number |  | "0" |  | Schuldzinsen des Finanzierungskredits pro Jahr in EUR (nur der Zinsanteil, nicht die Tilgung) |
| `erhaltungsaufwand_jahr` | number |  | "0" |  | Erhaltungsaufwand pro Jahr in EUR (Reparaturen, Instandhaltung). Groesserer Aufwand ist nach §82b EStDV auf zwei bis fuenf Jahre verteilbar. |
| `sonstige_wk_jahr` | number |  | "0" |  | Sonstige Werbungskosten pro Jahr in EUR: Verwaltung, nicht umlagefaehiges Hausgeld, Fahrten, Kontofuehrung. |
| `anderes_zve` | number |  | "0" |  | Anderes zu versteuerndes Einkommen des Vermieters in EUR (Arbeitslohn, Selbstaendigkeit). Bestimmt den Grenzsteuersatz – ohne diesen Wert wird ab dem Grundfreibetrag gerechnet und die Mehrbelastung faellt deutlich zu niedrig aus. |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (relevant fuer den Kirchensteuer-Satz: 8 % in BY/BW, sonst 9 %) |
| `kirchenmitglied` | boolean |  | false |  | True wenn Kirchensteuer abzufuehren ist |

Beispiel:

```json
{
  "afa_jahr": 3000,
  "anderes_zve": 55000,
  "brutto_miete_jahr": 12000,
  "bundesland": "Nordrhein-Westfalen",
  "erhaltungsaufwand_jahr": 500,
  "kirchenmitglied": false,
  "schuldzinsen_jahr": 2000,
  "sonstige_wk_jahr": 300
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `werbungskosten_total` | string | ja |  |  | Summe der Werbungskosten (§9 EStG) in EUR |
| `mieteinkuenfte` | string | ja |  |  | Einkuenfte aus Vermietung und Verpachtung (§21 EStG) in EUR. Negativ bei Verlust. |
| `verlust` | boolean | ja |  |  | True wenn die Mieteinkuenfte negativ sind |
| `mehrbelastung_est` | string | ja |  |  | Zusaetzliche Einkommensteuer durch die Mieteinkuenfte in EUR |
| `mehrbelastung_soli` | string | ja |  |  | Zusaetzlicher Solidaritaetszuschlag in EUR |
| `mehrbelastung_kist` | string | ja |  |  | Zusaetzliche Kirchensteuer in EUR (0 wenn kein Kirchenmitglied) |
| `mehrbelastung_total` | string | ja |  |  | Gesamte Steuer-Mehrbelastung in EUR |
| `netto_miete` | string | ja |  |  | Mieteinkuenfte nach Steuern in EUR |
| `effektivlast_prozent` | string | ja |  |  | Effektivlast in Prozent, bezogen auf die MIETEINKUENFTE (nicht auf die Bruttomiete). 0 bei Verlust. |
| `grenzsteuersatz_vorher` | string | ja |  |  | Grenzsteuersatz ohne die Mieteinkuenfte in Prozent |
| `grenzsteuersatz_nachher` | string | ja |  |  | Grenzsteuersatz mit den Mieteinkuenften in Prozent |
| `hinweise` | array<string> |  |  |  | Kontextabhaengige Hinweise zum Ergebnis (kann leer sein) |
