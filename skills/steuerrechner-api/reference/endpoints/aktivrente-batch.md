# Aktivrente-Batch (max 1.000 Rentner)

`POST /v1/aktivrente/batch`

Kategorie: Aktivrente, Batch

Berechnet Aktivrente-Steuerersparnis fuer bis zu 1.000 Rentner in einem Aufruf. HR-/Lohnbuero-Use-Case: 'Welche Rentner ueber 63 profitieren wie stark vom Aktivrente-Freibetrag?'. Per-Item-Error-Isolation analog /v1/brutto-netto/batch und /v1/minijob/batch.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<AktivrenteRequest> | ja |  |  | Liste der Rentner-Aktivrente-Requests (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "brutto_rente_monat": 1800,
      "zusatzeinkommen_monat": 1500
    },
    {
      "brutto_rente_monat": 2200,
      "bundesland": "Bayern",
      "kirchensteuer": true,
      "zusatzeinkommen_monat": 2500
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<AktivrenteBatchItemResult> | ja |  |  |  |
| `total_count` | integer | ja |  |  |  |
| `success_count` | integer | ja |  |  |  |
| `error_count` | integer | ja |  |  |  |
