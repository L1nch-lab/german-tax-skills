# VL-Rechner – Arbeitnehmer-Sparzulage (§ 13 5. VermBG)

`POST /v1/vl`

Kategorie: VL-Sparzulage

Berechnet die staatliche Arbeitnehmer-Sparzulage auf vermoegenswirksame Leistungen (VL): 20 % auf VL bis 400 EUR/Jahr bei Vermoegensbeteiligungen (max. 80 EUR) bzw. 9 % auf VL bis 470 EUR/Jahr bei Bausparen/wohnwirtschaftlicher Verwendung (max. 42,30 EUR). Anspruch nur bis 40.000 EUR zvE (Einzel) bzw. 80.000 EUR (Zusammenveranlagung, § 13 Abs. 1 5. VermBG). Zusaetzlich Gesamtersparnis ueber die 7-jaehrige Sperrfrist.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `vl_monat` | number | ja |  |  | Monatliche vermoegenswirksame Leistung in EUR (AG- + Eigenanteil) |
| `anlage` | enum |  | "beteiligung" | beteiligung, bausparen | Anlageform: 'beteiligung' (20 % Zulage auf max. 400 EUR/Jahr) oder 'bausparen' (9 % Zulage auf max. 470 EUR/Jahr) |
| `zve` | number |  | "0" |  | Zu versteuerndes Jahreseinkommen in EUR (fuer die Einkommensgrenze). 0 = Grenze wird als eingehalten angenommen. |
| `zusammenveranlagung` | boolean |  | false |  | True -> Einkommensgrenze 80.000 statt 40.000 EUR zvE |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `vl_jahr` | string | ja |  |  | Jaehrliche VL-Einzahlung (vl_monat x 12) in EUR |
| `einkommensgrenze` | string | ja |  |  | Angewendete zvE-Grenze (40.000 Einzel / 80.000 Zusammen) in EUR |
| `anspruch` | boolean | ja |  |  | True wenn zvE innerhalb der Einkommensgrenze liegt |
| `gefoerderter_betrag` | string | ja |  |  | Gefoerderte VL pro Jahr (gedeckelt auf 400 bzw. 470 EUR) |
| `zulagensatz_prozent` | string | ja |  |  | Zulagensatz in Prozent (20 Beteiligung / 9 Bausparen) |
| `sparzulage_jahr` | string | ja |  |  | Arbeitnehmer-Sparzulage pro Jahr in EUR |
| `sparzulage_7jahre` | string | ja |  |  | Summe der Sparzulage ueber die 7-jaehrige Sperrfrist in EUR |
| `eingezahlt_7jahre` | string | ja |  |  | Eigene Einzahlungen ueber die 7-jaehrige Sperrfrist in EUR |
| `ag_zuschuss_hinweis` | boolean | ja |  |  | True wenn VL fliessen – AG-Zuschuss ist haeufig tariflich geregelt |
