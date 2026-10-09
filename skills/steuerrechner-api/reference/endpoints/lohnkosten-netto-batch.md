# Lohnkosten-Netto-Batch (max 200 Mitarbeiter)

`POST /v1/lohnkosten-netto/batch`

Kategorie: Lohnkosten-Netto, Batch

Berechnet Lohnkosten-zu-Netto fuer bis zu 1.000 Mitarbeiter in einem Aufruf. Per-Item-Error-Isolation analog /v1/brutto-netto/batch: Items mit unerreichbarem Ziel-Lohnkosten werden als success=False markiert.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<LohnkostenNettoRequest> | ja |  |  | Liste der Mitarbeiter-Lohnkosten-Netto-Requests (1 bis 200 Items) |

Beispiel:

```json
{
  "items": [
    {
      "lohnkosten_ziel": 6000,
      "steuerklasse": 1
    },
    {
      "bundesland": "Bayern",
      "kinder": 2,
      "lohnkosten_ziel": 8000,
      "steuerklasse": 3
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<LohnkostenNettoBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
