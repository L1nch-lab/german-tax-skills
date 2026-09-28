# Brutto-Netto-Batch (max 1.000 Mitarbeiter)

`POST /v1/brutto-netto/batch`

Kategorie: Brutto-Netto, Batch

Berechnet Brutto→Netto fuer bis zu 1.000 Mitarbeiter in einem Aufruf. Optimiert fuer Lohn-/HR-SaaS-Use-Cases. Per-Item-Error-Isolation: Schlaegt ein Item fehl, werden die anderen Items dennoch berechnet. Antwortet mit `data.items[i].success` als Pro-Item-Status. Top-level `success=True` bedeutet ledigich, dass das Request well-formed war.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<BruttoNettoRequest> | ja |  |  | Liste der Mitarbeiter-Brutto-Netto-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "bruttolohn": "3500",
      "steuerklasse": 1
    },
    {
      "bruttolohn": "5500",
      "kinder": 2,
      "steuerklasse": 3
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<BruttoNettoBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
