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
| `items` | array<AktivrenteBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
