# Freelancer-Stundensatz-Rechner (§ 18 / § 15 EStG)

`POST /v1/freelancer`

Kategorie: Freelancer

Berechnet den minimalen kostendeckenden Stundensatz auf Basis von Wunsch-Nettoeinkommen, Betriebsausgaben, Sozialversicherung (KV+PV freiwillig 21,1 %), Altersvorsorge (10 % pauschal), ESt + Soli + KiSt und ggf. Gewerbesteuer (>24.500 EUR Freibetrag × 14 % Pauschalsatz). Auslastungsmodell: 365 - 104 (WE) - 10 (Feiertag) - Urlaub - 10 (Krank) × Billable-Ratio × Stunden/Tag. Iterative Fixpunkt-Berechnung.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `wunsch_netto` | number | ja |  |  | Gewuenschtes monatliches Nettoeinkommen in EUR |
| `betriebsausgaben_monat` | number |  | "500" |  | Monatliche Betriebsausgaben in EUR |
| `urlaubstage` | integer |  | 30 |  | Urlaubstage pro Jahr |
| `billable_ratio` | number |  | "0.7" |  | Anteil abrechnungsfaehiger Tage (0.1-1.0) |
| `stunden_pro_tag` | number |  | "8" |  | Abrechnungsfaehige Stunden pro Tag |
| `ist_gewerbetreibend` | boolean |  | false |  | True wenn Gewerbe statt Freiberuf |
| `kirchenmitglied` | boolean |  | false |  | Kirchenmitglied? |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (KiSt 8 % / 9 %) |

Beispiel:

```json
{
  "betriebsausgaben_monat": 500,
  "bundesland": "Nordrhein-Westfalen",
  "wunsch_netto": 3500
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `mindeststundensatz` | string | ja |  |  | Kostendeckender Stundensatz |
| `empfohlener_stundensatz` | string | ja |  |  | +20 % Puffer |
| `bruttobedarf_jahr` | string | ja |  |  | Nötiger Jahresumsatz in EUR vor Steuern, Sozialversicherung und Betriebsausgaben, iterativ so bestimmt, dass netto_ergebnis das Wunsch-Netto × 12 auf etwa 10 EUR trifft. Basis von mindeststundensatz. |
| `betriebsausgaben_jahr` | string | ja |  |  | Betriebsausgaben pro Jahr in EUR = Eingabe betriebsausgaben_monat × 12. |
| `gewinn` | string | ja |  |  | Jahresgewinn in EUR = bruttobedarf_jahr − betriebsausgaben_jahr, nicht negativ. Bemessungsgrundlage für ESt, Gewerbesteuer, KV/PV und Altersvorsorge. |
| `est` | integer | ja |  |  | Einkommensteuer (gerundet) |
| `soli` | string | ja |  |  | Solidaritätszuschlag in EUR auf die Einkommensteuer (Einzelveranlagung, Tarif 2026). Berechnet auf est vor der Gewerbesteuer-Anrechnung. |
| `kist` | string | ja |  |  | Kirchensteuer in EUR, 8 % oder 9 % der est je nach bundesland; 0 ohne Kirchenmitgliedschaft. |
| `kv_pv` | string | ja |  |  | Freiwillige KV+PV-Beitraege/Jahr |
| `gewerbesteuer` | string | ja |  |  | Festgesetzte Gewerbesteuer in EUR. ⚠️ Das ist NICHT die Belastung – sie wird nach §35 EStG auf die Einkommensteuer angerechnet, siehe die beiden Felder darunter. 0 bei Freiberuflern und bei Gewinn unterhalb des Freibetrags. |
| `est_anrechnung` | string |  | "0" |  | Anrechnung auf die Einkommensteuer nach §35 Abs. 1 S. 1 Nr. 1 EStG: das Vierfache des Steuermessbetrags, gedeckelt auf die tatsaechlich zu zahlende Gewerbesteuer (S. 5) und auf die tarifliche Einkommensteuer als Ermaessigungshoechstbetrag (S. 2). |
| `gewerbesteuer_effektiv` | string |  | "0" |  | Gewerbesteuer nach Anrechnung – das ist der Betrag, der die Kalkulation wirklich belastet und der in den Stundensatz eingeht. Beim Musterhebesatz 400 % regelmaessig 0. |
| `altersvorsorge` | string | ja |  |  | 10 % vom Gewinn pauschal |
| `netto_ergebnis` | string | ja |  |  | Jährliches Netto in EUR = gewinn − est − soli − kist − gewerbesteuer_effektiv − kv_pv − altersvorsorge. Liegt nach der Iteration nahe am Wunsch-Netto × 12. |
| `abrechnungsfaehige_stunden` | string | ja |  |  | Abrechenbare Stunden pro Jahr = abrechnungsfaehige_tage × stunden_pro_tag, mindestens 1, gerundet auf 1 Nachkommastelle. Divisor für die Stundensätze. |
| `abrechnungsfaehige_tage` | string | ja |  |  | Abrechenbare Tage pro Jahr = arbeitstage × billable_ratio, gerundet auf 1 Nachkommastelle. |
| `arbeitstage` | integer | ja |  |  | Verfügbare Arbeitstage pro Jahr = 365 − 104 Wochenendtage − 10 Feiertage − urlaubstage − 10 Krankheitstage, mindestens 1. |
| `marktvergleich` | string | ja |  |  | 'unter', 'im' oder 'ueber' Marktdurchschnitt |
| `durchschnitt_markt` | string | ja |  |  | 104 EUR Marktdurchschnitt |
