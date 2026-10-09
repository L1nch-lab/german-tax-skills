# Midijob-Batch (max 1.000 Mitarbeiter)

`POST /v1/midijob/batch`

Kategorie: Midijob, Batch

Berechnet Midijob fuer bis zu 1.000 Mitarbeiter in einem Aufruf. Per-Item-Error-Isolation analog /v1/brutto-netto/batch: Items ausserhalb des Uebergangsbereichs (603,01 - 2.000 EUR) werden als success=False markiert, andere Items werden trotzdem berechnet.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<MidijobRequest> | ja |  |  | Liste der Mitarbeiter-Midijob-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "brutto_monat": 1000,
      "steuerklasse": 1
    },
    {
      "brutto_monat": 1800,
      "bundesland": "Bayern",
      "kirchensteuer": true,
      "steuerklasse": 5
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<MidijobBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
