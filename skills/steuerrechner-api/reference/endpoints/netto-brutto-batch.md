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
| `items` | array<NettoBruttoBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
