# Kapitalertragsteuer-Batch (max 1.000 Positionen)

`POST /v1/kapitalertragsteuer/batch`

Kategorie: Kapitalertragsteuer, Batch

Berechnet KapESt + Soli + KiSt fuer bis zu 1.000 bereinigte Bemessungsgrundlagen in einem Aufruf – z.B. fuer Depot-Positionslisten oder Mandanten-Sweeps. Per-Item-Error-Isolation analog /v1/brutto-netto/batch.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<KapitalertragsteuerRequest> | ja |  |  | Liste der Kapitalertragsteuer-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "bemessungsgrundlage": "10000",
      "bundesland": "Nordrhein-Westfalen"
    },
    {
      "bemessungsgrundlage": "2500",
      "bundesland": "Bayern",
      "kirchensteuerpflichtig": true
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<KapitalertragsteuerBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
