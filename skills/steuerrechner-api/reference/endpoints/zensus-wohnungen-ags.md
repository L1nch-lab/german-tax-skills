# Zensus-2022-Wohnungskennzahlen einer Gemeinde

`GET /v1/zensus/wohnungen/{ags}`

Kategorie: Zensus 2022

Liefert die Wohnungskennzahlen des Zensus 2022 (Stichtag 15.05.2022) fuer eine Gemeinde: durchschnittliche Nettokaltmiete je qm, Leerstandsquote, Eigentuemerquote, durchschnittliche Wohnflaeche je Wohnung sowie die Nutzungs-Zaehler (bewohnt, vermietet, Ferienwohnung, leerstehend). Dazu dieselben Kennzahlen fuer Kreis, Bundesland und Bund als Einordnung. Achtung: Bestandsmieten aus einer Vollerhebung, keine Angebotsmieten und kein Mietspiegel. Werte mit sehr kleiner Fallzahl sind ueber *_unsicher = true gekennzeichnet.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | path | string | ja |  |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  | Gemeinde-AGS (8-stellig) der Anfrage |
| `name` | string | ja |  |  | Gemeindename laut Zensus 2022 |
| `stichtag` | string | ja |  |  | Stichtag des Zensus (2022-05-15) |
| `gemeinde` | ZensusWohnungenKennzahlen | ja |  |  | Kennzahlen der Gemeinde |
| `vergleich` | array<ZensusWohnungenGebiet> |  |  |  | Einordnung: Kreis, Bundesland und Bund mit denselben Kennzahlen |
| `quelle` | string | ja |  |  | Datenquelle |
| `hinweis` | string |  | "Zensus 2022, Stichtag 15.05.2022: BESTANDSMIETEN aller vermieteten Wohnungen, nicht die aktuellen Angebotsmieten der Immobilienportale und kein Mietspiegel im Sinne der §§ 558c f. BGB. Fuer die ortsuebliche Vergleichsmiete ist der Mietspiegel der Gemeinde massgeblich. Zum Schutz von Einzelangaben ueberlagert das Verfahren nach § 16 BStatG (Cell-Key) die Fallzahlen leicht; Summen koennen deshalb abweichen. Werte mit *_unsicher = true beruhen auf sehr kleinen Fallzahlen." |  |  |
