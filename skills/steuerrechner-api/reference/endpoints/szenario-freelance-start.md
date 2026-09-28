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
| `gewinn_jahr` | string | ja |  |  |  |
| `eu_est` | string | ja |  |  |  |
| `eu_soli` | string | ja |  |  |  |
| `eu_kirchensteuer` | string | ja |  |  |  |
| `eu_gewerbesteuer` | string | ja |  |  |  |
| `eu_gesamt_belastung` | string | ja |  |  |  |
| `eu_netto` | string | ja |  |  |  |
| `eu_effektiv_prozent` | string | ja |  |  |  |
| `gmbh_koerperschaftsteuer` | string | ja |  |  |  |
| `gmbh_soli` | string | ja |  |  |  |
| `gmbh_gewerbesteuer` | string | ja |  |  |  |
| `gmbh_kapest_auf_ausschuettung` | string | ja |  |  |  |
| `gmbh_gesamt_belastung` | string | ja |  |  |  |
| `gmbh_netto` | string | ja |  |  |  |
| `gmbh_effektiv_prozent` | string | ja |  |  |  |
| `empfehlung` | string | ja |  |  |  |
| `hinweise` | array<string> | ja |  |  |  |
