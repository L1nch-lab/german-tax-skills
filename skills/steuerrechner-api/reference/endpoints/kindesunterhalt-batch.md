# Kindesunterhalt-Batch (max 1.000 Faelle)

`POST /v1/kindesunterhalt/batch`

Kategorie: Kindesunterhalt, Batch

Berechnet den Kindesunterhalt nach Duesseldorfer Tabelle 2026 fuer bis zu 1.000 Faelle in einem Aufruf – z.B. fuer Kanzlei-Fallisten oder Einkommens-Sweeps ueber die Tabellenstufen. Per-Item-Error-Isolation analog /v1/brutto-netto/batch.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<KindesunterhaltRequest> | ja |  |  | Liste der Kindesunterhalt-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "kinder": [
        {
          "altersstufe": 1
        },
        {
          "altersstufe": 2
        }
      ],
      "kindergeld_empfaenger": "berechtigt",
      "nettoeinkommen": "3500"
    },
    {
      "erwerbstaetig": false,
      "kinder": [
        {
          "altersstufe": 3
        }
      ],
      "kindergeld_empfaenger": "berechtigt",
      "nettoeinkommen": "1800"
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<KindesunterhaltBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
