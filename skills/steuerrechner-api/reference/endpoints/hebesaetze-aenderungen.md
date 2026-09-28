# Aenderungs-Feed: geaenderte Hebesaetze seit einem Datum

`GET /v1/hebesaetze-aenderungen`

Kategorie: Hebesaetze-Historie

Liefert alle Gemeinden, deren Hebesatz zu einem Stichtag NACH `since` als geaendert gemeldet wurde (GENESIS 71231-02-01-5, Stichtag jeweils 30.06.; der Datensatz ist halbjahresscharf, nicht tagesscharf). Je Zeile alter Satz aus dem Realsteuervergleich des Vorjahres, neuer Satz und Delta. Leere Liste statt 404, wenn nichts anliegt. `data.stand` nennt den juengsten Stichtag: beim naechsten Aufruf als `since` zurueckgeben, dann kommt nur Neues. Sortierung stichtag, steuerart, ags; `truncated` zeigt weitere Seiten an (`offset` hochzaehlen). Ein Delta von 0 heisst: der Realsteuervergleich des Vorjahres fuehrte den Satz bereits.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `since` | query | string | ja | ISO-Datum (YYYY-MM-DD), exklusiv: geliefert werden Stichtage danach. Pflicht. Fuer den Vollbestand ein Datum vor dem ersten Stichtag setzen. |
| `bundesland` | query | string |  | Kuerzel (NW, BY, ...) oder voller Name (Nordrhein-Westfalen). Optional. |
| `steuerart` | query | enum |  | Auf eine Steuerart eingrenzen. Optional. Werte: GewSt, GrundstA, GrundstB, GrundstC |
| `limit` | query | integer |  | Treffer je Antwort (1-5000, Default 1000). |
| `offset` | query | integer |  | Startposition fuer Folgeseiten (0 bis 1.000.000, Default 0). |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `since` | string | ja |  |  | Angefragte Untergrenze (exklusiv) |
| `stand` | string | ja |  |  | Juengster Stichtag im Datensatz; beim naechsten Aufruf als since senden |
| `anzahl_gesamt` | integer | ja |  |  | Treffer insgesamt (ohne limit/offset) |
| `anzahl` | integer | ja |  |  | Treffer in dieser Antwort |
| `limit` | integer | ja |  |  |  |
| `offset` | integer | ja |  |  |  |
| `truncated` | boolean | ja |  |  | True, wenn nach dieser Seite weitere Treffer folgen |
| `eintraege` | array<HebesatzAenderungItem> | ja |  |  |  |
