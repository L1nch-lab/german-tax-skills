# Midijob-Rechner (Uebergangsbereich)

`POST /v1/midijob`

Kategorie: Midijob

Berechnet das Netto eines Midijobbers im Uebergangsbereich (603,01 - 2.000,00 EUR Monatsbrutto 2026). Wendet die §20 Abs. 2a SGB IV Formeln mit Faktor F = 0,6619 an und berechnet Lohnsteuer separat auf das volle Brutto nach BMF PAP 2026. Gibt zusaetzlich den fiktiven AN-SV-Beitrag ohne Midijob-Reduzierung sowie die daraus resultierende Ersparnis zurueck.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_monat` | number | ja |  |  | Monatsbrutto im Uebergangsbereich (603,01 - 2.000,00 EUR). Werte ausserhalb werden mit 422 abgelehnt. |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse 1-6 |
| `bundesland` | enum |  | "Berlin" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (Sachsen-Sonderregel PV) |
| `kinderlos_ueber_23` | boolean |  | false |  | True wenn kinderlos und aelter als 23 (PV-Zuschlag 0,6 %) |
| `kinder` | integer |  | 0 |  | Anzahl Kinder (fuer PV-Abschlag und LSt-KFB) |
| `kirchensteuer` | boolean |  | false |  | Kirchensteuerpflicht |
| `geburtsjahr` | integer |  | 1990 |  | Geburtsjahr (fuer PV-Kinderlos-Altersgrenze im PAP) |
| `kv_zusatzbeitrag` | number |  | "2.9" |  | KV-Zusatzbeitrag in Prozent. Default ist der durchschnittliche Zusatzbeitragssatz nach § 242a SGB V (2026: 2,9 %). Wer den Satz seiner Kasse kennt, sollte ihn setzen: die Saetze reichen von 2,18 bis 4,39 %. |

Beispiel:

```json
{
  "brutto_monat": 1000,
  "bundesland": "Berlin",
  "kv_zusatzbeitrag": "2.9",
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_monat` | string | ja |  |  | Monatsbrutto in EUR |
| `beitragspflichtige_einnahme_gesamt` | string | ja |  |  | BE fuer Gesamtbeitrag (Formel 1, §20 Abs. 2a SGB IV) |
| `beitragspflichtige_einnahme_arbeitnehmer` | string | ja |  |  | BE fuer Arbeitnehmer-Anteil (Formel 2, §20 Abs. 2a SGB IV) |
| `faktor_f` | string | ja |  |  | Faktor F des Steuerjahres (§163 Abs. 10 SGB VI) |
| `kv_an` | string | ja |  |  | KV-Anteil Arbeitnehmer in EUR |
| `pv_an` | string | ja |  |  | PV-Anteil Arbeitnehmer inkl. Kinderlos-Zuschlag (falls aktiv) in EUR |
| `rv_an` | string | ja |  |  | RV-Anteil Arbeitnehmer in EUR |
| `av_an` | string | ja |  |  | AV-Anteil Arbeitnehmer in EUR |
| `sv_an_gesamt` | string | ja |  |  | Summe aller AN-SV-Beitraege in EUR |
| `lohnsteuer_monat` | string | ja |  |  | Lohnsteuer pro Monat in EUR |
| `soli_monat` | string | ja |  |  | Solidaritaetszuschlag pro Monat in EUR |
| `kirchensteuer_monat` | string | ja |  |  | Kirchensteuer pro Monat in EUR |
| `abzuege_gesamt` | string | ja |  |  | Summe aller Abzuege (SV + LSt + Soli + KiSt) in EUR |
| `netto_monat` | string | ja |  |  | Netto-Monatsgehalt in EUR |
| `voller_sv_an_vergleich` | string | ja |  |  | Fiktiver AN-SV-Beitrag ohne Midijob-Reduzierung (Vergleichswert) |
| `ersparnis_vs_volle_sv` | string | ja |  |  | Ersparnis pro Monat durch Midijob-Regelung (EUR) |
