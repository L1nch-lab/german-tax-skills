# Teilzeit-Rechner (Netto-Vergleich Vollzeit vs. Teilzeit)

`POST /v1/teilzeit`

Kategorie: Teilzeit

Vergleicht Vollzeit- und Teilzeit-Netto nebeneinander: Das Teilzeit-Brutto wird anteilig aus den Wochenstunden abgeleitet, beide Gehaelter laufen durch dieselbe Lohnsteuer-/SV-Logik wie /v1/brutto-netto (PAP, SV-Beitraege 2026). Wegen der Steuerprogression sinkt das Netto langsamer als die Stunden – die Netto-Quote liegt ueber der Stunden-Quote. Detailaufstellung der Abzuege liefert /v1/brutto-netto.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_vollzeit` | number | ja |  |  | Monatliches Bruttogehalt bei Vollzeit in EUR |
| `stunden_vollzeit` | number | ja |  |  | Wochenstunden bei Vollzeit (z.B. 40), mindestens 1 |
| `stunden_teilzeit` | number | ja |  |  | Gewuenschte Wochenstunden in Teilzeit (mindestens 1, max. Vollzeit-Stunden) |
| `steuerklasse` | enum | ja |  | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (Kirchensteuer-Satz, Sachsen-PV). Akzeptiert ISO-Codes (BW, BY, ...). |
| `kirchensteuer` | boolean |  | false |  | True wenn Kirchensteuer abzufuehren ist |
| `kinder` | integer |  | 0 |  | Anzahl Kinder (fuer PV-Staffelung) |
| `geburtsjahr` | integer |  | 1985 |  | Geburtsjahr (fuer PV-Kinderlos-Zuschlag) |
| `kv_zusatzbeitrag` | number |  | "2.9" |  | KV-Zusatzbeitrag in Prozent. Default ist der durchschnittliche Zusatzbeitragssatz nach § 242a SGB V (2026: 2,9 %). Wer den Satz seiner Kasse kennt, sollte ihn setzen: die Saetze reichen von 2,18 bis 4,39 %. |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_vollzeit` | string | ja |  |  | Monatsbrutto Vollzeit in EUR |
| `brutto_teilzeit` | string | ja |  |  | Anteiliges Monatsbrutto Teilzeit (Stunden-Quote) in EUR |
| `netto_vollzeit` | string | ja |  |  | Monatsnetto Vollzeit in EUR |
| `netto_teilzeit` | string | ja |  |  | Monatsnetto Teilzeit in EUR |
| `netto_diff_monat` | string | ja |  |  | Netto-Einbusse pro Monat in EUR |
| `netto_diff_jahr` | string | ja |  |  | Netto-Einbusse pro Jahr in EUR |
| `stunden_prozent` | string | ja |  |  | Teilzeit-Stunden in % der Vollzeit-Stunden |
| `netto_prozent` | string | ja |  |  | Teilzeit-Netto in % des Vollzeit-Nettos (Progression: > Stunden-Quote) |
| `netto_stundenlohn_vollzeit` | string | ja |  |  | Netto pro Arbeitsstunde bei Vollzeit in EUR |
| `netto_stundenlohn_teilzeit` | string | ja |  |  | Netto pro Arbeitsstunde bei Teilzeit in EUR |
