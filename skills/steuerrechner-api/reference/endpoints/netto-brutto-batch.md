# Netto-Brutto-Batch (max 200 Zielwerte)

`POST /v1/netto-brutto/batch`

Kategorie: Netto-Brutto, Batch

Ermittelt fuer bis zu 200 Wunsch-Nettos das noetige Brutto in einem Aufruf. Cap 200 statt 1.000, weil jede Zeile eine Bisection ueber den BMF-PAP rechnet. Per-Item-Error-Isolation: unerreichbare Ziel-Nettos werden als calculation_error markiert, der Rest laeuft.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<NettoBruttoRequest> | ja |  |  | Liste der Netto-Brutto-Requests (1 bis 200 Items, Bisection ist teuer) |

Beispiel:

```json
{
  "items": [
    {
      "nettolohn": "2500",
      "steuerklasse": 1
    },
    {
      "kinder": 2,
      "nettolohn": "3200",
      "steuerklasse": 3
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<NettoBruttoBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
