# Bauland-Kaufwerte (Kreisebene) zu einer Gemeinde

`GET /v1/bauland/{ags}`

Kategorie: Bauland

Zeitreihe 1995-2024 der Statistik der Kaufwerte fuer Bauland (GENESIS 61511-01-03-4) auf KREIS-Ebene: Veraeusserungsfaelle, veraeusserte Flaeche, Kaufsumme und durchschnittlicher Kaufwert je qm – jeweils fuer baureifes Land und Bauland insgesamt. Der Kreis wird aus den ersten 5 Stellen der Gemeinde-AGS abgeleitet; dazu die Einordnung gegen Bundesland und Bund im neuesten Jahr mit Kreis-Kaufwert.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | path | string | ja |  |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  | Gemeinde-AGS (8-stellig) der Anfrage |
| `kreis_ags` | string | ja |  |  | Kreis (erste 5 Stellen der Gemeinde-AGS) |
| `eintraege` | array<BaulandJahrItem> | ja |  |  | Kreis-Zeitreihe 1995-2024, je Jahr 2 Zeilen (baureif + insgesamt) |
| `vergleich` | BaulandVergleich |  |  |  | Einordnung gegen Land + Bund (baureifes Land) |
| `quelle` | string | ja |  |  | Datenquelle (GENESIS/Regionalstatistik 61511-01-03-4) |
| `hinweis` | string |  | "Durchschnittswerte tatsaechlicher Verkaufsfaelle (Statistik der Kaufwerte fuer Bauland). In kleinen Kreisen schwanken die Werte stark mit der Fallzahl; gesperrte oder verkaufslose Jahre sind null. Kein Bodenrichtwert und kein Ersatz fuer ein Verkehrswertgutachten." |  |  |
