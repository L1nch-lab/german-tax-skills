# Investitionsabzugsbetrag + Sonder-AfA (§ 7g EStG)

`POST /v1/iab`

Kategorie: IAB

Berechnet IAB (bis 50 % der geplanten Anschaffungskosten, max 200.000 EUR pro Betrieb) und Sonder-AfA (40 % verteilbar auf 5 Jahre) nach § 7g EStG. Die 200.000-EUR-Gewinngrenze gilt fuer beide Instrumente, misst aber verschiedene Wirtschaftsjahre: den IAB am Abzugsjahr (Abs. 1 S. 2 Nr. 1 b), die Sonder-AfA am Jahr vor der Anschaffung (Abs. 6 Nr. 1). Dafuer ist gewinn_abzugsjahr optional angebbar. Liefert Jahresplan Jahr 0 (IAB-Bildung) bis Jahr ND (Ende ND) und vergleicht den Liquiditaets-Vorzieheffekt mit reiner linearer AfA.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anschaffungskosten` | number | ja |  |  | Geplante netto Anschaffungskosten in EUR |
| `gewinn_vorjahr` | number | ja |  |  | Gewinn im Wirtschaftsjahr VOR DER ANSCHAFFUNG in EUR. Massgeblich fuer die Sonder-AfA (§ 7g Abs. 6 Nr. 1 EStG). |
| `gewinn_abzugsjahr` | number |  |  |  | Gewinn im Wirtschaftsjahr DES IAB-ABZUGS in EUR, ohne den IAB selbst und ohne Hinzurechnungen. Massgeblich fuer den IAB (§ 7g Abs. 1 S. 2 Nr. 1 Buchst. b EStG). Optional: Ohne Angabe wird gewinn_vorjahr verwendet, das Ergebnis bleibt dann unveraendert. |
| `nutzungsdauer` | integer |  | 8 |  | Nutzungsdauer in Jahren |
| `steuersatz_prozent` | number |  | "35" |  | Marginal-Steuersatz in Prozent |
| `jahre_bis_anschaffung` | integer |  | 1 |  | Jahre zwischen IAB-Bildung und Anschaffung (1-3, § 7g Abs. 3 EStG) |
| `iab_prozent` | number |  | "50" |  | IAB-Quote in Prozent (max 50) |
| `sonder_afa_prozent` | number |  | "40" |  | Sonder-AfA-Quote in Prozent (max 40) |

Beispiel:

```json
{
  "anschaffungskosten": 50000,
  "gewinn_vorjahr": 80000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anschaffungskosten` | string | ja |  |  |  |
| `gewinn_vorjahr` | string | ja |  |  | Gewinn im Jahr vor der Anschaffung (massgeblich fuer die Sonder-AfA) |
| `gewinn_abzugsjahr` | string | ja |  |  | Gewinn im Abzugsjahr (massgeblich fuer den IAB). Ohne eigene Angabe identisch mit gewinn_vorjahr. |
| `nutzungsdauer` | integer | ja |  |  |  |
| `steuersatz_prozent` | string | ja |  |  |  |
| `jahre_bis_anschaffung` | integer | ja |  |  |  |
| `iab_prozent` | string | ja |  |  |  |
| `sonder_afa_prozent` | string | ja |  |  |  |
| `berechtigt` | boolean | ja |  |  | Alias auf berechtigt_iab (Rueckwaertskompatibilitaet) |
| `berechtigt_iab` | boolean | ja |  |  | True wenn der Gewinn im Abzugsjahr <= 200.000 EUR ist (§ 7g Abs. 1 S. 2 Nr. 1 Buchst. b EStG) |
| `berechtigt_sonder_afa` | boolean | ja |  |  | True wenn der Gewinn im Jahr vor der Anschaffung <= 200.000 EUR ist (§ 7g Abs. 6 Nr. 1 EStG) |
| `gewinngrenze` | string | ja |  |  | § 7g-Gewinngrenze 200.000 EUR je Bezugsjahr |
| `iab_betrag` | string | ja |  |  | IAB im Bildungsjahr (auser-bilanziell) |
| `sofort_steuerersparnis` | string | ja |  |  | IAB × Marginal-Steuer im Jahr 0 |
| `hinzurechnung` | string | ja |  |  |  |
| `gemindertes_ak` | string | ja |  |  | AK nach IAB-Hinzurechnung |
| `sonder_afa_betrag` | string | ja |  |  |  |
| `linear_afa_jaehrlich` | string | ja |  |  |  |
| `jahres_plan` | array<IabJahr> | ja |  |  |  |
| `total_steuerersparnis_mit_iab` | string | ja |  |  |  |
| `total_steuerersparnis_nur_linear` | string | ja |  |  |  |
| `liquiditaetsvorteil_jahr_0_1` | string | ja |  |  | Vorzieheffekt Jahre 0+1 vs Nur-Linear |
| `empfehlung` | string | ja |  |  |  |
| `investitionsfrist_jahre` | integer | ja |  |  | 3 Jahre nach IAB-Bildung |
| `iab_prozent_max` | string | ja |  |  | 50 % |
| `sonder_afa_prozent_max` | string | ja |  |  | 40 % |
