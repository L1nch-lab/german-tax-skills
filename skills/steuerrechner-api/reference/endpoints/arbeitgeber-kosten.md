# Arbeitgeber-Gesamtkosten-Rechner

`POST /v1/arbeitgeber-kosten`

Kategorie: Arbeitgeber-Kosten

Berechnet die vollstaendigen Arbeitgeberkosten fuer ein Bruttogehalt. Umfasst AG-Anteile an KV, PV, RV, AV sowie Umlagen (U1/U2/Insolvenzgeld) und BG-Beitrag. Alle Saetze sind konfigurierbar.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_monat` | number | ja |  |  | Monatliches Bruttogehalt in EUR |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (relevant fuer PV-Sachsen-Sonderregel) |
| `kv_zusatzbeitrag` | number |  | "2.9" |  | KV-Zusatzbeitrag in Prozent. Default ist der durchschnittliche Zusatzbeitragssatz nach § 242a SGB V (2026: 2,9 %). Wer den Satz seiner Kasse kennt, sollte ihn setzen: die Saetze reichen von 2,18 bis 4,39 %. |
| `u1_satz` | number |  | "1.1" |  | U1-Umlage (Entgeltfortzahlung) in %. Variiert je Krankenkasse. |
| `u2_satz` | number |  | "0.44" |  | U2-Umlage (Mutterschaftsgeld) in % |
| `insolvenzgeld_satz` | number |  | "0.06" |  | Insolvenzgeldumlage in % |
| `bg_beitrag` | number |  | "1.3" |  | Berufsgenossenschaft-Beitrag in %. Variiert je Branche. |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |

Beispiel:

```json
{
  "brutto_monat": 5000,
  "bundesland": "Nordrhein-Westfalen",
  "kv_zusatzbeitrag": "2.9"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_monat` | string | ja |  |  | Bruttogehalt pro Monat in EUR |
| `ag_kv` | string | ja |  |  | KV AG-Anteil pro Monat in EUR |
| `ag_pv` | string | ja |  |  | PV AG-Anteil pro Monat in EUR |
| `ag_rv` | string | ja |  |  | RV AG-Anteil pro Monat in EUR |
| `ag_av` | string | ja |  |  | AV AG-Anteil pro Monat in EUR |
| `ag_u1` | string | ja |  |  | U1-Umlage pro Monat in EUR |
| `ag_u2` | string | ja |  |  | U2-Umlage pro Monat in EUR |
| `ag_insolvenzgeld` | string | ja |  |  | Insolvenzgeldumlage pro Monat in EUR |
| `ag_bg` | string | ja |  |  | BG-Beitrag pro Monat in EUR |
| `ag_gesamt` | string | ja |  |  | AG-Beitraege gesamt pro Monat in EUR |
| `gesamtkosten` | string | ja |  |  | Gesamtarbeitskosten (Brutto + AG) in EUR |
| `aufschlag_prozent` | string | ja |  |  | AG-Aufschlag in Prozent auf Brutto |
| `sv_saetze` | SVSaetzeAG | ja |  |  | Angewendete AG-Beitragssaetze |
