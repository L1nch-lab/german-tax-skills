# Arbeitgeber-Kosten-Batch (max 1.000 Mitarbeiter)

`POST /v1/arbeitgeber-kosten/batch`

Kategorie: Arbeitgeber-Kosten, Batch

Berechnet Arbeitgeber-Gesamtkosten fuer bis zu 1.000 Mitarbeiter in einem Aufruf. Per-Item-Error-Isolation analog /v1/brutto-netto/batch.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<ArbeitgeberKostenRequest> | ja |  |  | Liste der Mitarbeiter-AG-Kosten-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "brutto_monat": 5000
    },
    {
      "brutto_monat": 8500,
      "bundesland": "Bayern",
      "u1_satz": "2.5"
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<ArbeitgeberKostenBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
