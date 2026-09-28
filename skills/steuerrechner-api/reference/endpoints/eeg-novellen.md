# Liste aller bekannten EEG-Novellen

`GET /v1/eeg-novellen`

Kategorie: EEG-Einspeiseverguetung

Liefert alle in der API hinterlegten EEG-Novellen sortiert nach Gueltigkeit. Aktuelle Coverage: EEG 2017, EEG 2021, EEG 2023. Aeltere folgen in Phase 3.3.

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `novellen` | array<EegNovelleItem> | ja |  |  |  |
