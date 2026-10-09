# GWG-Rechner – Sofort vs Sammelposten vs Linear (§ 6 Abs. 2 / 2a EStG)

`POST /v1/gwg`

Kategorie: GWG

Vergleicht die drei Abschreibungs-Optionen fuer ein Wirtschaftsgut: Sofortabschreibung (<= 800 EUR netto, § 6 Abs. 2 EStG), Sammelposten (250,01-1.000 EUR netto auf 5 Jahre verteilt, § 6 Abs. 2a EStG) und regulaere lineare AfA (immer moeglich, § 7 Abs. 1 EStG). Pruefe Klasse und Wahlrecht, ermittle die Methode mit dem groessten Liquiditaets-Vorzieheffekt im Jahr 1.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anschaffungskosten` | number | ja |  |  | Netto-Anschaffungskosten in EUR |
| `nutzungsdauer` | integer |  | 5 |  | Nutzungsdauer in Jahren |
| `steuersatz_prozent` | number |  | "35" |  | Marginal-Steuersatz in Prozent |

Beispiel:

```json
{
  "anschaffungskosten": 600
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anschaffungskosten` | string | ja |  |  | Echo der Netto-Anschaffungskosten in EUR, gerundet auf 2 Nachkommastellen. Entscheidet über kann_sofort und kann_sammelposten. |
| `nutzungsdauer` | integer | ja |  |  | Echo der Nutzungsdauer in Jahren (Default 5); bestimmt nur den linear_plan. |
| `steuersatz_prozent` | string | ja |  |  | Echo des Grenzsteuersatzes in Prozent (Default 35), mit dem alle *_steuer_*-Felder als AfA × Satz / 100 berechnet werden. |
| `kann_sofort` | boolean | ja |  |  | True wenn AK <= 800 EUR (§ 6 Abs. 2 EStG) |
| `kann_sammelposten` | boolean | ja |  |  | True wenn 250,01 <= AK <= 1.000 EUR (§ 6 Abs. 2a EStG) |
| `kann_linear` | boolean | ja |  |  | Immer True (§ 7 Abs. 1 EStG) |
| `klasse_label` | string | ja |  |  | Welche GWG-Klasse das WG erreicht |
| `sofort_plan` | array<GwgJahr> | ja |  |  | Sofort-Abschreibung (leer wenn nicht moeglich) |
| `sammelposten_plan` | array<GwgJahr> | ja |  |  | Sammelposten 5 Jahre (leer wenn nicht moeglich) |
| `linear_plan` | array<GwgJahr> | ja |  |  | Linear nach Nutzungsdauer |
| `sofort_steuer_j1` | string | ja |  |  | Steuerersparnis in EUR im Anschaffungsjahr bei Sofortabschreibung. 0, wenn kann_sofort false ist. |
| `sammel_steuer_j1` | string | ja |  |  | Steuerersparnis in EUR im Anschaffungsjahr beim Sammelposten (1/5 der Anschaffungskosten × Steuersatz). 0, wenn kann_sammelposten false ist. |
| `linear_steuer_j1` | string | ja |  |  | Steuerersparnis in EUR im Anschaffungsjahr bei linearer AfA (Anschaffungskosten / Nutzungsdauer × Steuersatz). |
| `sofort_steuer_5j` | string | ja |  |  | Kumulierte Steuerersparnis der ersten 5 Jahre bei Sofortabschreibung in EUR, gleich sofort_steuer_j1. 0, wenn nicht möglich. |
| `sammel_steuer_5j` | string | ja |  |  | Kumulierte Steuerersparnis der 5 Sammelposten-Jahre in EUR (entspricht Anschaffungskosten × Steuersatz). 0, wenn nicht möglich. |
| `linear_steuer_5j` | string | ja |  |  | Kumulierte Steuerersparnis der ersten 5 Jahre bei linearer AfA in EUR. Bei Nutzungsdauer über 5 Jahre nur ein Teil der Gesamtersparnis. |
| `beste_methode` | string | ja |  |  | Methode mit groesstem Jahr-1-Steuervorteil |
| `beste_steuer_j1` | string | ja |  |  | Höchste Jahr-1-Steuerersparnis in EUR unter den zulässigen Methoden, gehört zu beste_methode. 0 bei ungültiger Eingabe. |
| `empfehlung` | string | ja |  |  | Deutscher Hinweistext in Du-Form passend zu beste_methode (Sofort, Sammelposten oder Linear). Nicht maschinenlesbar. |
| `sofort_grenze` | string | ja |  |  | 800 EUR § 6 Abs. 2 EStG |
| `aufzeichnung_grenze` | string | ja |  |  | 250 EUR ab hier Aufzeichnungspflicht |
| `sammelposten_unter` | string | ja |  |  | 250,01 EUR untere Pool-Grenze |
| `sammelposten_ober` | string | ja |  |  | 1.000 EUR obere Pool-Grenze |
| `sammelposten_jahre` | integer | ja |  |  | 5 Jahre Aufloesung des Sammelpostens |
