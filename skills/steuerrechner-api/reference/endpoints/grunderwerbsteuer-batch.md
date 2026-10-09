# Grunderwerbsteuer-Batch (max 1.000 Objekte)

`POST /v1/grunderwerbsteuer/batch`

Kategorie: Grunderwerbsteuer, Batch

Berechnet Grunderwerbsteuer + Kaufnebenkosten fuer bis zu 1.000 Kaufobjekte in einem Aufruf – z.B. fuer Immobilien-Portfolios oder Standort-Vergleiche ueber mehrere Bundeslaender. Per-Item-Error-Isolation analog /v1/brutto-netto/batch.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<GrunderwerbsteuerRequest> | ja |  |  | Liste der Grunderwerbsteuer-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "bundesland": "Bayern",
      "kaufpreis": "300000"
    },
    {
      "bundesland": "Nordrhein-Westfalen",
      "kaufpreis": "450000",
      "mit_makler": true
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<GrunderwerbsteuerBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
