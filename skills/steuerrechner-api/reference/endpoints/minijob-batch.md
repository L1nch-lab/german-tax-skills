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
| `items` | array<MinijobBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
