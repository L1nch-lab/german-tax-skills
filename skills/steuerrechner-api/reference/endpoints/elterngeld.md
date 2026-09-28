# Elterngeld-Rechner (Basis + ElterngeldPlus)

`POST /v1/elterngeld`

Kategorie: Elterngeld

Berechnet Basiselterngeld und ElterngeldPlus nach dem BEEG. Beruecksichtigt gestaffelte Ersatzrate (65-67%), Geschwisterbonus (+10%, min 75 EUR), Mehrlingsbonus (+300 EUR) und optionale Teilzeit waehrend des Bezugs.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `nettoeinkommen_monat` | number | ja |  |  | Durchschnittliches Nettoeinkommen der letzten 12 Monate vor Geburt (EUR) |
| `teilzeit_einkommen` | number |  | "0" |  | Einkommen aus Teilzeit waehrend Elterngeldbezug (EUR, 0 = keine Teilzeit) |
| `geschwisterbonus` | boolean |  | false |  | Geschwisterbonus anwendbar (Kind <3 oder 2 Kinder <6) |
| `mehrlinge` | integer |  | 1 |  | Anzahl gleichzeitig geborener Kinder (1 = kein Mehrling) |

Beispiel:

```json
{
  "nettoeinkommen_monat": 2500
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ersatzrate_prozent` | string | ja |  |  | Angewendete Ersatzrate in Prozent (65-67) |
| `basiselterngeld` | string | ja |  |  | Basiselterngeld pro Monat in EUR (300-1800) |
| `elterngeld_plus` | string | ja |  |  | ElterngeldPlus pro Monat in EUR (150-900) |
| `geschwisterbonus_basis` | string | ja |  |  | Geschwisterbonus Basis in EUR |
| `geschwisterbonus_plus` | string | ja |  |  | Geschwisterbonus Plus in EUR |
| `mehrlingsbonus` | string | ja |  |  | Mehrlingsbonus Basis in EUR |
| `mehrlingsbonus_plus` | string | ja |  |  | Mehrlingsbonus Plus in EUR |
| `basiselterngeld_gesamt` | string | ja |  |  | Basiselterngeld + Boni pro Monat in EUR |
| `elterngeld_plus_gesamt` | string | ja |  |  | ElterngeldPlus + Boni pro Monat in EUR |
| `bezugsmonate_basis` | integer | ja |  |  | Bezugsmonate Basiselterngeld (12+2 Partnermonate) |
| `bezugsmonate_plus` | integer | ja |  |  | Bezugsmonate ElterngeldPlus (24+4 Partnermonate) |
