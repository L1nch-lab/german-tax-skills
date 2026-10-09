# Einkommensteuer-Batch (max 1.000 zvE-Werte)

`POST /v1/einkommensteuer/batch`

Kategorie: Einkommensteuer, Batch

Berechnet den ESt-Tarif fuer bis zu 1.000 zvE-Werte in einem Aufruf – z.B. fuer Tarif-Tabellen, zvE-Sweeps oder Szenario-Vergleiche. Per-Item-Error-Isolation analog /v1/brutto-netto/batch.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<EinkommensteuerTarifRequest> | ja |  |  | Liste der ESt-Tarif-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "zve": "30000"
    },
    {
      "zusammenveranlagung": true,
      "zve": "60000"
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<EinkommensteuerTarifBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
