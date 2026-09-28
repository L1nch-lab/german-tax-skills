# Krankengeld-Rechner (gesetzliche KV)

`POST /v1/krankengeld`

Kategorie: Krankengeld

Berechnet gesetzliches Krankengeld nach SGB V: 70% des Bruttolohns (max. BBG KV/PV), gedeckelt auf 90% des Nettolohns. Abzuege: AN-Anteile PV, RV und AV (nicht KV). Max. Bezugsdauer: 78 Wochen fuer dieselbe Krankheit. Hinweis: Das Regelentgelt wird aus dem laufenden Monatsbrutto ermittelt. Einmalig gezahltes Arbeitsentgelt (z. B. Weihnachts-/Urlaubsgeld) der letzten 12 Monate wird nach § 47 Abs. 2 Satz 6 SGB V mit 1/360 hinzugerechnet und ist in dieser Berechnung nicht enthalten - das tatsaechliche Krankengeld kann daher hoeher liegen. Ab bezugsjahr 2027 mit beschaeftigung_beendet=true: § 47 Abs. 2a SGB V (GKV-Beitragssatzstabilisierungsgesetz, BGBl. 2026 I Nr. 228) - 60 % des Nettoarbeitsentgelts, 67 % mit Kind, ohne PV/RV/AV-Abzuege beim Versicherten.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bruttogehalt_monat` | number | ja |  |  | Regelmaessiges monatliches Bruttogehalt in EUR |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) fuer die Netto-Berechnung, falls nettolohn_monat nicht angegeben ist |
| `kinder` | integer |  | 0 |  | Anzahl Kinder (fuer PV-Abschlag) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland – relevant fuer Kirchensteuersatz und die Sachsen-Sonderregel beim PV-Beitrag |
| `kinderlos` | boolean |  | true |  | Kinderlos ueber 23 (PV-Zuschlag 0.6%) |
| `kirchenmitglied` | boolean |  | false |  | Kirchensteuerpflichtig (fliesst in die Netto-Berechnung ein) |
| `nettolohn_monat` | number |  |  |  | Optionales Netto-Gehalt (wird aus Brutto berechnet wenn nicht angegeben) |
| `beschaeftigung_beendet` | boolean |  | false |  | Beschaeftigungsverhaeltnis endet waehrend der Arbeitsunfaehigkeit. Ab bezugsjahr 2027 gilt dann § 47 Abs. 2a SGB V: 60 % des Netto (67 % mit Kind), keine PV/RV/AV-Abzuege beim Versicherten. Fuer 2026 ohne Wirkung. |
| `bezugsjahr` | integer |  | 2026 |  | Jahr des Krankengeldbezugs. 2026 = geltendes Recht, 2027 = mit § 47 Abs. 2a SGB V (GKV-Beitragssatzstabilisierungsgesetz). |

Beispiel:

```json
{
  "bruttogehalt_monat": 4000,
  "bundesland": "Nordrhein-Westfalen",
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `regelentgelt` | string | ja |  |  | Regelentgelt (Brutto begrenzt auf BBG KV/PV) |
| `brutto_krankengeld_monat` | string | ja |  |  | Brutto-Krankengeld pro Monat |
| `netto_cap` | string | ja |  |  | 90%-Netto-Obergrenze |
| `abzug_pv` | string | ja |  |  | PV AN-Anteil auf Krankengeld |
| `abzug_rv` | string | ja |  |  | RV AN-Anteil auf Krankengeld |
| `abzug_av` | string | ja |  |  | AV AN-Anteil auf Krankengeld |
| `abzuege_gesamt` | string | ja |  |  | Summe PV+RV+AV Abzuege |
| `netto_krankengeld_monat` | string | ja |  |  | Netto-Krankengeld pro Monat |
| `netto_krankengeld_tag` | string | ja |  |  | Netto-Krankengeld pro Tag |
| `nettolohn_monat` | string | ja |  |  | Referenz-Nettolohn (berechnet oder angegeben) |
| `einkommensverlust_monat` | string | ja |  |  | Einkommensverlust pro Monat in EUR |
| `einkommensverlust_prozent` | string | ja |  |  | Einkommensverlust in Prozent |
| `max_bezugsdauer_wochen` | integer | ja |  |  | Max. Bezugsdauer (78 Wochen) |
| `regime` | string |  | "regel" |  | 'regel' = 70 % brutto / max. 90 % netto; 'nach_beschaeftigungsende' = § 47 Abs. 2a SGB V (ab 2027, Beschaeftigung endet waehrend der AU) |
| `satz_prozent` | string |  | "70" |  | Angewendeter Satz: 70 (Regel), 60 oder 67 (nach Beschaeftigungsende) |
| `bezugsjahr` | integer |  | 2026 |  | Jahr des Krankengeldbezugs |
| `beschaeftigung_beendet` | boolean |  | false |  | Beschaeftigungsverhaeltnis endet waehrend der AU |
