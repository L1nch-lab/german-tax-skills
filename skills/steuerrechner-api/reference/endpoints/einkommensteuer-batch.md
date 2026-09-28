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
| `items` | array<EinkommensteuerTarifBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
