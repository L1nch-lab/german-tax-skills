# KfW 458 Waermepumpe-Foerderungs-Rechner (BEG EM)

`POST /v1/waermepumpe`

Kategorie: Waermepumpe

Berechnet die KfW-Zuschussfoerderung fuer Waermepumpen-Tausch nach Bundesfoerderung effiziente Gebaeude – Einzelmassnahmen (BEG EM), Programm 458 (Richtlinie ab 21.07.2026). Bonus-Bausteine: Grund 30 %, Klimageschwindigkeit 16 % (ab 01.02.2027 −4 Pp/Halbjahr), gestaffelter Einkommensbonus 40/30/10 % (zvE HH <= 30k/40k/50k), Familienzuschlag −10.000 EUR aufs anzusetzende Einkommen bei minderjaehrigem Kind. Einkommensabhaengiger Deckel 80 % (zvE <= 30k) bzw. 70 %. Vergleicht mit Alternative § 35c EStG (Doppelfoerderverbot).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `investition_eur` | number | ja |  |  | Bruttoinvestition (Waermepumpe + Installation + Zubehoer) in EUR |
| `wohneinheiten` | integer |  | 1 |  | Wohneinheiten (1 = EFH) |
| `heizungstausch` | boolean |  | true |  | Wird eine bestehende Heizung getauscht? |
| `heizungsalter_ok` | boolean |  | true |  | Oel/Kohle/Etagen/Nachtspeicher beliebigen Alters ODER Gas/Biomasse >= 20 Jahre alt |
| `haushaltseinkommen_eur` | number |  |  |  | zu versteuerndes Haushaltsjahreseinkommen in EUR (Einkommensbonus 40/30/10 % bei <= 30k/40k/50k). None = kein Einkommensbonus, Deckel 70 %. |
| `hat_minderjaehriges_kind` | boolean |  | false |  | Mind. 1 gemeldetes minderjaehriges Kind (Familienzuschlag: anzusetzendes Einkommen einmalig -10.000 EUR)? |

Beispiel:

```json
{
  "heizungsalter_ok": true,
  "heizungstausch": true,
  "investition_eur": 32000,
  "wohneinheiten": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `investition_eur` | string | ja |  |  | Bruttoinvestition für die Wärmepumpe inkl. Installation in EUR aus der Anfrage. |
| `wohneinheiten` | integer | ja |  |  | Anzahl Wohneinheiten im Gebäude (1 = Einfamilienhaus). Bestimmt die Summe der förderfähigen Höchstkosten. |
| `heizungstausch` | boolean | ja |  |  | Echo: true, wenn eine bestehende Heizung ersetzt wird; Voraussetzung für den Klimageschwindigkeitsbonus. Auch bei investition_eur 0 die Eingabe. |
| `heizungsalter_ok` | boolean | ja |  |  | Echo: true, wenn die alte Heizung die Bonus-Voraussetzung erfüllt (Öl/Kohle/Etagen/Nachtspeicher beliebigen Alters oder Gas/Biomasse ab 20 Jahren). Auch bei investition_eur 0 die Eingabe. |
| `haushaltseinkommen_eur` | string | ja |  |  | Zu versteuerndes Haushaltsjahreseinkommen in EUR aus der Anfrage. null, wenn nicht angegeben (dann kein Einkommensbonus, Deckel 70 %). |
| `hat_minderjaehriges_kind` | boolean | ja |  |  | Echo: true, wenn mindestens ein minderjähriges Kind im Haushalt ist; senkt das anzusetzende Einkommen einmalig um 10.000 EUR. Auch bei investition_eur 0 die Eingabe. |
| `familienzuschlag_angewandt` | boolean | ja |  |  | True, wenn hat_minderjaehriges_kind gesetzt und ein Haushaltseinkommen angegeben ist, also der Abzug von 10.000 EUR tatsächlich gerechnet wurde. |
| `anzusetzendes_einkommen_eur` | string | ja |  |  | zvE nach Familienzuschlag (-10.000 EUR bei minderj. Kind) |
| `stichtag` | string | ja |  |  | Antragsdatum fuer die Degression (ISO) |
| `foerderfaehige_investition` | string | ja |  |  | Förderfähiger Teil der Investition in EUR: Minimum aus investition_eur und der Höchstkostensumme (1. WE nach Antragsdatum, WE 2–6 je 15.000, ab WE 7 je 8.000). |
| `investition_ueber_cap` | boolean | ja |  |  | True, wenn investition_eur die Höchstkostensumme übersteigt und der Rest nicht gefördert wird. |
| `cap_hinweise` | array<string> | ja |  |  | Liste mit höchstens einem Text: Betrag über der Höchstkostensumme, der aus Eigenmitteln zu tragen ist. Sonst leer. |
| `grund_prozent` | string | ja |  |  | 30 % Grundfoerderung |
| `klima_prozent` | string | ja |  |  | Klimageschwindigkeitsbonus (16 % ab 21.07.2026) |
| `einkommen_prozent` | string | ja |  |  | Gestaffelt 40/30/10 % nach anzusetzendem zvE |
| `summe_ungekappt_prozent` | string | ja |  |  | Summe der Förderbausteine in Prozent vor dem Deckel: Grundförderung + Klimabonus + Einkommensbonus. |
| `final_quote_prozent` | string | ja |  |  | Nach einkommensabh. Deckel (80/70 %) |
| `ist_quote_gekappt` | boolean | ja |  |  | True, wenn summe_ungekappt_prozent über dem einkommensabhängigen Deckel (80 % bzw. 70 %) liegt. |
| `zuschuss_eur` | string | ja |  |  | KfW-Zuschuss in EUR = foerderfaehige_investition × finale Förderquote. Datum der Degression ist der Tag der Anfrage. |
| `eigenanteil_eur` | string | ja |  |  | Selbst zu tragender Betrag in EUR = investition_eur − zuschuss_eur, inkl. des Teils über der Höchstkostensumme. |
| `paragraph_35c_ermaessigung_eur` | string | ja |  |  | Alternative 20 % / max 40.000 EUR |
| `kfw_besser_als_35c` | boolean | ja |  |  | True, wenn zuschuss_eur größer ist als die § 35c-Alternative (20 % der Investition, höchstens 40.000 EUR). Die § 35c-Voraussetzungen werden dabei nicht geprüft. |
| `vorteil_kfw_vs_35c_eur` | string | ja |  |  | Differenz in EUR: zuschuss_eur − § 35c-Ermäßigung. Negativ, wenn § 35c mehr bringt; der Zuschuss fließt sofort, die Ermäßigung verteilt über 3 Jahre (nicht abgezinst). |
| `empfehlung` | string | ja |  |  | Zusammengesetzter Text: Vergleich KfW gegen § 35c, ggf. Kappungshinweis, entgangene Boni, Cap-Hinweise und der Hinweis auf Antragstellung vor Auftragsvergabe. |
| `max_foerderquote` | string | ja |  |  | Angewandter Deckel: 80 % (zvE <= 30k) o. 70 % |
| `klima_prozent_aktuell` | string | ja |  |  | Klimabonus am Stichtag (vor Qualifikation) |
| `cap_we1` | string | ja |  |  | 28.000 EUR pro 1. WE (degressiv ab 02/2027) |
| `cap_we2_6` | string | ja |  |  | 15.000 EUR je WE 2-6 |
| `cap_we_ab_7` | string | ja |  |  | 8.000 EUR je WE ab 7 |
