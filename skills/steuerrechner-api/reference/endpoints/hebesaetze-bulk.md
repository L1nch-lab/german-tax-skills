# Bulk-Hebesatz-Lookup per AGS-Liste

`POST /v1/hebesaetze/bulk`

Kategorie: Hebesaetze

Liefert Hebesaetze fuer bis zu 1000 AGS in einem Request. Nicht gefundene AGS werden unter 'nicht_gefunden' gelistet. Datenquelle: Destatis Realsteuervergleich 2024 (dl-de/by-2-0).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags_liste` | array<string> | ja |  |  | Liste von 8-stelligen Amtlichen Gemeindeschluesseln (max 1000) |

Beispiel:

```json
{
  "ags_liste": [
    "01001000",
    "09162000",
    "11000000"
  ]
}
```
