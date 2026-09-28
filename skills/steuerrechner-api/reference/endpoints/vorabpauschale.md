# Vorabpauschale fuer thesaurierende ETF/Fonds (§18 InvStG)

`POST /v1/vorabpauschale`

Kategorie: Vorabpauschale

Berechnet die Vorabpauschale fuer ein volles Kalenderjahr nach §18 InvStG. Beruecksichtigt den jahresspezifischen Basiszins (BMF-Schreiben Anfang Januar), den 70-Prozent-Faktor nach §16 InvStG, die Cap auf die Wertsteigerung, gezahlte Ausschuettungen sowie die Teilfreistellung nach §20 InvStG (Aktien 30, Misch 15, Sonstige 0, Immo Inland 60, Immo Ausland 80 Prozent). Sonderfaelle (negativer Basiszins, Verlustjahr, Ausschuettungen >= Basisertrag) werden mit `keine_vap_grund` markiert.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `fondswert_jahresanfang` | number | ja |  |  | Ruecknahmepreis am ersten Bewertungstag des Jahres in EUR |
| `fondswert_jahresende` | number | ja |  |  | Ruecknahmepreis am letzten Bewertungstag des Jahres in EUR |
| `ausschuettungen` | number |  | "0" |  | Im Jahr gezahlte Ausschuettungen in EUR (0 fuer thesaurierende Fonds) |
| `fondstyp` | enum | ja |  | aktien_51, misch_25, sonstige, immo_inland, immo_ausland | Fondstyp nach §20 InvStG: aktien_51 (>=51 % Aktien, TFQ 30 %), misch_25 (>=25 % Aktien, TFQ 15 %), sonstige (TFQ 0 %), immo_inland (TFQ 60 %), immo_ausland (TFQ 80 %) |
| `jahr` | integer |  | 2026 |  | Kalenderjahr der Vorabpauschale-Berechnung. Basiszins kommt aus BMF-Schreiben Anfang Januar des Folgejahres. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `fondswert_jahresanfang` | string | ja |  |  | Ruecknahmepreis Jahresanfang in EUR |
| `fondswert_jahresende` | string | ja |  |  | Ruecknahmepreis Jahresende in EUR |
| `ausschuettungen` | string | ja |  |  | Im Jahr gezahlte Ausschuettungen in EUR |
| `wertsteigerung` | string | ja |  |  | Wertsteigerung im Kalenderjahr (Jahresende - Jahresanfang) in EUR |
| `basiszins_prozent` | string | ja |  |  | Anzuwendender Basiszins in Prozent (BMF-Schreiben Anfang Januar) |
| `basisertrag` | string | ja |  |  | Basisertrag nach §16 Abs. 1 InvStG = Wert_Jahresanfang × Basiszins × 0,70 |
| `vorabpauschale_brutto` | string | ja |  |  | VAP brutto = min(Basisertrag - Ausschuettungen, Wertsteigerung), in EUR |
| `teilfreistellung_quote` | string | ja |  |  | Teilfreistellungsquote nach §20 InvStG (0.30 Aktien, 0.15 Misch, ...) |
| `vorabpauschale_steuerpflichtig` | string | ja |  |  | VAP nach Teilfreistellung – Bemessungsgrundlage fuer Kapitalertragsteuer |
| `keine_vap_grund` | string |  |  |  | Falls keine VAP anfaellt: 'negativer_basiszins', 'kein_wertzuwachs' oder 'ausschuettungen_decken_basisertrag'. Sonst null. |
| `fondstyp` | string | ja |  |  |  |
| `jahr` | integer | ja |  |  |  |
| `rechtsgrundlage` | string |  | "§18 InvStG, §16 InvStG, §20 InvStG" |  |  |
