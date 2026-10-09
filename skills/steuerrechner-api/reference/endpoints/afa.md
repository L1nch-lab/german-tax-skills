# AfA-Rechner – Linear vs degressiv 2025-2027

`POST /v1/afa`

Kategorie: AfA

Vergleicht lineare AfA (§ 7 Abs. 1 EStG) mit der degressiven Reaktivierung nach § 7 Abs. 2 EStG i.d.F. Wachstumsbooster-Gesetz (Anschaffung 01.07.2025-31.12.2027, Faktor max 3,0 × linear, gedeckelt 30 % p.a.). Erzeugt Jahresplan beider Methoden incl. automatischem Wechsel degressiv -> linear (§ 7 Abs. 3 EStG) und berechnet den Liquiditaets-Vorzieheffekt im persoenlichen Marginal-Steuersatz.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anschaffungskosten` | number | ja |  |  | Netto-Anschaffungskosten in EUR |
| `nutzungsdauer` | integer |  | 8 |  | Betriebsgewoehnliche Nutzungsdauer (AfA-Tabelle BMF) in Jahren |
| `steuersatz_prozent` | number |  | "35" |  | Marginal-Steuersatz (ESt+Soli+KiSt) in Prozent |
| `monat_anschaffung` | integer |  | 1 |  | Anschaffungsmonat 1-12 (Pro-rata-temporis § 7 Abs. 1 Satz 4 EStG) |

Beispiel:

```json
{
  "anschaffungskosten": 25000,
  "nutzungsdauer": 8
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anschaffungskosten` | string | ja |  |  | Echo der Netto-Anschaffungskosten in EUR, auf 2 Nachkommastellen gerundet. Basis beider Abschreibungspläne. |
| `nutzungsdauer` | integer | ja |  |  | Echo der betriebsgewöhnlichen Nutzungsdauer in Jahren. Bestimmt den linearen Satz (100 / Nutzungsdauer) und daraus den degressiven Satz. |
| `steuersatz_prozent` | string | ja |  |  | Echo des Grenzsteuersatzes in Prozent (0–100, Default 35). Damit werden alle Steuerersparnis-Felder als AfA × Satz / 100 berechnet. |
| `monat_anschaffung` | integer | ja |  |  | Echo des Anschaffungsmonats (1–12). Jahr 1 erhält nur den Anteil (13 − Monat) / 12 der Jahres-AfA, der Rest wandert ins Jahr nach Ende der Nutzungsdauer. |
| `afa_satz_linear` | string | ja |  |  | Linearer AfA-Satz in % p.a. |
| `afa_satz_degressiv` | string | ja |  |  | Effektiver degressiver Satz in % (Min(3x linear, 30 %)) |
| `linear_plan` | array<AfaJahrLinear> | ja |  |  | Jahres-Plan lineare AfA |
| `degressiv_plan` | array<AfaJahrDegressiv> | ja |  |  | Jahres-Plan degressive AfA mit Wechsel |
| `afa_jahr_1_linear` | string | ja |  |  | Lineare Abschreibung im Anschaffungsjahr in EUR, inklusive Pro-rata-Kürzung nach monat_anschaffung. 0, wenn kein Plan entsteht. |
| `afa_jahr_1_degressiv` | string | ja |  |  | Degressive Abschreibung im Anschaffungsjahr in EUR (Anschaffungskosten × afa_satz_degressiv, pro rata gekürzt). 0, wenn kein Plan entsteht. |
| `steuer_jahr_1_linear` | string | ja |  |  | ESt-Ersparnis Jahr 1 bei linearer AfA |
| `steuer_jahr_1_degressiv` | string | ja |  |  | ESt-Ersparnis Jahr 1 bei degressiver AfA |
| `vorteil_jahr_1` | string | ja |  |  | Mehrersparnis degressiv minus linear Jahr 1 |
| `steuer_linear_3j` | string | ja |  |  | Kumulierte ESt-Ersparnis linear ueber 3 Jahre |
| `steuer_degressiv_3j` | string | ja |  |  | Kumulierte ESt-Ersparnis degressiv ueber 3 Jahre |
| `liquiditaetsvorteil_3j` | string | ja |  |  | Liquiditaetsvorteil 3 Jahre |
| `summe_afa_linear` | string | ja |  |  | Sanity-Sum: linear ueber gesamte ND (= AK) |
| `summe_afa_degressiv` | string | ja |  |  | Sanity-Sum: degressiv ueber gesamte ND (= AK) |
| `wechsel_jahr` | integer | ja |  |  | Jahr des Wechsels degressiv -> linear (None wenn nie) |
| `empfehlung` | string | ja |  |  | Deutscher Hinweistext in Du-Form: nennt den Mehrvorteil der degressiven AfA in Jahr 1 und über 3 Jahre oder rät zur linearen Methode, wenn kein Vorteil besteht. Nicht maschinenlesbar. |
| `zeitraum_von` | string | ja |  |  | Gueltigkeitsbeginn der degressiven AfA |
| `zeitraum_bis` | string | ja |  |  | Gueltigkeitsende der degressiven AfA |
