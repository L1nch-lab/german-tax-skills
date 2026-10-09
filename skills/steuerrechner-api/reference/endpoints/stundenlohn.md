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
| `modus` | string | ja |  |  | Echo der Rechenrichtung: 'stundenlohn_zu_gehalt' (Stundenlohn wird in Monatsgehalt umgerechnet) oder 'gehalt_zu_stundenlohn' (Monatsgehalt wird in Stundenlohn umgerechnet). |
| `wochenstunden` | string | ja |  |  | Echo der vertraglichen Wochenarbeitszeit in Stunden; Grundlage für die Umrechnung Stunde/Monat mit dem Faktor 52/12 Wochen pro Monat. |
| `stunden_pro_monat` | string | ja |  |  | Stunden pro Monat (52/12 * Wochenstunden) |
| `stundenlohn_brutto` | string | ja |  |  | Brutto-Stundenlohn in EUR |
| `brutto_monat` | string | ja |  |  | Bruttogehalt in EUR pro Monat; im Modus stundenlohn_zu_gehalt berechnet als Stundenlohn × Wochenstunden × 52/12, sonst das eingegebene Monatsgehalt. |
| `brutto_jahr` | string | ja |  |  | Jahresbrutto in EUR, berechnet als brutto_monat × 12; Sonderzahlungen sind nicht enthalten. |
| `lohnsteuer_monat` | string | ja |  |  | Lohnsteuer in EUR pro Monat nach BMF-Programmablaufplan, berechnet als Jahreslohnsteuer auf das Zwölffache des Monatsbruttos geteilt durch 12. |
| `soli_monat` | string | ja |  |  | Solidaritätszuschlag in EUR pro Monat (Jahreswert / 12); Bemessung ist die Steuer auf das zvE nach Abzug der Kinderfreibeträge, unterhalb der Freigrenze 0. |
| `kirchensteuer_monat` | string | ja |  |  | Kirchensteuer in EUR pro Monat (Jahreswert / 12), Satz nach Bundesland; 0, wenn kirchensteuer=false. |
| `kv_an_monat` | string | ja |  |  | Arbeitnehmeranteil zur gesetzlichen Krankenversicherung in EUR pro Monat; Bemessung bis zur BBG KV/PV gekappt, im Übergangsbereich (Midijob) die reduzierte Bemessungsgrundlage. |
| `kv_satz` | string | ja |  |  | Angewendeter KV-Beitragssatz des Arbeitnehmers in Prozent (Skala 0-100, kein Faktor): allgemeiner AN-Satz plus die Hälfte des übergebenen kv_zusatzbeitrag. |
| `pv_an_monat` | string | ja |  |  | Arbeitnehmeranteil zur Pflegeversicherung in EUR pro Monat; Bemessung bis zur BBG KV/PV gekappt, im Übergangsbereich wird der Kinderlosenzuschlag auf eine eigene Bemessungsgrundlage gerechnet. |
| `pv_satz` | string | ja |  |  | Angewendeter PV-Beitragssatz des Arbeitnehmers in Prozent (Skala 0-100): Basissatz (in Sachsen abweichend) plus Kinderlosenzuschlag bei 0 Kindern und Alter über 23, oder minus Abschlag ab dem 2. Kind (bis 5 Kinder). |
| `rv_an_monat` | string | ja |  |  | Arbeitnehmeranteil zur Rentenversicherung in EUR pro Monat; Bemessung bis zur BBG RV/AV gekappt, im Übergangsbereich die reduzierte Bemessungsgrundlage. |
| `rv_satz` | string | ja |  |  | Angewendeter RV-Beitragssatz des Arbeitnehmers in Prozent (Skala 0-100). |
| `av_an_monat` | string | ja |  |  | Arbeitnehmeranteil zur Arbeitslosenversicherung in EUR pro Monat; Bemessung bis zur BBG RV/AV gekappt, im Übergangsbereich die reduzierte Bemessungsgrundlage. |
| `av_satz` | string | ja |  |  | Angewendeter AV-Beitragssatz des Arbeitnehmers in Prozent (Skala 0-100). |
| `sv_gesamt_monat` | string | ja |  |  | Summe der Arbeitnehmeranteile KV, PV, RV und AV in EUR pro Monat. Unterhalb des Übergangsbereichs rechnet der Code volle Beiträge, einen Minijob-Sonderfall gibt es hier nicht. |
| `abzuege_gesamt_monat` | string | ja |  |  | Alle Abzüge in EUR pro Monat: Lohnsteuer + Soli + Kirchensteuer + Arbeitnehmer-SV-Beiträge. |
| `netto_monat` | string | ja |  |  | Nettogehalt in EUR pro Monat: brutto_monat minus abzuege_gesamt_monat. |
| `netto_jahr` | string | ja |  |  | Jahresnetto in EUR, berechnet als netto_monat × 12; Sonderzahlungen sind nicht enthalten. |
| `stundenlohn_netto` | string | ja |  |  | Netto-Stundenlohn in EUR |
| `ag_kosten_gesamt` | string | ja |  |  | Arbeitgeber-Gesamtkosten/Monat |
| `mindestlohn_stunde` | string | ja |  |  | Gesetzlicher Mindestlohn je Stunde in EUR (MiLoG) |
| `unter_mindestlohn` | boolean | ja |  |  | True, wenn der Brutto-Stundenlohn unter dem gesetzlichen Mindestlohn liegt |
