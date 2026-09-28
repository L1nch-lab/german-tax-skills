# Bundle: Jobwechsel + Abfindung + Arbeitslosigkeit

`POST /v1/szenario/jobwechsel`

Kategorie: Szenario-Bundles

Aggregiert Brutto-Netto (alt + neu), Abfindung mit Fuenftelregel, ALG1-Anspruch und Progressionsvorbehalt-Mehrbelastung in einem Aufruf. Ideal fuer Szenario-Planung bei Arbeitgeberwechsel mit Abfindung und Zwischenarbeitslosigkeit.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `altes_brutto_monat` | number | ja |  |  | Bisheriges monatliches Bruttogehalt in EUR |
| `neues_brutto_monat` | number |  | "0" |  | Neues monatliches Bruttogehalt in EUR (0 = noch kein neuer Job) |
| `abfindung` | number |  | "0" |  | Abfindung in EUR – wird nach der Fuenftelregelung (§ 34 EStG) versteuert (0 = keine Abfindung) |
| `arbeitslos_monate` | integer |  | 0 |  | Monate Arbeitslosigkeit zwischen den Jobs – loest ALG-I-Berechnung inkl. Progressionsvorbehalt (§ 32b EStG) aus |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (Kirchensteuersatz, PV-Sachsen-Sonderregel) |
| `kirchenmitglied` | boolean |  | false |  | Kirchensteuerpflichtig |
| `kinder` | integer |  | 0 |  | Anzahl Kinder |
| `geburtsjahr` | integer |  | 1985 |  | Geburtsjahr (fuer PV-Zuschlag) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `altes_netto_monat` | string | ja |  |  |  |
| `neues_netto_monat` | string | ja |  |  |  |
| `netto_differenz_monat` | string | ja |  |  |  |
| `abfindung_netto_fuenftel` | string | ja |  |  |  |
| `abfindung_netto_normal` | string | ja |  |  |  |
| `abfindung_ersparnis` | string | ja |  |  |  |
| `alg1_monat` | string | ja |  |  |  |
| `alg1_bezugsdauer_monate` | integer | ja |  |  |  |
| `progression_mehrbelastung_jahr` | string | ja |  |  |  |
| `hinweise` | array<string> | ja |  |  |  |
