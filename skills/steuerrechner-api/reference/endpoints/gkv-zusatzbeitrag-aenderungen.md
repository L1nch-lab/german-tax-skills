# Aenderungs-Feed: Zusatzbeitrags-Wechsel aller Kassen seit einem Datum

`GET /v1/gkv-zusatzbeitrag/aenderungen`

Kategorie: GKV-Zusatzbeitrag

Liefert jeden Wechsel des Zusatzbeitrags, der in einem Snapshot NACH `since` erstmals sichtbar war: Kasse, alter Satz, neuer Satz, Delta. `festgestellt_am` ist der erste Snapshot mit dem neuen Satz (Obergrenze des Aenderungsdatums), `letzter_stand_alt` der letzte mit dem alten (Untergrenze). Der erste Snapshot einer Kasse zaehlt nicht als Wechsel. Leere Liste statt 404, wenn nichts anliegt. `data.stand` beim naechsten Aufruf als `since` zurueckgeben. Sortierung festgestellt_am, ik_nummer; `truncated` zeigt weitere Seiten an.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `since` | query | string | ja | ISO-Datum (YYYY-MM-DD), exklusiv: geliefert werden Wechsel, die in Snapshots danach festgestellt wurden. Pflicht. |
| `limit` | query | integer |  | Treffer je Antwort (1-5000, Default 1000). |
| `offset` | query | integer |  | Startposition fuer Folgeseiten (0 bis 1.000.000, Default 0). |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `since` | string | ja |  |  | Angefragte Untergrenze (exklusiv) |
| `stand` | string | ja |  |  | Juengstes Snapshot-Datum im Datensatz; beim naechsten Aufruf als since senden |
| `anzahl_gesamt` | integer | ja |  |  | Wechsel insgesamt (ohne limit/offset) |
| `anzahl` | integer | ja |  |  | Wechsel in dieser Antwort |
| `limit` | integer | ja |  |  |  |
| `offset` | integer | ja |  |  |  |
| `truncated` | boolean | ja |  |  | True, wenn nach dieser Seite weitere Treffer folgen |
| `eintraege` | array<GkvAenderungItem> | ja |  |  |  |
