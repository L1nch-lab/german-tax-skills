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
| `basis_elterngeld_monat` | string | ja |  |  | Basiselterngeld in EUR/Monat aus dem Elterngeld-Rechner (berechne_elterngeld) auf Basis von nettoeinkommen_monat, begrenzt auf die Code-Konstanten 300 bis 1800. Ausgegeben wird das Feld basiselterngeld ohne Geschwisterbonus und Mehrlingszuschlag; die Eingaben geschwisterbonus und erwartete_kinder ändern diesen Wert daher nicht. |
| `elterngeld_plus_monat` | string | ja |  |  | ElterngeldPlus in EUR/Monat aus berechne_elterngeld: halbes rohes Basiselterngeld, begrenzt auf die Code-Konstanten 150 bis 900. Wie beim Basiselterngeld ohne Geschwisterbonus und Mehrlingszuschlag. |
| `bezugsmonate_basis` | integer | ja |  |  | Bezugsdauer des Basiselterngelds in Monaten, fest 14 (12 plus 2 Partnermonate laut Code-Kommentar), unabhängig von der Eingabe. |
| `bezugsmonate_plus` | integer | ja |  |  | Bezugsdauer des ElterngeldPlus in Monaten, fest 28 (24 plus 4 Partnermonate laut Code-Kommentar), unabhängig von der Eingabe. |
| `kindergeld_monat` | string | ja |  |  | Kindergeld für alle Kinder in EUR/Monat: (anzahl_kinder_aktuell + erwartete_kinder) × fester Satz pro Kind. Der Satz ist die Konstante KINDERGELD_PRO_KIND im Szenario-Router (255) und kommt nicht aus dem Kindergeld- oder Kindesunterhalt-Modul. |
| `stkl_aktuell_netto` | string | ja |  |  | DEPRECATED (2026.52): irrefuehrend benannt, der Wert ist nicht die aktuelle Steuerklasse. Identisch mit stkl_vergleich_netto. Wird in einer kuenftigen API-Version entfernt. |
| `stkl_vergleich_netto` | string | ja |  |  | Vergleichsbasis der Steuerklassen-Empfehlung. Mit Partner: gemeinsames Monatsnetto beider Partner in EUR in der ungünstigeren der zwei Varianten III/V und IV/IV aus dem Steuerklassen-Vergleich (berechne_steuerklassen_vergleich). Ohne Partner (partner_brutto_monat = 0): unverändert nettoeinkommen_monat aus der Eingabe. |
| `stkl_empfehlung` | string | ja |  |  | Empfehlungstext aus dem Steuerklassen-Vergleich (III/V gegen IV/IV, Partner 1 mit brutto_monat in III), inklusive der gerundeten Jahresdifferenz; bei weniger als 120 EUR Jahresdifferenz ein Hinweis auf IV/IV. Ohne Partner ein fester Text, dass der Vergleich entfällt. |
| `stkl_empfehlung_netto` | string | ja |  |  | Gemeinsames Monatsnetto beider Partner in EUR in der günstigeren Variante (III/V oder IV/IV). Ohne Partner gleich nettoeinkommen_monat. Bei einer Jahresdifferenz unter 120 EUR kann der Text in stkl_empfehlung IV/IV nennen, obwohl dieser Wert zu III/V gehört. |
| `stkl_ersparnis_jahr` | string | ja |  |  | Netto-Vorteil der günstigeren gegenüber der ungünstigeren Steuerklassen-Kombination in EUR/Jahr: (stkl_empfehlung_netto − stkl_aktuell_netto) × 12. Bezieht sich nur auf den Lohnsteuerabzug, eine spätere Nachzahlung in der Veranlagung ist nicht eingerechnet. 0 ohne Partner. |
| `hinweise` | array<string> | ja |  |  | Liste von Hinweistexten: Basis-Elterngeld und ElterngeldPlus mit Bezugsmonaten, Kinderzahl × Kindergeldsatz, und ohne Partner ein Hinweis, dass die Steuerklassen-Empfehlung das Partner-Brutto braucht. |
