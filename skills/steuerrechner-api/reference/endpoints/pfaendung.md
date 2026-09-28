# Pfaendungsfreigrenzen-Rechner

`POST /v1/pfaendung`

Kategorie: Pfaendungsfreigrenzen

Berechnet den pfaendbaren und unpfaendbaren Anteil des monatlichen Nettoeinkommens nach §850c ZPO. Beruecksichtigt Unterhaltspflichten (0-5 Personen) und die aktuelle Pfaendungsfreigrenzenbekanntmachung.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `nettoeinkommen` | number | ja |  |  | Monatliches Nettoeinkommen in EUR |
| `unterhaltspflichten` | integer |  | 0 |  | Anzahl unterhaltsberechtigter Personen (0-5). Die Pfaendungstabelle nach §850c ZPO staffelt bis max. 5 Personen. |

Beispiel:

```json
{
  "nettoeinkommen": 2500
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `nettoeinkommen` | string | ja |  |  | Monatliches Nettoeinkommen in EUR |
| `unterhaltspflichten` | integer | ja |  |  | Anzahl unterhaltsberechtigter Personen |
| `grundfreibetrag` | string | ja |  |  | Monatlicher Grundfreibetrag in EUR |
| `erhoehung_unterhalt` | string | ja |  |  | Erhoehung des Freibetrags fuer Unterhaltspflichten in EUR |
| `freibetrag_gesamt` | string | ja |  |  | Gesamter Pfaendungsfreibetrag in EUR |
| `pfaendbarer_betrag` | string | ja |  |  | Pfaendbarer Anteil in EUR |
| `unpfaendbarer_betrag` | string | ja |  |  | Unpfaendbarer Anteil in EUR |
| `pfaendbarer_anteil_zehntel` | integer | ja |  |  | Pfaendbarer Anteil in Zehnteln (7=70% bei 0 UP, 5=50% bei 1 UP, etc.) |
| `anteil_pfaendbar_prozent` | string | ja |  |  | Pfaendbarer Anteil in Prozent |
| `rechtsgrundlage` | string | ja |  |  | Angewendete Rechtsgrundlage |
| `gueltig_ab` | string | ja |  |  | Beginn des Gueltigkeitszeitraums der Tabelle |
| `gueltig_bis` | string | ja |  |  | Ende des Gueltigkeitszeitraums der Tabelle |
| `warnung` | string |  |  |  | Warnung falls die Pfaendungstabelle abgelaufen ist |
