# Gewerbesteuer-Batch (max 1.000 Faelle)

`POST /v1/gewerbesteuer/batch`

Kategorie: Gewerbesteuer, Batch

Berechnet die Gewerbesteuer fuer bis zu 1.000 Faelle in einem Aufruf – z.B. fuer Multi-Standort-Vergleiche oder Hebesatz-Sweeps ueber viele Gemeinden. Per-Item-Error-Isolation: unbekannte AGS/Gemeindenamen werden als calculation_error markiert, der Rest laeuft weiter.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<GewerbesteuerRequest> | ja |  |  | Liste der Gewerbesteuer-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "gewinn": "100000",
      "hebesatz": 490,
      "rechtsform": "kapitalgesellschaft"
    },
    {
      "gemeinde": "München",
      "gewinn": "100000",
      "rechtsform": "kapitalgesellschaft"
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<GewerbesteuerBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
