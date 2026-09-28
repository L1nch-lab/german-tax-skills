# Krankenkassenbeitrags-Rechner (KV + PV, §§ 241 ff. SGB V / § 55 SGB XI)

`POST /v1/krankenkassenbeitrag`

Kategorie: Krankenkassenbeitrag

Berechnet Kranken- und Pflegeversicherungsbeitrag mit AN-/AG-Split aus dem Monatsbrutto: KV 14,6 % (bzw. 14,0 % ermaessigt) plus kassenindividueller Zusatzbeitrag, paritaetisch getragen (§ 249 SGB V); PV 3,6 % mit Kinderlosenzuschlag 0,6 (AN allein), Abschlag 0,25 je Kind ab dem 2. bis 5. Kind und Sachsen-Sonderregel (§ 58 Abs. 3 SGB XI). Beitragspflichtiges Entgelt gedeckelt auf die BBG KV/PV 5.812,50 EUR/Monat. Den Zusatzbeitrag einer konkreten Kasse liefert GET /v1/gkv-zusatzbeitrag.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto` | number | ja |  |  | Monatliches Bruttoeinkommen in EUR |
| `zusatzbeitrag` | number |  | "2.9" |  | Kassenindividueller Zusatzbeitrag in % (Durchschnitt 2026: 2,9) |
| `ermaessigt` | boolean |  | false |  | True = ermaessigter KV-Satz 14,0 % ohne Krankengeldanspruch (§ 243 SGB V) |
| `kinderlos` | boolean |  | false |  | True = PV-Kinderlosenzuschlag 0,6 Punkte, traegt der AN allein (§ 55 SGB XI) |
| `kinder` | integer |  | 0 |  | Anzahl Kinder unter 25 (PV-Abschlag 0,25 je Kind ab dem 2. bis 5.) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (Sachsen: AN traegt 1 PV-Punkt mehr, § 58 Abs. 3 SGB XI) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bemessung` | string | ja |  |  | Beitragspflichtiges Entgelt (gedeckelt auf BBG) |
| `bbg_gedeckelt` | boolean | ja |  |  | True wenn das Brutto ueber der BBG KV/PV lag |
| `bbg_monat` | string | ja |  |  | BBG KV/PV 2026: 5.812,50 EUR/Monat |
| `kv_satz` | string | ja |  |  | KV-Basissatz: 14,6 % allgemein / 14,0 % ermaessigt |
| `kv_satz_gesamt` | string | ja |  |  | KV-Basissatz + Zusatzbeitrag in % |
| `kv_an` | string | ja |  |  | KV-Arbeitnehmeranteil in EUR/Monat (haelftig) |
| `kv_ag` | string | ja |  |  | KV-Arbeitgeberanteil in EUR/Monat (haelftig) |
| `pv_satz_gesamt` | string | ja |  |  | Effektiver PV-Gesamtsatz (AN + AG) in % |
| `pv_an_satz` | string | ja |  |  | PV-AN-Satz in % inkl. Kinderlosenzuschlag/Kinder-Abschlag/Sachsen |
| `pv_ag_satz` | string | ja |  |  | PV-AG-Satz in % (nach Kinder-Abschlag) |
| `pv_an` | string | ja |  |  | PV-Arbeitnehmeranteil in EUR/Monat |
| `pv_ag` | string | ja |  |  | PV-Arbeitgeberanteil in EUR/Monat |
| `sachsen` | boolean | ja |  |  | True wenn Sachsen-Sonderregel angewandt wurde |
| `an_gesamt` | string | ja |  |  | Summe AN-Anteil KV+PV in EUR/Monat |
| `ag_gesamt` | string | ja |  |  | Summe AG-Anteil KV+PV in EUR/Monat |
| `gesamt` | string | ja |  |  | Gesamtbeitrag KV+PV (AN+AG) in EUR/Monat |
