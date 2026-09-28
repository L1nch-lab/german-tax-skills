# Lohnkosten-zu-Netto-Umkehrrechner

`POST /v1/lohnkosten-netto`

Kategorie: Lohnkosten-Netto

Ermittelt Brutto- und Nettogehalt aus einem gegebenen Arbeitgeber-Gesamtkostenbudget. Beantwortet: 'Was verdient der Mitarbeiter netto, wenn ich als AG X EUR ausgebe?' Hinweis: Nutzt ein vereinfachtes AG-Kostenmodell (pauschale Umlagesaetze). Fuer detaillierte AG-Kosten mit konfigurierbaren U1/U2/BG-Saetzen siehe POST /v1/arbeitgeber-kosten.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `lohnkosten_ziel` | number | ja |  |  | Gewuenschte monatliche AG-Gesamtkosten in EUR |
| `steuerklasse` | enum | ja |  | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland |
| `kirchensteuer` | boolean |  | false |  | Kirchensteuerpflichtig |
| `kinder` | integer |  | 0 |  | Anzahl Kinder |
| `geburtsjahr` | integer |  | 1985 |  | Geburtsjahr |
| `kv_zusatzbeitrag` | number |  | "2.9" |  | KV-Zusatzbeitrag in Prozent. Default ist der durchschnittliche Zusatzbeitragssatz nach § 242a SGB V (2026: 2,9 %). Wer den Satz seiner Kasse kennt, sollte ihn setzen: die Saetze reichen von 2,18 bis 4,39 %. |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "kv_zusatzbeitrag": "2.9",
  "lohnkosten_ziel": 6000,
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ziel_lohnkosten` | string | ja |  |  | Angefragte AG-Gesamtkosten in EUR |
| `brutto_monat` | string | ja |  |  | Ermitteltes Bruttogehalt pro Monat |
| `brutto_jahr` | string | ja |  |  | Ermitteltes Bruttogehalt pro Jahr |
| `netto_monat` | string | ja |  |  | Resultierendes Nettogehalt pro Monat |
| `netto_jahr` | string | ja |  |  | Resultierendes Nettogehalt pro Jahr |
| `ag_kosten_gesamt` | string | ja |  |  | Tatsaechliche AG-Gesamtkosten |
| `abweichung` | string | ja |  |  | Abweichung vom Ziel in EUR |
| `iterationen` | integer | ja |  |  | Anzahl Bisection-Schritte |
| `abzuege_gesamt_monat` | string | ja |  |  | Alle AN-Abzuege pro Monat |
| `lohnsteuer_monat` | string | ja |  |  | Lohnsteuer pro Monat |
| `soli_monat` | string | ja |  |  | Solidaritaetszuschlag pro Monat |
| `kirchensteuer_monat` | string | ja |  |  | Kirchensteuer pro Monat |
| `kv_an_monat` | string | ja |  |  | KV AN-Anteil pro Monat |
| `pv_an_monat` | string | ja |  |  | PV AN-Anteil pro Monat |
| `rv_an_monat` | string | ja |  |  | RV AN-Anteil pro Monat |
| `av_an_monat` | string | ja |  |  | AV AN-Anteil pro Monat |
| `sv_gesamt_monat` | string | ja |  |  | SV gesamt (AN) pro Monat |
| `ag_kv` | string | ja |  |  | KV AG-Anteil pro Monat |
| `ag_pv` | string | ja |  |  | PV AG-Anteil pro Monat |
| `ag_rv` | string | ja |  |  | RV AG-Anteil pro Monat |
| `ag_av` | string | ja |  |  | AV AG-Anteil pro Monat |
| `ag_umlage` | string | ja |  |  | Umlage U1/U2/Insolvenzgeld pro Monat |
| `ag_gesamt` | string | ja |  |  | AG-Beitraege gesamt pro Monat |
