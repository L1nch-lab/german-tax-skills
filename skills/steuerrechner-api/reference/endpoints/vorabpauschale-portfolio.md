# Vorabpauschale fuer ein Multi-Fonds-Portfolio (max 1.000 Fonds)

`POST /v1/vorabpauschale/portfolio`

Kategorie: Vorabpauschale

Berechnet die Vorabpauschale nach §18 InvStG fuer bis zu 1.000 Fonds in einem Aufruf. Optimiert fuer Robo-Advisor-Use-Cases (n Kunden × m Fonds × jaehrlich Anfang Januar). Per-Item-Error-Isolation: Schlaegt die Berechnung eines Items fehl (z.B. Jahr ohne BMF-Basiszins, ungueltige Eingabe), werden die anderen Items dennoch berechnet. Antwortet mit `data.items[i].success` als Pro-Item-Status plus aggregiertem `summe_steuerpflichtig` ueber alle erfolgreichen Items. Top-level `success=True` bedeutet lediglich, dass das Request well-formed war (keine 400/422).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<VorabpauschalePortfolioItem> | ja |  |  | Liste der Fonds (1 bis 1000 Items) |

Beispiel:

```json
{
  "items": [
    {
      "fondstyp": "aktien_51",
      "fondswert_jahresanfang": "10000",
      "fondswert_jahresende": "11000",
      "jahr": 2026
    },
    {
      "ausschuettungen": "50",
      "fondstyp": "misch_25",
      "fondswert_jahresanfang": "5000",
      "fondswert_jahresende": "5300",
      "jahr": 2026
    }
  ]
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `items` | array<VorabpauschalePortfolioItemResult> | ja |  |  | Per-Item-Ergebnisse, Reihenfolge entspricht Eingabe |
| `total_count` | integer | ja |  |  | Gesamtzahl Items |
| `success_count` | integer | ja |  |  | Anzahl erfolgreich berechnet |
| `error_count` | integer | ja |  |  | Anzahl mit Fehler |
| `summe_steuerpflichtig` | string | ja |  |  | Summe `vorabpauschale_steuerpflichtig` ueber alle erfolgreichen Items in EUR. Bei error_count > 0 ist die Summe nur ueber die erfolgreichen Items berechnet. |
