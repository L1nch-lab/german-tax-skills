# Netto-Brutto-Umkehrrechner

`POST /v1/netto-brutto`

Kategorie: Netto-Brutto

Ermittelt das Bruttogehalt, das zu einem gewuenschten Nettogehalt fuehrt. Nutzt Bisection ueber die offizielle Brutto-Netto-Berechnung (BMF PAP 2026). Liefert die volle Gehaltsaufschluesselung inkl. Lohnsteuer, SV-Beitraege und AG-Kosten fuer das ermittelte Bruttogehalt.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `nettolohn` | number | ja |  |  | Gewuenschtes monatliches Nettoeinkommen in EUR |
| `steuerklasse` | enum | ja |  | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (relevant fuer Kirchensteuer-Satz und PV-Sachsen) |
| `kirchensteuer` | boolean |  | false |  | True wenn Kirchensteuer abzufuehren ist |
| `kinder` | integer |  | 0 |  | Anzahl Kinder (fuer PV-Staffelung) |
| `geburtsjahr` | integer |  | 1985 |  | Geburtsjahr (fuer PV-Kinderlos-Zuschlag) |
| `kv_zusatzbeitrag` | number |  | "2.9" |  | KV-Zusatzbeitrag in Prozent. Default ist der durchschnittliche Zusatzbeitragssatz nach § 242a SGB V (2026: 2,9 %). Wer den Satz seiner Kasse kennt, sollte ihn setzen: die Saetze reichen von 2,18 bis 4,39 %. |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "kv_zusatzbeitrag": "2.9",
  "nettolohn": 2500,
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ziel_netto` | string | ja |  |  | Angefragtes Wunsch-Netto in EUR |
| `brutto_monat` | string | ja |  |  | Ermitteltes Bruttogehalt pro Monat in EUR |
| `brutto_jahr` | string | ja |  |  | Ermitteltes Bruttogehalt pro Jahr in EUR |
| `netto_monat` | string | ja |  |  | Tatsaechlich erreichtes Netto pro Monat in EUR |
| `netto_jahr` | string | ja |  |  | Tatsaechlich erreichtes Netto pro Jahr in EUR |
| `abweichung` | string | ja |  |  | Abweichung vom Ziel-Netto in EUR (positiv/negativ) |
| `iterationen` | integer | ja |  |  | Anzahl Bisection-Schritte |
| `abzuege_gesamt_monat` | string | ja |  |  | Alle Abzuege pro Monat in EUR |
| `lohnsteuer_monat` | string | ja |  |  | Lohnsteuer pro Monat in EUR |
| `soli_monat` | string | ja |  |  | Solidaritaetszuschlag pro Monat in EUR |
| `kirchensteuer_monat` | string | ja |  |  | Kirchensteuer pro Monat in EUR |
| `kv_an_monat` | string | ja |  |  | Krankenversicherung AN-Anteil pro Monat |
| `pv_an_monat` | string | ja |  |  | Pflegeversicherung AN-Anteil pro Monat |
| `rv_an_monat` | string | ja |  |  | Rentenversicherung AN-Anteil pro Monat |
| `av_an_monat` | string | ja |  |  | Arbeitslosenversicherung AN-Anteil pro Monat |
| `sv_gesamt_monat` | string | ja |  |  | Sozialversicherung gesamt (AN) pro Monat |
| `ag_kv` | string | ja |  |  | KV AG-Anteil pro Monat in EUR |
| `ag_pv` | string | ja |  |  | PV AG-Anteil pro Monat in EUR |
| `ag_rv` | string | ja |  |  | RV AG-Anteil pro Monat in EUR |
| `ag_av` | string | ja |  |  | AV AG-Anteil pro Monat in EUR |
| `ag_umlage` | string | ja |  |  | Umlage U1/U2/Insolvenzgeld pro Monat in EUR |
| `ag_gesamt` | string | ja |  |  | AG-SV-Anteil gesamt pro Monat in EUR |
| `ag_kosten_gesamt` | string | ja |  |  | Gesamtarbeitskosten pro Monat in EUR |
| `kv_satz` | string | ja |  |  | Angewendeter KV-Gesamtbeitragssatz in Prozent |
| `pv_satz` | string | ja |  |  | Angewendeter PV-AN-Beitragssatz in Prozent |
| `rv_satz` | string | ja |  |  | RV-Beitragssatz AN in Prozent |
| `av_satz` | string | ja |  |  | AV-Beitragssatz AN in Prozent |
