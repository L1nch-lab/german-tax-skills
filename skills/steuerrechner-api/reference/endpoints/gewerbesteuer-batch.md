# Gewerbesteuer-Batch (max 1.000 Faelle)

`POST /v1/gewerbesteuer/batch`

Kategorie: Gewerbesteuer, Batch

Berechnet die Gewerbesteuer fuer bis zu 1.000 Faelle in einem Aufruf – z.B. fuer Multi-Standort-Vergleiche oder Hebesatz-Sweeps ueber viele Gemeinden. Per-Item-Error-Isolation: unbekannte AGS werden als calculation_error markiert, unbekannte oder mehrdeutige PLZ/Gemeindenamen mit PLZ_*/GEMEINDE_* und Kandidaten, der Rest laeuft weiter.

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
| `items` | array<GewerbesteuerBatchItemResult> | ja |  |  | Ein Eintrag je Element des Eingabe-Arrays `items`, in derselben Reihenfolge; `index` (0-basiert) nennt die Position in der Eingabe. |
| `total_count` | integer | ja |  |  | Anzahl der übergebenen Einträge, also die Länge des Eingabe-Arrays `items`; es gilt success_count + error_count = total_count. |
| `success_count` | integer | ja |  |  | Anzahl der Einträge mit `success=true`. |
| `error_count` | integer | ja |  |  | Anzahl der Einträge mit `success=false`. Auch wenn alle Einträge scheitern, antwortet der Endpunkt mit HTTP 200; nur ein Schemafehler im Body führt zu 422 für die ganze Anfrage. |
