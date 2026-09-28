# Stundenlohn <-> Monatsgehalt + Netto-Berechnung

`POST /v1/stundenlohn`

Kategorie: Stundenlohn

Wandelt Brutto-Stundenlohn <-> Monatsgehalt um und berechnet das Nettogehalt via BMF-PAP 2026. Beruecksichtigt Lohnsteuer (Steuerklasse 1-6), Soli, Kirchensteuer (optional), KV+PV+RV+AV (SV-Beitraege 2026, Sachsen-Sonderregel). Modus 'stundenlohn_zu_gehalt' nimmt stundenlohn_brutto, 'gehalt_zu_stundenlohn' nimmt monatsgehalt_brutto.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `modus` | enum | ja |  | stundenlohn_zu_gehalt, gehalt_zu_stundenlohn | 'stundenlohn_zu_gehalt' oder 'gehalt_zu_stundenlohn' |
| `stundenlohn_brutto` | number |  | "0" |  | Brutto-Stundenlohn in EUR (Modus stundenlohn_zu_gehalt) |
| `monatsgehalt_brutto` | number |  | "0" |  | Monatsgehalt brutto in EUR (Modus gehalt_zu_stundenlohn) |
| `wochenstunden` | number |  | "40" |  | Arbeitsstunden pro Woche (min 0.1) |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Steuerklasse 1-6 |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland |
| `kirchensteuer` | boolean |  | false |  | Kirchensteuerpflichtig? |
| `kinder` | integer |  | 0 |  | Anzahl Kinder (fuer PV) |
| `geburtsjahr` | integer |  | 1990 |  | Geburtsjahr (fuer PV-Zuschlag) |
| `kv_zusatzbeitrag` | number |  | "2.9" |  | KV-Zusatzbeitrag in Prozent. Default ist der durchschnittliche Zusatzbeitragssatz nach § 242a SGB V (2026: 2,9 %). Wer den Satz seiner Kasse kennt, sollte ihn setzen: die Saetze reichen von 2,18 bis 4,39 %. |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "kv_zusatzbeitrag": "2.9",
  "modus": "stundenlohn_zu_gehalt",
  "steuerklasse": 1,
  "stundenlohn_brutto": 25,
  "wochenstunden": 40
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `modus` | string | ja |  |  |  |
| `wochenstunden` | string | ja |  |  |  |
| `stunden_pro_monat` | string | ja |  |  | Stunden pro Monat (52/12 * Wochenstunden) |
| `stundenlohn_brutto` | string | ja |  |  | Brutto-Stundenlohn in EUR |
| `brutto_monat` | string | ja |  |  |  |
| `brutto_jahr` | string | ja |  |  |  |
| `lohnsteuer_monat` | string | ja |  |  |  |
| `soli_monat` | string | ja |  |  |  |
| `kirchensteuer_monat` | string | ja |  |  |  |
| `kv_an_monat` | string | ja |  |  |  |
| `kv_satz` | string | ja |  |  |  |
| `pv_an_monat` | string | ja |  |  |  |
| `pv_satz` | string | ja |  |  |  |
| `rv_an_monat` | string | ja |  |  |  |
| `rv_satz` | string | ja |  |  |  |
| `av_an_monat` | string | ja |  |  |  |
| `av_satz` | string | ja |  |  |  |
| `sv_gesamt_monat` | string | ja |  |  |  |
| `abzuege_gesamt_monat` | string | ja |  |  |  |
| `netto_monat` | string | ja |  |  |  |
| `netto_jahr` | string | ja |  |  |  |
| `stundenlohn_netto` | string | ja |  |  | Netto-Stundenlohn in EUR |
| `ag_kosten_gesamt` | string | ja |  |  | Arbeitgeber-Gesamtkosten/Monat |
| `mindestlohn_stunde` | string | ja |  |  | Gesetzlicher Mindestlohn je Stunde in EUR (MiLoG) |
| `unter_mindestlohn` | boolean | ja |  |  | True, wenn der Brutto-Stundenlohn unter dem gesetzlichen Mindestlohn liegt |
