# Minijob-Batch (max 1.000 Mitarbeiter)

`POST /v1/minijob/batch`

Kategorie: Minijob, Batch

Berechnet Minijob/Midijob-Status fuer bis zu 1.000 Mitarbeiter in einem Aufruf. Per-Item-Error-Isolation analog /v1/brutto-netto/batch.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<MinijobRequest> | ja |  |  | Liste der Mitarbeiter-Minijob-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "bruttogehalt": "538"
    },
    {
      "bruttogehalt": "1500",
      "kinderlos_ueber_23": true
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<MinijobBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
