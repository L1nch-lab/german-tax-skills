# Bundle: Aktien & ETF Komplett-Steuer (VAP + 3-Topf + KapESt mit BL-KiSt)

`POST /v1/szenario/aktien-etf`

Kategorie: Szenario-Bundles

Aggregiert Vorabpauschale (§18 InvStG), 3-Topf-Verlustverrechnung (§20 Abs. 6 EStG + §23 EStG) und echte Kapitalertragsteuer mit bundeslandspezifischer Kirchensteuer (§51a Abs. 2c EStG-Spezialformel) in einem Aufruf. Liefert die tatsaechliche Steuerlast statt der ueberschlaegigen 26,375-%-Pauschale, die viele Online-Rechner ansetzen.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `fondswert_jahresanfang` | number |  | "0" |  | Ruecknahmepreis am ersten Bewertungstag des Jahres in EUR (0 = kein VAP) |
| `fondswert_jahresende` | number |  | "0" |  | Ruecknahmepreis am letzten Bewertungstag des Jahres in EUR |
| `ausschuettungen` | number |  | "0" |  | Im Jahr gezahlte Ausschuettungen in EUR |
| `fondstyp` | enum |  | "aktien_51" | aktien_51, misch_25, sonstige, immo_inland, immo_ausland | Fondsklassifikation fuer Teilfreistellung (§20 InvStG): aktien_51 (30 %), misch_25 (15 %), sonstige (0 %), immo_inland (60 %), immo_ausland (80 %) |
| `aktien_gewinne_ytd` | number |  | "0" |  | Realisierte Gewinne aus Aktien-Verkaeufen YTD in EUR |
| `aktien_verluste_ytd` | number |  | "0" |  | Realisierte Verluste aus Aktien-Verkaeufen YTD in EUR (positiv eintragen) |
| `aktien_verlustvortrag` | number |  | "0" |  | Verlustvortrag im Aktien-Topf aus Vorjahren in EUR (positiv eintragen) |
| `sonstige_gewinne_ytd` | number |  | "0" |  | Gewinne im Sonstigen Topf YTD (ETF-Verkaeufe, Anleihen, Zinsen, Dividenden, Termingeschaefte) in EUR |
| `sonstige_verluste_ytd` | number |  | "0" |  | Verluste im Sonstigen Topf YTD in EUR (positiv eintragen) |
| `sonstige_verlustvortrag` | number |  | "0" |  | Verlustvortrag im Sonstigen Topf aus Vorjahren in EUR (positiv eintragen) |
| `krypto_gewinne_ytd` | number |  | "0" |  | §23 EStG Krypto/PrivVG-Gewinne in der Haltefrist YTD in EUR |
| `krypto_verluste_ytd` | number |  | "0" |  | §23 EStG Krypto/PrivVG-Verluste YTD in EUR (positiv eintragen) |
| `krypto_verlustvortrag` | number |  | "0" |  | §23 EStG Verlustvortrag aus Vorjahren in EUR (positiv eintragen) |
| `sparer_pauschbetrag_verfuegbar` | number |  | "1000" |  | Verfuegbarer Sparer-Pauschbetrag in EUR (1000 Einzelveranlagung, 2000 Zusammenveranlagung) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland fuer die Kirchensteuer-Hoehe (8 % Bayern/Baden-Württemberg, 9 % uebrige Laender) |
| `kirchenmitglied` | boolean |  | false |  | Kirchensteuerpflichtig (8 % BY/BW, 9 % uebrige Laender) |
| `veranlagungszeitraum` | integer |  | 2026 |  | Veranlagungszeitraum (fuer AKTIEN_TOPF_AKTIV-Feature-Flag) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `aktien_topf_saldo` | string | ja |  |  | Saldo Aktien-Topf in EUR (negativ = gefangener Verlust) |
| `aktien_topf_vortrag_neu` | string | ja |  |  | Verbleibender Aktien-Verlustvortrag fuer Folgejahr in EUR |
| `sonstiger_topf_saldo` | string | ja |  |  | Saldo Sonstiger Topf in EUR (vor Sparer-Pauschbetrag, inkl. Aktien-Merger) |
| `sonstiger_topf_vortrag_neu` | string | ja |  |  | Verbleibender Sonstiger-Verlustvortrag fuer Folgejahr in EUR |
| `krypto_topf_saldo` | string | ja |  |  | §23 EStG Saldo in EUR |
| `krypto_topf_vortrag_neu` | string | ja |  |  | Verbleibender §23 Verlustvortrag fuer Folgejahr in EUR |
| `krypto_freigrenze_greift` | boolean | ja |  |  | True wenn §23 Saldo > 0 aber unter 1.000 EUR Freigrenze |
| `vorabpauschale_brutto` | string | ja |  |  | VAP brutto in EUR (vor Teilfreistellung) |
| `vorabpauschale_steuerpflichtig` | string | ja |  |  | VAP nach Teilfreistellung – fliesst in den Sonstigen Topf in EUR |
| `vorabpauschale_keine_vap_grund` | string | ja |  |  | Grund warum keine VAP anfaellt (negativer_basiszins, kein_wertzuwachs, ausschuettungen_decken_basisertrag) – None wenn VAP > 0 |
| `sparer_pauschbetrag_verbraucht` | string | ja |  |  | An den Sonstigen Topf angerechneter Betrag in EUR |
| `sparer_pauschbetrag_rest` | string | ja |  |  | Verbleibender Sparer-Pauschbetrag in EUR |
| `steuerpflichtige_bemessungsgrundlage` | string | ja |  |  | Bemessungsgrundlage fuer KapESt in EUR (Sonstiger-Topf-Saldo plus VAP steuerpflichtig, abzueglich Sparer-Pauschbetrag) |
| `kapest` | string | ja |  |  | Kapitalertragsteuer 25 % in EUR (§43a EStG) |
| `soli` | string | ja |  |  | Solidaritaetszuschlag 5,5 % auf KapESt in EUR |
| `kirchensteuer` | string | ja |  |  | Kirchensteuer 8 % (BY/BW) bzw. 9 % auf KapESt in EUR |
| `steuer_summe` | string | ja |  |  | KapESt + Soli + KiSt in EUR |
| `netto_kapitalertraege` | string | ja |  |  | Bemessungsgrundlage abzueglich Steuer-Summe in EUR |
| `effektivsatz_prozent` | string | ja |  |  | Effektiver Steuersatz auf Bemessungsgrundlage in Prozent (mit KiSt) |
| `krypto_steuerpflichtig` | string | ja |  |  | Steuerpflichtiger §23-Krypto-Gewinn in EUR – wird mit persoenlichem ESt-Tarif §32a EStG versteuert (NICHT 25 % KapESt). 0 wenn Freigrenze greift. |
| `pauschal_steuer_naiv` | string | ja |  |  | Vergleichswert: Bemessungsgrundlage × 26,375 % (KapESt+Soli ohne KiSt) – wie es viele Online-Rechner pauschal ansetzen |
| `differenz_zu_naiv` | string | ja |  |  | Echte Steuer-Summe minus Pauschal-Naiv in EUR. Positiv = du zahlst durch KiSt mehr als der Pauschalansatz suggeriert. |
| `aktien_topf_aktiv` | boolean | ja |  |  | Status §20 Abs. 6 Satz 4 EStG (False nach BVerfG-Aufhebung) |
| `bverfg_hinweis` | string | ja |  |  | Hinweis zum §165 AO-Vorlaeufigkeitsvermerk (None wenn nicht relevant) |
| `bundesland` | string | ja |  |  | Bundesland aus der Anfrage (Default "Nordrhein-Westfalen"). Bestimmt den Kirchensteuersatz (8 % in Bayern und Baden-Württemberg, sonst 9 %). |
| `kirchenmitglied` | boolean | ja |  |  | Echo des Eingabeflags. Bei true wird die Kapitalertragsteuer mit Kirchensteuer nach der Formel e/(4+k) berechnet. |
| `veranlagungszeitraum` | integer | ja |  |  | Veranlagungsjahr aus der Anfrage (Default: aktuelles Steuerjahr). Wählt den Basiszins für die Vorabpauschale; fehlt er für das Jahr, antwortet der Endpoint mit 400. |
| `rechtsgrundlage` | string | ja |  |  | Fester Text mit den Normen, auf denen das Bundle beruht. Hängt nicht von der Eingabe ab. |
| `hinweise` | array<string> | ja |  |  | Liste erläuternder Texte: Bundle-Herkunft, ggf. Vorabpauschale bzw. Grund für keine, Kirchensteuersatz, Krypto-Freigrenze oder Krypto-Besteuerung nach persönlichem Tarif sowie ggf. BVerfG-Hinweis. |
