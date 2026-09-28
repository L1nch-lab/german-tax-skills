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
| `items` | array<GrunderwerbsteuerBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
