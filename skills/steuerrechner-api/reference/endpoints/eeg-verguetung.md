# EEG-Einspeiseverguetung fuer PV-Anlage (anzulegender Wert + Restlaufzeit)

`GET /v1/eeg-verguetung`

Kategorie: EEG-Einspeiseverguetung

Liefert den anzulegenden Wert in Cent/kWh fuer eine PV-Anlage auf Basis von Inbetriebnahme-Datum, Anlagentyp und Anlagenleistung. Berechnet zusaetzlich Foerderende-Datum und Restlaufzeit in Monaten (20 Jahre Foerderung + Rest des Inbetriebnahmejahres, § 25 EEG 2023). Quelle: BNetzA Archiv VergSaetze. Coverage Phase 3.0: 2024-02-01 bis heute. Aeltere Inbetriebnahmen folgen in Phase 3.1 (SFV-Backfill).

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `inbetriebnahme` | query | string | ja | Inbetriebnahme-Datum der PV-Anlage (YYYY-MM-DD) |
| `anlagentyp` | query | string | ja | 'pv_dach_wohngebaeude' (Privat-EFH/MFH) oder 'pv_dach_sonstige' (Gewerbe / sonstige Gebaeude) |
| `kwp` | query | number | ja | Anlagenleistung in kWp (z.B. 9.8 fuer Privat-PV, 50 fuer KMU-Anlage) |
| `einspeisung` | query | string |  | 'teil' (Teileinspeisung mit Eigenverbrauch) oder 'voll' (Volleinspeisung) |
| `stichtag` | query | string |  | Stichtag fuer Restlaufzeit-Berechnung (default: heute) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `verguetung_ct_per_kwh` | string | ja |  |  | Anzulegender Wert in Cent/kWh, gilt fuer 20 Jahre ab Inbetriebnahme |
| `novelle` | string | ja |  |  | EEG-Novelle, unter der die Anlage gefoerdert wird |
| `novelle_id` | integer | ja |  |  | Interne ID der EEG-Novelle; entspricht dem Feld id in /v1/eeg-novellen. |
| `inbetriebnahme_von` | string | ja |  |  | Anfang des passenden Inbetriebnahme-Intervalls im BNetzA-Tariff |
| `inbetriebnahme_bis` | string | ja |  |  | Ende des Inbetriebnahme-Intervalls |
| `kw_klasse_min` | string | ja |  |  | kWp-Klasse Untergrenze (exklusiv) |
| `kw_klasse_max` | string |  |  |  | kWp-Klasse Obergrenze (inklusiv); null = nach oben offen |
| `anlagentyp` | string | ja |  |  | 'pv_dach_wohngebaeude' \| 'pv_dach_sonstige' |
| `einspeisung` | string | ja |  |  | 'teil' \| 'voll' |
| `verguetungsdauer_jahre` | integer | ja |  |  | 20 Jahre Standard (§ 25 EEG 2023) |
| `gueltig_bis` | string | ja |  |  | Ende der EEG-Foerderung (20 Jahre + Restjahr) |
| `restlaufzeit_monate` | integer | ja |  |  | Volle Monate ab stichtag bis gueltig_bis |
| `quelle_url` | string | ja |  |  | Quelle des Tarif-Eintrags (BNetzA-File-Label) |
| `besonderheit` | string |  |  |  | z.B. 'ausgefoerdert_anschluss' (§ 53 EEG 2021 Anschlussfoerderung) |
