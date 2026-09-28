# Firmenwagen-Batch (max 200 Fahrzeuge)

`POST /v1/firmenwagen/batch`

Kategorie: Firmenwagen, Batch

Berechnet geldwerten Vorteil + Netto-Vergleich fuer bis zu 200 Fahrzeuge in einem Aufruf – z.B. fuer Fuhrpark-Analysen oder Antriebsart-Vergleiche. Cap 200 statt 1.000, weil jede Zeile zwei Lohnsteuerlaeufe ueber den BMF-PAP rechnet. Per-Item-Error-Isolation analog /v1/brutto-netto/batch.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<FirmenwagenRequest> | ja |  |  | Liste der Firmenwagen-Requests (1 bis 200 Items, jede Zeile rechnet zwei BMF-PAP-Lohnsteuerlaeufe) |

Beispiel:

```json
{
  "items": [
    {
      "antriebsart": "verbrenner",
      "bruttogehalt": "4000",
      "entfernung_km": 25,
      "listenpreis": "40000"
    },
    {
      "anschaffungsdatum": "2025-09-15",
      "antriebsart": "bev",
      "bruttogehalt": "4000",
      "entfernung_km": 25,
      "listenpreis": "50000"
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<FirmenwagenBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
