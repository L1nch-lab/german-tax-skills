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
| `items` | array<KindesunterhaltBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
