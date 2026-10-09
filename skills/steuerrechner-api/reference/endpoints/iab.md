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
| `anschaffungskosten` | string | ja |  |  | Echo der geplanten Netto-Anschaffungskosten in EUR, gerundet auf 2 Nachkommastellen. Bei 0 liefert der Endpunkt ein leeres Ergebnis. |
| `gewinn_vorjahr` | string | ja |  |  | Gewinn im Jahr vor der Anschaffung (massgeblich fuer die Sonder-AfA) |
| `gewinn_abzugsjahr` | string | ja |  |  | Gewinn im Abzugsjahr (massgeblich fuer den IAB). Ohne eigene Angabe identisch mit gewinn_vorjahr. |
| `nutzungsdauer` | integer | ja |  |  | Echo der Nutzungsdauer in Jahren; bestimmt Länge des jahres_plan und linear_afa_jaehrlich. Auch im Leerfall (Anschaffungskosten 0) die Eingabe. |
| `steuersatz_prozent` | string | ja |  |  | Echo des Grenzsteuersatzes in Prozent (Default 35), mit dem alle Steuerwirkungen gerechnet werden. Auch im Leerfall die Eingabe. |
| `jahre_bis_anschaffung` | integer | ja |  |  | Echo der Jahre zwischen IAB-Bildung und Anschaffung (1–3). Wird nur zurückgegeben und fließt nicht in die Rechnung ein, der Plan setzt die Anschaffung immer in Jahr 1. |
| `iab_prozent` | string | ja |  |  | Echo der IAB-Quote in Prozent der Anschaffungskosten (0–50, Default 50). |
| `sonder_afa_prozent` | string | ja |  |  | Echo der Sonder-AfA-Quote in Prozent (0–40, Default 40), angewendet auf die um den IAB geminderten Anschaffungskosten. |
| `berechtigt` | boolean | ja |  |  | Alias auf berechtigt_iab (Rueckwaertskompatibilitaet) |
| `berechtigt_iab` | boolean | ja |  |  | True wenn der Gewinn im Abzugsjahr <= 200.000 EUR ist (§ 7g Abs. 1 S. 2 Nr. 1 Buchst. b EStG) |
| `berechtigt_sonder_afa` | boolean | ja |  |  | True wenn der Gewinn im Jahr vor der Anschaffung <= 200.000 EUR ist (§ 7g Abs. 6 Nr. 1 EStG) |
| `gewinngrenze` | string | ja |  |  | § 7g-Gewinngrenze 200.000 EUR je Bezugsjahr |
| `iab_betrag` | string | ja |  |  | IAB im Bildungsjahr (auser-bilanziell) |
| `sofort_steuerersparnis` | string | ja |  |  | IAB × Marginal-Steuer im Jahr 0 |
| `hinzurechnung` | string | ja |  |  | Hinzurechnung im Anschaffungsjahr in EUR, gleich iab_betrag. Neutralisiert im Modell die gleich hohe Minderung der Anschaffungskosten; 0, wenn kein IAB gebildet wird. |
| `gemindertes_ak` | string | ja |  |  | AK nach IAB-Hinzurechnung |
| `sonder_afa_betrag` | string | ja |  |  | Sonder-AfA in EUR = gemindertes_ak × sonder_afa_prozent / 100, vereinfacht komplett im Anschaffungsjahr angesetzt. 0, wenn berechtigt_sonder_afa false ist. |
| `linear_afa_jaehrlich` | string | ja |  |  | Jährliche lineare AfA in EUR = (gemindertes_ak − sonder_afa_betrag) / nutzungsdauer, gleich in jedem Jahr von 1 bis Nutzungsdauer. |
| `jahres_plan` | array<IabJahr> | ja |  |  | Liste der Jahre 0 bis nutzungsdauer: Jahr 0 IAB-Bildung, Jahr 1 Anschaffung mit Hinzurechnung, Sonder-AfA und linearer AfA, danach nur lineare AfA. Leer im Leerfall. |
| `total_steuerersparnis_mit_iab` | string | ja |  |  | Summe der steuerwirkung aller Planjahre in EUR. Ergibt im Modell Anschaffungskosten × Steuersatz und ist damit bis auf Rundung gleich total_steuerersparnis_nur_linear; der Vorteil liegt nur im Zeitpunkt. |
| `total_steuerersparnis_nur_linear` | string | ja |  |  | Vergleichswert in EUR: Steuerersparnis bei reiner linearer AfA ohne IAB und Sonder-AfA = Anschaffungskosten / Nutzungsdauer × Steuersatz × Nutzungsdauer. |
| `liquiditaetsvorteil_jahr_0_1` | string | ja |  |  | Vorzieheffekt Jahre 0+1 vs Nur-Linear |
| `empfehlung` | string | ja |  |  | Deutscher Hinweistext in Du-Form zur Berechtigung (IAB und Sonder-AfA getrennt) und zur sofortigen Steuerersparnis. Nicht maschinenlesbar. |
| `investitionsfrist_jahre` | integer | ja |  |  | 3 Jahre nach IAB-Bildung |
| `iab_prozent_max` | string | ja |  |  | 50 % |
| `sonder_afa_prozent_max` | string | ja |  |  | 40 % |
