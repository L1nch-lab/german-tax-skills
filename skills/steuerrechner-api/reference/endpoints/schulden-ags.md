# Kommunale Schulden (Kreisebene) zu einer Gemeinde

`GET /v1/schulden/{ags}`

Kategorie: Gemeinde-Daten

Zeitreihe der Schulden des kommunalen Kernhaushalts (GENESIS 71327-Z-01, Stichtag 31.12.) auf KREIS-Ebene. Die Quelle fuehrt Gemeinde-Schulden ueberwiegend nur ueber Amts-/Kreisverbaende, daher liefert der Endpoint den Kreis (erste 5 Stellen der Gemeinde-AGS) samt Schulden je Kreis-Einwohner.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | path | string | ja | 8-stelliger Amtlicher Gemeindeschluessel oder 5-stellige Postleitzahl. Gehoert die PLZ zu mehreren Gemeinden, kommt 409 mit den Kandidaten. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  | Angefragte Gemeinde-AGS (8-stellig) |
| `kreis_ags` | string | ja |  |  | Zugehoeriger Kreis (5-stellig, erste 5 Stellen der AGS) |
| `kreis_einwohner` | integer |  |  |  | Einwohner des Kreises (Summe der Gemeinden), Basis je-Einwohner |
| `hinweis` | string |  | "Schulden auf KREIS-Ebene (Kernhaushalt). Die Quelle 71327-Z-01 fuehrt Gemeinde-Schulden ueberwiegend nur ueber Amts-/Kreisverbaende, daher Kreisebene als sauberer Kontext-Layer." |  | Fester Hinweistext: Die Schulden gelten für den Kreis (Kernhaushalt), weil die Quelle Gemeindeschulden überwiegend nur über Amts- und Kreisverbände führt. |
| `eintraege` | array<SchuldenKreisItem> | ja |  |  | Schuldenstände des Kreises je Jahr (Stichtag 31.12.), aufsteigend nach jahr. |
