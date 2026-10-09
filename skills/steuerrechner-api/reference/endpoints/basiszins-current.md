# Aktuell gueltiger Basiszinssatz §247 BGB

`GET /v1/basiszins/current`

Kategorie: Basiszinssatz

Liefert den juengsten Basiszinssatz aus der halbjaehrlich gepflegten Reihe (Bundesbank-Pressemitteilung 1.1. + 1.7.). Cache-Control: public, max-age=86400.

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `stichtag` | string | ja |  |  | Geltungsbeginn |
| `satz_prozent` | string | ja |  |  | Basiszinssatz in Prozent |
| `naechste_anpassung_erwartet` | string | ja |  |  | Naechster halbjaehrlicher Anpassungstermin (1.1. oder 1.7.) |
| `rechtsgrundlage` | string |  | "§247 Abs. 1 Satz 1 BGB" |  | Rechtsgrundlage des Satzes als fester Text "§247 Abs. 1 Satz 1 BGB". |
