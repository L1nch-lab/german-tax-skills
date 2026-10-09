# Bundesbank-Referenzzinssaetze (Bauzins, Tagesgeld, Festgeld, Konsumkredit)

`GET /v1/zinsen`

Kategorie: Zinsen

Effektivzinssaetze aus der MFI-Zinsstatistik der Deutschen Bundesbank (Neugeschaeft Banken DE, private Haushalte, monatlich ab 2003): Wohnungsbaukredite nach Zinsbindung (insgesamt, bis 1 / 1-5 / 5-10 / ueber 10 Jahre), Konsumentenkredite, Tagesgeld und Festgeld bis 1 Jahr. Ohne Parameter: alle Serien mit aktuellstem Monatswert. Mit ?serie=<code>: volle Monats-Historie der Serie.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `serie` | query | string |  |  |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `stand` | string | ja |  |  | Stand des Bundesbank-Exports (YYYY-MM-DD) |
| `hinweis` | string |  | "Effektivzinssaetze der MFI-Zinsstatistik der Deutschen Bundesbank (Neugeschaeft Banken DE, private Haushalte, volumengewichtete Durchschnitte). Individuelle Kredit-/Anlagekonditionen weichen ab." |  | Fester Hinweistext: Effektivzinssätze der MFI-Zinsstatistik der Bundesbank (Neugeschäft, private Haushalte, volumengewichtet); individuelle Konditionen weichen ab. |
| `serien` | array<ZinsSerie> | ja |  |  | Zinsreihen, sortiert nach Serien-Code: ohne Parameter alle Reihen mit nur dem jüngsten Monatswert, mit ?serie= nur diese Reihe mit voller Monatshistorie. |
