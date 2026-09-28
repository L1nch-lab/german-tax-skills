# Firmenwagen / Geldwerter Vorteil / Dienstwagen-Rechner

`POST /v1/firmenwagen`

Kategorie: Firmenwagen

Berechnet den geldwerten Vorteil eines Firmenwagens nach der 1%-Regelung (§8 Abs. 2 EStG) und die Netto-Auswirkung. Verbrenner 1%, reine Elektrofahrzeuge (BEV) 0.25% bis zur Listenpreis-Grenze, Plug-in-Hybride 0.5% – aber nur, wenn sie die Voraussetzungen erfuellen (hoechstens 50 g CO2/km ODER die Mindestreichweite ihres Anschaffungsjahres). Ohne `phev_reichweite_km` oder `phev_co2_g` rechnet die API beim Hybrid mit dem vollen Satz. Beide Grenzen – BEV-Listenpreis und PHEV-Reichweite – haengen am `anschaffungsdatum`, nicht am Steuerjahr. Plus Fahrten Wohnung-Arbeit (0.03%) und Netto-Vergleich mit/ohne Firmenwagen inkl. Sozialversicherung (§14 SGB IV).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `listenpreis` | number | ja |  |  | Bruttolistenpreis inkl. Sonderausstattung in EUR |
| `entfernung_km` | number | ja |  |  | Einfache Entfernung Wohnung-Arbeitsstaette in km |
| `antriebsart` | enum | ja |  | verbrenner, bev, plugin_hybrid | Antriebsart: 'verbrenner', 'bev' (rein elektrisch) oder 'plugin_hybrid' |
| `bruttogehalt` | number | ja |  |  | Monatliches Bruttogehalt in EUR |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) fuer den Netto-Vergleich mit/ohne Firmenwagen |
| `eigenbeteiligung` | number |  | "0" |  | Monatliche Zuzahlung des AN in EUR |
| `kinder` | integer |  | 0 |  | Anzahl Kinder |
| `geburtsjahr` | integer |  | 1990 |  | Geburtsjahr |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland – relevant fuer Kirchensteuersatz und die Sachsen-Sonderregel beim PV-Beitrag |
| `kirchenmitglied` | boolean |  | false |  | Kirchensteuerpflichtig (fliesst in den Netto-Vergleich ein) |
| `anschaffungsdatum` | string |  |  |  | Anschaffungsdatum des Fahrzeugs (ISO 8601, z.B. '2025-09-15'). Massgeblich ist die Anschaffung, NICHT das Steuerjahr – ein Fahrzeug behaelt die Regeln seines Anschaffungszeitpunkts (§ 52 Abs. 12 Saetze 4-6 EStG). Bestimmt zweierlei: (1) die BEV-Listenpreis-Grenze fuer den Viertel-Ansatz – 60.000 EUR bis 31.12.2023, 70.000 EUR ab 01.01.2024, 100.000 EUR ab 01.07.2025; (2) die Mindestreichweite, ab der ein Plug-in-Hybrid den halben Ansatz bekommt – 40 km bis 2021, 60 km bis 2024, 80 km ab 2025. Default: heute. |
| `phev_reichweite_km` | number |  |  |  | Elektrische Reichweite in km unter ausschliesslicher Nutzung der elektrischen Antriebsmaschine. Nur bei antriebsart='plugin_hybrid' relevant. Der halbe Ansatz (0,5 %) setzt voraus, dass die Reichweite die Schwelle des Anschaffungsjahres erreicht ODER der CO2-Ausstoss hoechstens 50 g/km betraegt – eines von beiden genuegt (§ 6 Abs. 1 Nr. 4 Satz 2 Nr. 2/4/5 EStG). WIRD KEINER DER BEIDEN WERTE UEBERGEBEN, RECHNET DIE API MIT DEM VOLLEN SATZ (1 %) – der halbe Ansatz ist die Ausnahme, die das Fahrzeug erfuellen muss. Massgeblicher Nachweis ist die Uebereinstimmungsbescheinigung (CoC). |
| `phev_co2_g` | number |  |  |  | CO2-Ausstoss in g je gefahrenem Kilometer. Nur bei antriebsart='plugin_hybrid' relevant. Alternative zur Reichweite: 'hoechstens 50 Gramm' genuegt fuer den halben Ansatz – bei EXAKT 50 ist er noch drin. Diese Schwelle steht seit 2019 unveraendert im Gesetz. |
| `kv_zusatzbeitrag` | number |  | "2.9" |  | KV-Zusatzbeitrag in Prozent. Default ist der durchschnittliche Zusatzbeitragssatz nach § 242a SGB V (2026: 2,9 %). Wer den Satz seiner Kasse kennt, sollte ihn setzen: die Saetze reichen von 2,18 bis 4,39 %. |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |

Beispiel:

```json
{
  "antriebsart": "verbrenner",
  "bruttogehalt": 4000,
  "bundesland": "Nordrhein-Westfalen",
  "entfernung_km": 25,
  "kv_zusatzbeitrag": "2.9",
  "listenpreis": 40000,
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `prozentsatz` | string | ja |  |  | Angewendeter Prozentsatz (0.25/0.5/1.0) |
| `geldwerter_vorteil_privat` | string | ja |  |  | GWV Privatnutzung pro Monat in EUR |
| `fahrten_zuschlag_monat` | string | ja |  |  | Fahrten Wohnung-Arbeit Zuschlag pro Monat |
| `eigenbeteiligung` | string | ja |  |  | Eigenbeteiligung AN pro Monat |
| `geldwerter_vorteil_monat` | string | ja |  |  | Gesamt-GWV pro Monat |
| `geldwerter_vorteil_jahr` | string | ja |  |  | Gesamt-GWV pro Jahr |
| `netto_ohne_firmenwagen` | string | ja |  |  | Nettolohn ohne Firmenwagen |
| `netto_mit_firmenwagen` | string | ja |  |  | Nettolohn mit Firmenwagen |
| `mehrbelastung_steuer_monat` | string | ja |  |  | Zusaetzliche Steuer durch GWV |
| `effektive_kosten_monat` | string | ja |  |  | Effektive Kosten des FW pro Monat |
| `effektive_kosten_prozent` | string | ja |  |  | Effektive Kosten in Prozent des GWV |
| `bev_grenze_applied` | integer |  |  |  | Angewandte BEV-Listenpreis-Grenze in EUR (70.000 vor 01.07.2025, 100.000 ab Stichtag). None fuer Verbrenner/Plugin-Hybrid. |
| `bev_stichtag` | string | ja |  |  | Stichtag der BEV-Listenpreis-Grenzen-Erhoehung (Investitionssofortprogramm). |
| `anschaffungsdatum_used` | string | ja |  |  | Effektiv genutztes Anschaffungsdatum fuer die Stichtag-Logik. Entspricht dem Request-Wert oder ``date.today()`` bei fehlendem Input. |
