# Basiszinssatz §247 BGB fuer einen Stichtag

`GET /v1/basiszins/{stichtag}`

Kategorie: Basiszinssatz

Liefert den am Stichtag gueltigen Basiszinssatz (juengster Eintrag <= Stichtag). Stichtag im Format YYYY-MM-DD, mind. 2002-01-01. Cache-Control: public, max-age=86400.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `stichtag` | path | string | ja | Stichtag im Format YYYY-MM-DD (mind. 2002-01-01) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `stichtag_requested` | string | ja |  |  |  |
| `gueltig_ab` | string | ja |  |  | Geltungsbeginn des verwendeten Satzes |
| `satz_prozent` | string | ja |  |  |  |
| `rechtsgrundlage` | string |  | "§247 Abs. 1 Satz 1 BGB" |  |  |
