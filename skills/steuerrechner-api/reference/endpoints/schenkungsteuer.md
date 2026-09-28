# Schenkungsteuer-Rechner (ErbStG)

`POST /v1/schenkungsteuer`

Kategorie: Schenkungsteuer

Berechnet die Schenkungsteuer nach ErbStG. Beruecksichtigt Steuerklassen I-III, persoenliche Freibetraege (20.000-500.000 EUR) und progressive Steuersaetze (7-50 %). Versorgungsfreibetraege nach §17 ErbStG entfallen bei Schenkungen. Freibetraege sind alle 10 Jahre erneut nutzbar (§14 ErbStG). Liefert einen Vergleich aller Verwandtschaftsgrade.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `wert` | number | ja |  |  | Wert der Schenkung in EUR |
| `verwandtschaft` | enum | ja |  | Ehegatte / Lebenspartner, Kind, Enkel (Elternteil lebt), Enkel (Elternteil verstorben), Urenkel, Eltern / Grosseltern, Geschwister, Nichte / Neffe, Stiefeltern, Schwiegerkinder / -eltern, Geschiedener Ehegatte, Nicht verwandt | Verwandtschaftsverhaeltnis zum Schenker |

Beispiel:

```json
{
  "verwandtschaft": "Kind",
  "wert": 500000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `steuerklasse` | string | ja |  |  | ErbSt-Steuerklasse (I, II oder III) |
| `freibetrag` | string | ja |  |  | Persoenlicher Freibetrag in EUR (§16 ErbStG) |
| `steuerpflichtiger_erwerb` | string | ja |  |  | Steuerpflichtiger Erwerb in EUR |
| `steuersatz` | string | ja |  |  | Angewendeter Steuersatz in Prozent |
| `steuer` | string | ja |  |  | Schenkungsteuer in EUR |
| `effektiv_prozent` | string | ja |  |  | Effektiver Steuersatz bezogen auf Gesamtwert in % |
| `netto` | string | ja |  |  | Netto nach Steuer in EUR |
| `vergleich` | array<SchenkungsteuerVergleichItem> | ja |  |  | Steuervergleich fuer alle Verwandtschaftsgrade |
