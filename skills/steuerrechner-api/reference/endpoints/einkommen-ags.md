# Einkommen je Gemeinde (Gesamtbetrag der Einkuenfte)

`GET /v1/einkommen/{ags}`

Kategorie: Gemeinde-Daten

Zeitreihe des Gesamtbetrags der Einkuenfte (§ 2 Abs. 3 EStG) und der Zahl der Steuerpflichtigen je Gemeinde aus der Lohn- und Einkommensteuerstatistik (GENESIS 73111-01-01-5). WICHTIG: Das ist NICHT das Brutto-/Durchschnittsgehalt und hat 3-4 Jahre Datenlag.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | path | string | ja | 8-stelliger Amtlicher Gemeindeschluessel oder 5-stellige Postleitzahl. Gehoert die PLZ zu mehreren Gemeinden, kommt 409 mit den Kandidaten. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  |  |
| `hinweis` | string |  | "Merkmal ist der Gesamtbetrag der Einkuenfte (§ 2 Abs. 3 EStG), nicht das Bruttoeinkommen. Datenlag typischerweise 3-4 Jahre." |  |  |
| `eintraege` | array<EinkommenGemeindeItem> | ja |  |  |  |
