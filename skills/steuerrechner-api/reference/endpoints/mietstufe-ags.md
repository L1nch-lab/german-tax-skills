# Wohngeld-Mietenstufe einer Gemeinde

`GET /v1/mietstufe/{ags}`

Kategorie: Gemeinde-Daten

Liefert die Wohngeld-Mietenstufe (I-VII / 1-7) einer Gemeinde nach der Anlage zur Wohngeldverordnung (gueltig ab 01.01.2023). Nutzbar zum Vorbelegen des Mietstufe-Felds im Wohngeld-Rechner.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | path | string | ja |  |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  |  |
| `mietstufe` | integer | ja |  |  | Wohngeld-Mietenstufe I-VII (1-7) |
| `mietstufe_roman` | string | ja |  |  | Mietenstufe als roemische Ziffer (I-VII) |
| `gueltig_ab` | string |  | "2023-01-01" |  | WoGV-Fassung gueltig ab |
| `quelle` | string |  | "wogv_anlage" |  |  |
