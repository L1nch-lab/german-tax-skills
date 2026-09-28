# Kfz-Steuer

`POST /v1/kfz-steuer`

Kategorie: Kfz-Steuer

Berechnet die Kfz-Jahressteuer nach dem Kraftfahrzeugsteuergesetz (KraftStG).

**Drei Erstzulassungs-Regime.** `erstzulassung_jahr` waehlt die Rechenweise, nicht `bezugsjahr`:

- **ab 1.1.2021** (§9 Abs. 1 Nr. 2c): Hubraum plus progressiv gestaffelter CO2-Anteil ueber 95 g/km, sechs Stufen von 2,00 bis 4,00 EUR je Gramm.
- **1.7.2009 bis 31.12.2020** (Nr. 2b): Hubraum plus flach 2,00 EUR je Gramm ueber der Schwelle. Die Schwelle haengt am Zulassungsjahr – 120 g/km bis 2011, 110 g/km ab 2012, 95 g/km ab 2014.
- **Elektro** (§3d i.V.m. §9 Abs. 2): zehn Jahre steuerbefreit ab Erstzulassung, laengstens bis 2035, und nur fuer Erstzulassungen zwischen 2011 und 2030. Danach Gewichtsbesteuerung nach §9 Abs. 1 Nr. 3 abzueglich 50 %.

**Aufrundung.** Der Hubraum-Anteil rechnet je ANGEFANGENE 100 cm3 (PKW) bzw. 25 cm3 (Kraftrad). 1.601 cm3 kosten deshalb genauso viel wie 1.700 cm3 – ein haeufiger Grund fuer scheinbar falsche Ergebnisse.

**Diesel-Aufschlag.** 9,50 statt 2,00 EUR je angefangene 100 cm3 (Selbst- statt Fremdzuendungsmotor). Das ist der groesste Einzelhebel im Ergebnis; `kraftstoff` gehoert deshalb in jede Anfrage fuer 'pkw'.

⚠️ Nicht abgedeckt: Wohnmobile (§9 Abs. 1 Nr. 2a), Nutzfahrzeuge ueber 3,5 t (Nr. 4), Anhaenger (Nr. 5) und PKW mit Erstzulassung vor dem 1.7.2009 – dort gilt die Euro-Norm-Tabelle der Nr. 2a statt der CO2-Besteuerung. Fuer diese Fahrzeuge liefert der Endpoint kein belastbares Ergebnis.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `fahrzeugart` | enum | ja |  | pkw, elektro, motorrad, oldtimer | 'pkw' (Hubraum + CO2), 'elektro' (§3d Befreiung, danach Gewichtsbesteuerung), 'motorrad' (§9 Abs. 1 Nr. 1) oder 'oldtimer' (H-Kennzeichen, §9 Abs. 4). |
| `hubraum` | integer |  | 0 |  | Hubraum in cm3. Pflicht fuer 'pkw' und 'motorrad'. Wird auf angefangene 100 cm3 (PKW) bzw. 25 cm3 (Kraftrad) aufgerundet – 1601 cm3 kosten deshalb so viel wie 1700 cm3. |
| `co2` | integer |  | 0 |  | CO2-Ausstoss in g/km laut Zulassungsbescheinigung Teil I (Feld V.7), WLTP. Nur fuer 'pkw' relevant. |
| `kraftstoff` | enum |  | "benziner" | benziner, diesel | 'benziner' = Fremdzuendungsmotor (2,00 EUR je angef. 100 cm3), 'diesel' = Selbstzuendungsmotor (9,50 EUR). Der Unterschied ist der groesste Einzelhebel im Ergebnis. |
| `erstzulassung_jahr` | integer |  | 2021 |  | Jahr der Erstzulassung. Waehlt das Besteuerungsregime: ab 2021 progressive CO2-Staffel (§9 Abs. 1 Nr. 2c), 2009-2020 flache 2 EUR je g ueber Schwelle (Nr. 2b). Steuert bei 'elektro' ausserdem die Zehnjahresbefreiung nach §3d. |
| `gewicht` | integer |  | 1500 |  | Zulaessiges Gesamtgewicht in kg. Nur fuer 'elektro' NACH Ablauf der Befreiung relevant (Gewichtsbesteuerung §9 Abs. 1 Nr. 3, abzueglich 50 % nach Abs. 2). |
| `bezugsjahr` | integer |  | 2026 |  | Jahr, fuer das die Steuer ermittelt wird. Entscheidet bei 'elektro', ob die Befreiung noch laeuft. |

Beispiel:

```json
{
  "co2": 132,
  "erstzulassung_jahr": 2022,
  "fahrzeugart": "pkw",
  "hubraum": 1598,
  "kraftstoff": "benziner"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `jahressteuer` | string | ja |  |  | Kfz-Jahressteuer in EUR |
| `monatlich` | string | ja |  |  | Jahressteuer geteilt durch 12 in EUR |
| `hubraum_anteil` | string | ja |  |  | Hubraum-Anteil der Steuer in EUR (§9 Abs. 1 Nr. 1 bzw. 2 KraftStG) |
| `co2_anteil` | string | ja |  |  | CO2-Anteil der Steuer in EUR (§9 Abs. 1 Nr. 2b/2c KraftStG) |
| `co2_freibetrag` | integer | ja |  |  | Angewandte CO2-Freibetragsschwelle in g/km. 95 im Regime ab 2021; im Regime 2009-2020 je nach Erstzulassung 120, 110 oder 95. 0 wenn kein CO2-Anteil anfaellt. |
| `regime` | string | ja |  |  | Angewandtes Besteuerungsregime: 'ab2021', '2009-2020', 'motorrad', 'oldtimer', 'elektro-befreit' oder 'elektro-gewicht'. |
| `befreit` | boolean | ja |  |  | True wenn das Fahrzeug steuerbefreit ist (§3d KraftStG) |
| `befreit_bis_jahr` | integer | ja |  |  | Letztes Jahr der Elektro-Steuerbefreiung (0 wenn nicht einschlaegig). Zehn Jahre ab Erstzulassung, laengstens bis 2035. |
| `hinweis` | string | ja |  |  | Erlaeuterung zum angewandten Regime (kann leer sein) |
