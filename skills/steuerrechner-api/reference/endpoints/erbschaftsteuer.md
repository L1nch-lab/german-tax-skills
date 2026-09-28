# Erbschaft- und Schenkungsteuer-Rechner

`POST /v1/erbschaftsteuer`

Kategorie: Erbschaftsteuer

Berechnet die Erbschaftsteuer oder Schenkungsteuer nach ErbStG. Beruecksichtigt Steuerklassen I-III, persoenliche Freibetraege (20.000-500.000 EUR), Versorgungsfreibetraege (§17 ErbStG) und progressive Steuersaetze (7-50%). Liefert einen Vergleich aller Verwandtschaftsgrade.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `wert` | number | ja |  |  | Wert der Erbschaft/Schenkung in EUR |
| `verwandtschaft` | enum | ja |  | Ehegatte / Lebenspartner, Kind, Enkel (Elternteil lebt), Enkel (Elternteil verstorben), Urenkel, Eltern / Grosseltern, Geschwister, Nichte / Neffe, Stiefeltern, Schwiegerkinder / -eltern, Geschiedener Ehegatte, Nicht verwandt | Verwandtschaftsverhaeltnis zum Erblasser/Schenker |
| `modus` | enum |  | "erbschaft" | erbschaft, schenkung | 'erbschaft' oder 'schenkung' (bei Schenkung: kein Versorgungsfreibetrag, Eltern in SK II) |
| `alter_kind` | integer |  |  |  | Alter des Kindes/Enkels (nur fuer Versorgungsfreibetrag bei Erbschaft) |

Beispiel:

```json
{
  "alter_kind": 12,
  "verwandtschaft": "Kind",
  "wert": 500000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `steuerklasse` | string | ja |  |  | ErbSt-Steuerklasse (I, II oder III) |
| `freibetrag` | string | ja |  |  | Persoenlicher Freibetrag in EUR |
| `versorgungsfreibetrag` | string | ja |  |  | Versorgungsfreibetrag in EUR (nur Erbschaft) |
| `freibetrag_gesamt` | string | ja |  |  | Freibetrag gesamt (persoenlich + Versorgung) in EUR |
| `steuerpflichtiger_erwerb` | string | ja |  |  | Steuerpflichtiger Erwerb in EUR |
| `steuersatz` | string | ja |  |  | Angewendeter Steuersatz in Prozent |
| `steuer` | string | ja |  |  | Erbschaft-/Schenkungsteuer in EUR |
| `effektiv_prozent` | string | ja |  |  | Effektiver Steuersatz bezogen auf Gesamtwert in % |
| `netto` | string | ja |  |  | Netto nach Steuer in EUR |
| `modus_label` | string | ja |  |  | 'Erbschaft' oder 'Schenkung' |
| `vergleich` | array<ErbschaftsteuerVergleichItem> | ja |  |  | Steuervergleich fuer alle Verwandtschaftsgrade |
