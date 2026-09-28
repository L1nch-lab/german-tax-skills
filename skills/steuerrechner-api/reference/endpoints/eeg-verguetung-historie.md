# Time-Series der EEG-Verguetung fuer eine kWp-Klasse

`GET /v1/eeg-verguetung/historie`

Kategorie: EEG-Einspeiseverguetung

Liefert alle bekannten Tarif-Eintraege fuer eine kWp-Klasse + Anlagentyp + Einspeisung, sortiert nach Inbetriebnahme. Coverage 2009-01 bis 2026-07. Nuetzlich fuer Charts oder Vergleich verschiedener Inbetriebnahme-Jahre.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `anlagentyp` | query | string |  | 'pv_dach_wohngebaeude' oder 'pv_dach_sonstige' |
| `kwp` | query | number | ja | Anlagenleistung in kWp |
| `einspeisung` | query | string |  | 'teil' oder 'voll' |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anlagentyp` | string | ja |  |  |  |
| `einspeisung` | string | ja |  |  |  |
| `kw_klasse_min` | string | ja |  |  |  |
| `kw_klasse_max` | string | ja |  |  |  |
| `eintraege` | array<EegHistorieItem> | ja |  |  |  |
