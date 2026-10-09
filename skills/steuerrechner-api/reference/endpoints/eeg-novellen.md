# Liste aller bekannten EEG-Novellen

`GET /v1/eeg-novellen`

Kategorie: EEG-Einspeiseverguetung

Liefert alle in der API hinterlegten EEG-Novellen sortiert nach Gueltigkeit. Coverage: EEG 2009, EEG 2012, EEG 2014, EEG 2017, EEG 2021, EEG 2023.

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `novellen` | array<EegNovelleItem> | ja |  |  | Alle in der Datenbank hinterlegten EEG-Novellen, aufsteigend nach gueltig_ab sortiert. |
