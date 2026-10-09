# 3-Topf-Verlustverrechnung (Aktien / Sonstige / §23 Krypto)

`POST /v1/verlustverrechnung`

Kategorie: Verlustverrechnung

Berechnet die getrennte Verlustverrechnung in den drei steuerlichen Toepfen nach §20 Abs. 6 EStG (Aktien-Topf, Sonstiger Topf) und §23 EStG (Krypto/PrivVG-Topf). Beruecksichtigt Sparer-Pauschbetrag (1.000 / 2.000 EUR), §23-Freigrenze (1.000 EUR), Verlustvortraege aus Vorjahren und das BVerfG-Verfahren 2 BvL 3/21 zur Aktien-Topf-Beschraenkung. Liefert eine Schaetzung der Steuer-Ersparnis durch die Verlustverrechnung im Vergleich zu einer naiven Berechnung ohne Verluste.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `aktien_gewinne_ytd` | number |  | "0" |  | Realisierte Gewinne aus Aktien-Verkaeufen YTD in EUR |
| `aktien_verluste_ytd` | number |  | "0" |  | Realisierte Verluste aus Aktien-Verkaeufen YTD in EUR (positiv eintragen) |
| `aktien_verlustvortrag` | number |  | "0" |  | Verlustvortrag im Aktien-Topf aus Vorjahren in EUR (positiv eintragen) |
| `sonstige_gewinne_ytd` | number |  | "0" |  | Gewinne im Sonstigen Topf YTD (ETF, Anleihen, Zinsen, Dividenden, Termingeschaefte) in EUR |
| `sonstige_verluste_ytd` | number |  | "0" |  | Verluste im Sonstigen Topf YTD in EUR (positiv eintragen) |
| `sonstige_verlustvortrag` | number |  | "0" |  | Verlustvortrag im Sonstigen Topf aus Vorjahren in EUR (positiv eintragen) |
| `krypto_gewinne_ytd` | number |  | "0" |  | §23 EStG Krypto/PrivVG-Gewinne in der Haltefrist YTD in EUR |
| `krypto_verluste_ytd` | number |  | "0" |  | §23 EStG Krypto/PrivVG-Verluste YTD in EUR (positiv eintragen) |
| `krypto_verlustvortrag` | number |  | "0" |  | §23 EStG Verlustvortrag aus Vorjahren in EUR (positiv eintragen) |
| `veranlagungszeitraum` | integer |  | 2026 |  | Veranlagungszeitraum (fuer AKTIEN_TOPF_AKTIV-Feature-Flag) |
| `sparer_pauschbetrag_verfuegbar` | number |  | "1000" |  | Verfuegbarer Sparer-Pauschbetrag in EUR (1000 Einzel, 2000 Zusammen). Reduziert um bereits an anderer Stelle einbehaltenen Anteil. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `aktien_topf_saldo` | string | ja |  |  | Saldo Aktien-Topf in EUR (negativ = gefangener Verlust, sonst 0) |
| `aktien_topf_vortrag_neu` | string | ja |  |  | Verbleibender Aktien-Verlustvortrag in Folgejahr in EUR (immer >= 0) |
| `aktien_in_sonstige_geflossen` | string | ja |  |  | Positiver Aktien-Saldo, der in den Sonstigen Topf gemerged wurde (bei BVerfG-Aufhebung auch negative Werte moeglich) |
| `sonstiger_topf_saldo` | string | ja |  |  | Saldo Sonstiger Topf in EUR (vor Sparer-Pauschbetrag) |
| `sonstiger_topf_vortrag_neu` | string | ja |  |  | Verbleibender Sonstiger-Verlustvortrag in Folgejahr in EUR (immer >= 0) |
| `krypto_topf_saldo` | string | ja |  |  | §23 EStG Saldo in EUR (positiv vor Freigrenze, negativ = Verlust-Vortrag) |
| `krypto_topf_vortrag_neu` | string | ja |  |  | Verbleibender §23 Verlustvortrag in Folgejahr in EUR (immer >= 0) |
| `krypto_freigrenze_greift` | boolean | ja |  |  | True wenn §23 Saldo > 0 aber unter 1.000 EUR Freigrenze |
| `sparer_pauschbetrag_verfuegbar` | string | ja |  |  | Angesetzter Sparer-Pauschbetrag in EUR (Eingabe, Default 1.000 für Einzelveranlagung, maximal 2.000). Wird nur gegen den Sonstigen Topf verrechnet. |
| `sparer_pauschbetrag_verbraucht` | string | ja |  |  | An den Sonstigen Topf angerechneter Betrag in EUR |
| `sparer_pauschbetrag_rest` | string | ja |  |  | Nicht verbrauchter Teil des Sparer-Pauschbetrags in EUR (verfügbar minus verbraucht). Entspricht dem vollen verfügbaren Betrag, wenn der Sonstige Topf nicht positiv ist. |
| `steuerpflichtige_kapitalertraege` | string | ja |  |  | Steuerpflichtiger §20-Endsaldo nach SP-Anrechnung in EUR |
| `steuerpflichtige_krypto` | string | ja |  |  | Steuerpflichtiger §23-Krypto-Gewinn in EUR (0 wenn Freigrenze greift) |
| `aktien_topf_aktiv` | boolean | ja |  |  | Status §20 Abs. 6 Satz 4 EStG (False nach BVerfG-Aufhebung) |
| `bverfg_hinweis` | string | ja |  |  | Hinweis-Text zum §165 AO-Vorlaeufigkeitsvermerk (None wenn nicht relevant) |
| `ersparnis_vs_naive` | string | ja |  |  | Geschaetzte Steuer-Ersparnis durch Verlustverrechnung in EUR (Vergleichssatz 26,375 % KapESt+Soli, ohne KiSt; nur §20-Welt) |
| `veranlagungszeitraum` | integer | ja |  |  | Echo des Veranlagungsjahres (2018–2030, Default aktuelles Steuerjahr). Ist nur für den Aktien-Topf-Schalter vorgesehen und verändert das Ergebnis derzeit nicht. |
| `rechtsgrundlage` | string | ja |  |  | Fester Text mit den angewendeten Normen und dem BVerfG-Aktenzeichen, gleich für jede Anfrage. |
