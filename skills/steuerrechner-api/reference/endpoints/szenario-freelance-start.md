# Bundle: Freelance-Start EU vs GmbH

`POST /v1/szenario/freelance-start`

Kategorie: Szenario-Bundles

Vergleicht die Gesamtsteuerbelastung eines Gewinns als Einzelunternehmer (ESt + Soli + KiSt + GewSt mit §35 EStG-Anrechnung) und als Kapitalgesellschaft (KSt + Soli + GewSt + KapESt auf Ausschuettung). Liefert eine Netto-Empfehlung.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `gewinn_jahr` | number | ja |  |  | Erwarteter Jahresgewinn vor Steuern in EUR |
| `hebesatz_gewerbesteuer` | integer |  | 400 |  | Gewerbesteuer-Hebesatz der Gemeinde in Prozent (§ 16 GewStG) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (Kirchensteuersatz: 8 % BY/BW, 9 % uebrige) |
| `kirchenmitglied` | boolean |  | false |  | Kirchensteuerpflichtig |
| `zusammenveranlagung` | boolean |  | false |  | Zusammenveranlagung mit Ehe-/Lebenspartner (Splittingtarif, § 32a EStG) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `gewinn_jahr` | string | ja |  |  | Jahresgewinn in EUR aus der Anfrage. Dient beim Einzelunternehmen direkt als zu versteuerndes Einkommen und bei der GmbH als Gewinn vor Steuern. |
| `eu_est` | string | ja |  |  | Einkommensteuer des Einzelunternehmers in EUR nach Grundtarif bzw. Splitting (zusammenveranlagung), gerechnet auf gewinn_jahr als zvE. Ohne Abzug von Vorsorgeaufwendungen und ohne Minderung durch § 35 EStG. |
| `eu_soli` | string | ja |  |  | Solidaritätszuschlag in EUR auf eu_est, aus dem Einkommensteuer-Tarif-Rechner. |
| `eu_kirchensteuer` | string | ja |  |  | Kirchensteuer in EUR auf eu_est nach dem Satz des Bundeslands. 0, wenn kirchenmitglied=false. |
| `eu_gewerbesteuer` | string | ja |  |  | Gewerbesteuer des Einzelunternehmens in EUR nach Abzug der Anrechnung (Faktor 4 × Messbetrag, höchstens die Gewerbesteuer). Bei Hebesatz bis 400 % meist 0. |
| `eu_gesamt_belastung` | string | ja |  |  | Summe der Steuern des Einzelunternehmens in EUR: eu_est + eu_soli + eu_kirchensteuer + eu_gewerbesteuer. |
| `eu_netto` | string | ja |  |  | Gewinn nach Steuern beim Einzelunternehmen in EUR: gewinn_jahr − eu_gesamt_belastung. Ohne Sozialversicherung. |
| `eu_effektiv_prozent` | string | ja |  |  | Effektive Steuerbelastung des Einzelunternehmens in Prozent des Gewinns (32.12 = 32,12 %). 0, wenn gewinn_jahr 0 ist. |
| `gmbh_koerperschaftsteuer` | string | ja |  |  | Körperschaftsteuer der GmbH in EUR: 15 % des Gewinns. |
| `gmbh_soli` | string | ja |  |  | Solidaritätszuschlag auf die Körperschaftsteuer in EUR: 5,5 %, ohne Freigrenze. |
| `gmbh_gewerbesteuer` | string | ja |  |  | Gewerbesteuer der GmbH in EUR mit dem Hebesatz der Anfrage, ohne Freibetrag und ohne Anrechnung. |
| `gmbh_kapest_auf_ausschuettung` | string | ja |  |  | Steuer auf die Ausschüttung in EUR: Kapitalertragsteuer + Soli + ggf. Kirchensteuer auf den vollständig ausgeschütteten Gewinn nach KSt, Soli und GewSt. Ohne Sparer-Pauschbetrag. |
| `gmbh_gesamt_belastung` | string | ja |  |  | Gesamtsteuer der GmbH-Variante in EUR bei 100 % Ausschüttung: KSt + Soli + GewSt + Steuer auf die Ausschüttung. |
| `gmbh_netto` | string | ja |  |  | Netto beim Gesellschafter in EUR: gewinn_jahr − gmbh_gesamt_belastung, bei voller Ausschüttung. Ohne Geschäftsführergehalt und Sozialversicherung. |
| `gmbh_effektiv_prozent` | string | ja |  |  | Effektive Steuerbelastung der GmbH-Variante in Prozent des Gewinns. 0, wenn gewinn_jahr 0 ist. |
| `empfehlung` | string | ja |  |  | Text, welche Variante mehr Netto bringt und um wie viel EUR (Vergleich eu_netto gegen gmbh_netto bei voller Ausschüttung). Bei Gleichstand wird die GmbH genannt. |
| `hinweise` | array<string> | ja |  |  | Liste fester Texte: Bundle-Herkunft, Bezug auf 100 % Ausschüttung und nicht berechnete Faktoren wie Haftung und Sozialversicherung. |
