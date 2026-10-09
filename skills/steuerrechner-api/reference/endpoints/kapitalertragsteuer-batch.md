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
| `items` | array<KapitalertragsteuerBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
