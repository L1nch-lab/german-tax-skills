# Bundle: Familienplanung (Elterngeld + StKl + Kindergeld)

`POST /v1/szenario/familie`

Kategorie: Szenario-Bundles

Aggregiert Basis-Elterngeld, Elterngeld Plus, Kindergeld-Simulation und eine Steuerklassen-Empfehlung (III/V vs IV/IV) in einem Aufruf. Ideal fuer Familienplanung vor der Geburt.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `nettoeinkommen_monat` | number | ja |  |  | Durchschnittliches Nettoeinkommen des Elterngeld-beziehenden Elternteils vor Geburt in EUR/Monat (Elterngeld-Bemessung, § 2 BEEG) |
| `brutto_monat` | number | ja |  |  | Monatliches Bruttogehalt des ersten Partners in EUR |
| `partner_brutto_monat` | number |  | "0" |  | Monatliches Bruttogehalt des zweiten Partners in EUR (0 = Alleinverdiener; Basis fuer den Steuerklassen-Vergleich) |
| `anzahl_kinder_aktuell` | integer |  | 0 |  | Bereits vorhandene Kinder (fuer Kindergeld-Simulation) |
| `erwartete_kinder` | integer |  | 1 |  | Erwartete Kinder (1 = Einzelkind, 2+ = Mehrlinge/Planung) |
| `geschwisterbonus` | boolean |  | false |  | Geschwisterbonus nach § 2a BEEG (+10 %, min. 75 EUR): weiteres Kind unter 3 Jahren bzw. zwei Kinder unter 6 im Haushalt |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (Kirchensteuersatz, PV-Sachsen-Sonderregel) |
| `kirchenmitglied` | boolean |  | false |  | Kirchensteuerpflichtig |
| `geburtsjahr` | integer |  | 1990 |  | Geburtsjahr (fuer PV-Zuschlag) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `basis_elterngeld_monat` | string | ja |  |  |  |
| `elterngeld_plus_monat` | string | ja |  |  |  |
| `bezugsmonate_basis` | integer | ja |  |  |  |
| `bezugsmonate_plus` | integer | ja |  |  |  |
| `kindergeld_monat` | string | ja |  |  |  |
| `stkl_aktuell_netto` | string | ja |  |  |  |
| `stkl_empfehlung` | string | ja |  |  |  |
| `stkl_empfehlung_netto` | string | ja |  |  |  |
| `stkl_ersparnis_jahr` | string | ja |  |  |  |
| `hinweise` | array<string> | ja |  |  |  |
