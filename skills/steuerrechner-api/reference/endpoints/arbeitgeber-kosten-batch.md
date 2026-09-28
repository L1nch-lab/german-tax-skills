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
| `items` | array<ArbeitgeberKostenBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
