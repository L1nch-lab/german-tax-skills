# Gewerbesteuer-Rechner

`POST /v1/gewerbesteuer`

Kategorie: Gewerbesteuer

Berechnet die Gewerbesteuer fuer Einzelunternehmen, Personengesellschaften und Kapitalgesellschaften. Beruecksichtigt den Freibetrag (24.500 EUR fuer Personenunternehmen), die Steuermesszahl (3,5%) und den gemeindlichen Hebesatz. Fuer Personenunternehmen wird die ESt-Anrechnung nach §35 EStG (max. 4x Steuermessbetrag) berechnet. Hebesatz kann direkt angegeben oder per AGS, PLZ oder Gemeindename ermittelt werden. Rechtsgrundlage: §6, §7, §11, §16 GewStG, §35 EStG.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `gewinn` | number | ja |  |  | Gewerbeertrag (vereinfacht = Gewinn) in EUR |
| `rechtsform` | enum | ja |  | einzelunternehmen, personengesellschaft, kapitalgesellschaft | Rechtsform: 'einzelunternehmen', 'personengesellschaft' oder 'kapitalgesellschaft' |
| `hebesatz` | integer |  |  |  | Gewerbesteuer-Hebesatz in Prozent (z.B. 490 fuer 490%). Alternativ: ags, plz oder gemeinde zur automatischen Ermittlung. |
| `ags` | string |  |  |  | 8-stelliger Amtlicher Gemeindeschluessel (AGS) zur automatischen Hebesatz-Ermittlung. |
| `plz` | string |  |  |  | 5-stellige PLZ zur Hebesatz-Ermittlung. Gehoert sie zu mehreren Gemeinden, kommt 409 PLZ_AMBIGUOUS mit den Kandidaten (dann ags senden). |
| `gemeinde` | string |  |  |  | Gemeindename zur Hebesatz-Suche (verwendet erstes Ergebnis). Beispiel: 'München'. |

Beispiel:

```json
{
  "gewinn": 100000,
  "hebesatz": 490,
  "rechtsform": "kapitalgesellschaft"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `gewinn` | string | ja |  |  | Gewerbeertrag (Gewinn) in EUR |
| `rechtsform` | string | ja |  |  | Rechtsform des Unternehmens |
| `hebesatz` | integer | ja |  |  | Angewendeter Hebesatz in Prozent |
| `freibetrag` | string | ja |  |  | Freibetrag in EUR (24.500 Personen, 0 Kapital) |
| `gewerbeertrag_nach_freibetrag` | string | ja |  |  | Gewerbeertrag nach Abzug des Freibetrags in EUR |
| `steuermesszahl` | string | ja |  |  | Steuermesszahl in Prozent (3,5%) |
| `steuermessbetrag` | string | ja |  |  | Steuermessbetrag in EUR |
| `gewerbesteuer` | string | ja |  |  | Gewerbesteuer in EUR |
| `effektiver_steuersatz` | string | ja |  |  | Effektiver Gewerbesteuersatz in Prozent (bezogen auf Gewinn) |
| `est_anrechnung` | string | ja |  |  | ESt-Anrechnung nach §35 EStG in EUR (nur Personenunternehmen) |
| `gewerbesteuer_nach_anrechnung` | string | ja |  |  | Verbleibende Gewerbesteuer nach ESt-Anrechnung in EUR |
| `hebesatz_vergleich` | array<GewerbesteuerHebesatzVergleichItem> | ja |  |  | Vergleich der Gewerbesteuer bei verschiedenen Hebesaetzen |
