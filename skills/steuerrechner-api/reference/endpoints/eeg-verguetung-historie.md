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
| `anlagentyp` | string | ja |  |  | Angefragter Anlagentyp: "pv_dach_wohngebaeude" oder "pv_dach_sonstige". |
| `einspeisung` | string | ja |  |  | Angefragte Einspeiseart: "teil" oder "voll". Die Reihe enthält nur Tarife, die in der Datenbank unter dieser Einspeiseart geführt sind. |
| `kw_klasse_min` | string | ja |  |  | Untergrenze (exklusiv) des kWp-Bereichs, in dem jeder Eintrag der Reihe gilt: die größte Klassen-Untergrenze aller Einträge. |
| `kw_klasse_max` | string | ja |  |  | Obergrenze (inklusiv) des kWp-Bereichs, in dem jeder Eintrag der Reihe gilt: die kleinste Klassen-Obergrenze aller Einträge; null = nach oben offen. |
| `eintraege` | array<EegHistorieItem> | ja |  |  | Alle Tarifeinträge, deren kWp-Klasse den angefragten kWp-Wert enthält, aufsteigend nach Beginn des Inbetriebnahme-Intervalls. |
