# Minijob / Midijob-Rechner

`POST /v1/minijob`

Kategorie: Minijob

Bestimmt den Beschaeftigungsstatus (Minijob, Midijob oder volle SV-Pflicht) und berechnet den Nettolohn sowie die Sozialversicherungsbeitraege. Beruecksichtigt den Uebergangsbereich (Midijob) von 603-2.000 EUR mit gleitenden Beitraegen (§8, §20 SGB IV). Grenzwerte ab 01.01.2026 (Mindestlohn 13,90 EUR/h).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bruttogehalt` | number | ja |  |  | Monatliches Bruttogehalt in EUR |
| `kinderlos_ueber_23` | boolean |  | false |  | True wenn kinderlos und aelter als 23 (PV-Zuschlag) |
| `bundesland` | enum |  | "Berlin" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (relevant fuer Sachsen-Sonderregel PV) |

Beispiel:

```json
{
  "bruttogehalt": 550,
  "bundesland": "Berlin"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `status` | string | ja |  |  | Beschaeftigungsstatus: 'minijob', 'midijob' oder 'volle_sv' |
| `brutto` | string | ja |  |  | Bruttogehalt pro Monat in EUR |
| `netto` | string | ja |  |  | Nettogehalt pro Monat in EUR |
| `sv_abzuege` | string | ja |  |  | SV-Abzuege gesamt pro Monat in EUR |
| `kv_beitrag` | string | ja |  |  | KV-Beitrag AN pro Monat in EUR |
| `pv_beitrag` | string | ja |  |  | PV-Beitrag AN pro Monat in EUR |
| `rv_beitrag` | string | ja |  |  | RV-Beitrag AN pro Monat in EUR |
| `av_beitrag` | string | ja |  |  | AV-Beitrag AN pro Monat in EUR |
| `ag_kv` | string | ja |  |  | AG KV-Beitrag pro Monat in EUR |
| `ag_pv` | string | ja |  |  | AG PV-Beitrag pro Monat in EUR (0 bei Minijob) |
| `ag_rv` | string | ja |  |  | AG RV-Beitrag pro Monat in EUR |
| `ag_av` | string | ja |  |  | AG AV-Beitrag pro Monat in EUR (0 bei Minijob) |
| `ag_u1` | string | ja |  |  | AG U1-Umlage pro Monat in EUR |
| `ag_u2` | string | ja |  |  | AG U2-Umlage pro Monat in EUR |
| `ag_insolvenzgeld` | string | ja |  |  | AG Insolvenzgeldumlage pro Monat in EUR |
| `ag_pauschale_steuer` | string | ja |  |  | AG pauschale Lohnsteuer (nur Minijob) in EUR |
| `ag_gesamt` | string | ja |  |  | AG-Kosten gesamt pro Monat in EUR |
| `ag_kosten_gesamt` | string | ja |  |  | Gesamtarbeitskosten (Brutto + AG) pro Monat in EUR |
| `stunden_mindestlohn` | string | ja |  |  | Arbeitsstunden bei Mindestlohn (13,90 EUR/h) |
| `vergleich_plus_100` | MinijobVergleich | ja |  |  | Netto bei Brutto + 100 EUR |
| `vergleich_minus_100` | MinijobVergleich | ja |  |  | Netto bei Brutto - 100 EUR |
| `hinweis` | string | ja |  |  | Erklaerungstext zum Beschaeftigungsstatus |
