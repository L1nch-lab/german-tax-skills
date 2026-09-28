# U1-/U2-Umlagesaetze aller Krankenkassen

`GET /v1/gkv/umlagen`

Kategorie: GKV-Umlagen

Liefert je Krankenkasse die Arbeitgeber-Umlagesaetze fuer Lohnfortzahlung (U1, inkl. aller Wahltarife mit Erstattungssatz) und Mutterschaft (U2) aus der SV-Stammdatendatei der GKV-Arbeitsgemeinschaft (ITSG). Optionaler Query-Parameter stichtag=YYYY-MM-DD waehlt den historischen Satz-Block (Daten ab ~2020); ohne Parameter gilt der heutige Tag.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `stichtag` | query | string |  |  |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `stichtag` | string | ja |  |  | Stichtag der Auswahl (YYYY-MM-DD) |
| `stand` | string | ja |  |  | Erstellungsdatum der ITSG-Stammdatendatei (YYYY-MM-DD) |
| `hinweis` | string |  | "U1-/U2-Umlagesaetze nach der SV-Stammdatendatei der GKV-Arbeitsgemeinschaft (ITSG). Der massgebliche U1-Erstattungssatz haengt vom gewaehlten Tarif des Arbeitgebers ab; verbindlich ist die Auskunft der jeweiligen Kasse." |  |  |
| `kassen` | array<GkvUmlagenKasse> | ja |  |  |  |
