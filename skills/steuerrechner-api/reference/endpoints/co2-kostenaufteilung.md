# CO2-Kosten Mieter/Vermieter aufteilen

`POST /v1/co2-kostenaufteilung`

Kategorie: CO2-Kostenaufteilung

Teilt die CO2-Kosten einer Heizperiode nach dem Kohlendioxidkostenaufteilungsgesetz (CO2KostAufG) zwischen Mieter und Vermieter auf.

**Stufenmodell.** Massgeblich ist der spezifische Ausstoss in kg CO2 je m2 Wohnflaeche und Jahr. Je schlechter das Gebaeude, desto mehr traegt der Vermieter: von 0 % unter 12 kg/m2 bis 95 % ab 52 kg/m2 (Anlage zu §§ 5 bis 7).

⚠️ **Gerundet wird VOR der Einstufung.** §5 Abs. 1 S. 3 verlangt, den Wert auf die erste Nachkommastelle zu runden; Abs. 2 S. 2 ordnet ausdruecklich *diesen* Wert in die Tabelle ein. 11,96 kg/m2/a gehoeren damit in die Stufe '12 bis unter 17', nicht in 'unter 12'. `co2_pro_m2` gibt deshalb den gerundeten Wert zurueck – genau den, nach dem eingestuft wurde.

**Bei zentraler Versorgung zaehlt die Gesamtwohnflaeche des Gebaeudes**, nicht die der einzelnen Wohnung. Wer die eigene Wohnungsgroesse einsetzt, bekommt eine zu hohe Stufe.

**Eine Spanne statt eines Betrags.** Seit 2026 werden die Zertifikate versteigert (§10 Abs. 1 S. 2 BEHG); §10 Abs. 2 S. 4 legt nur einen Korridor von 55 bis 65 EUR je Tonne fest. Deshalb `kosten_jahr_min`/`_max` statt eines Festpreises – 55 EUR ist der Mindest-, kein Festpreis.

**Ausnahmen.** `ausnahme=halbierung` halbiert den Vermieteranteil (§9 Abs. 1, oeffentlich-rechtliche Vorgaben verhindern energetische Verbesserungen, typisch Denkmalschutz); `keine_aufteilung` streicht ihn ganz (Abs. 2). `nichtwohngebaeude=true` ersetzt die Stufentabelle durch die haelftige Teilung nach §8 Abs. 4.

⚠️ Die Emissionsfaktoren sind die heizwertbezogenen Standardwerte der EBeV 2030 (Anlage 2 Teil 4), die §3 Abs. 1 Nr. 3 CO2KostAufG vorgibt. **Fernwaerme ist davon ausgenommen**: sie ist kein BEHG-Brennstoff, und §3 Abs. 4 Nr. 3 verlangt einen netzspezifischen Mischfaktor. Der hier verwendete Wert von 0,18 kg/kWh ist eine Annaeherung – massgeblich ist der Faktor auf deiner Abrechnung.

⚠️ Nicht abgebildet: die §§ 5a bis 5d, die zum 29.07.2026 eingefuegt wurden (Netzentgelte, Kosten nach §43 Gebaeudemodernisierungsgesetz).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brennstoff` | enum | ja |  | erdgas, heizoel, fluessiggas, fernwaerme | Eingesetzter Brennstoff. 'erdgas' und 'fernwaerme' rechnen in kWh, 'heizoel' und 'fluessiggas' in Litern. |
| `verbrauch` | number | ja |  |  | Jahresverbrauch in der Einheit des Brennstoffs (kWh bzw. Liter). Bei Erdgas der Wert von der Jahresabrechnung. |
| `wohnflaeche` | number | ja |  |  | Wohnflaeche in m2, mindestens 1. Bei zentraler Versorgung die GESAMTwohnflaeche des Gebaeudes, nicht die der einzelnen Wohnung (§5 Abs. 1 S. 1) – sonst faellt die Stufe zu hoch aus. |
| `nichtwohngebaeude` | boolean |  | false |  | True = Nichtwohngebaeude. Dann greift nicht die Stufentabelle, sondern die haelftige Teilung nach §8 Abs. 4 CO2KostAufG. |
| `ausnahme` | enum |  | "keine" | keine, halbierung, keine_aufteilung | Ausnahmen nach §9 CO2KostAufG. 'halbierung' = der Vermieteranteil halbiert sich, weil oeffentlich-rechtliche Vorgaben energetische Verbesserungen verhindern (Abs. 1, typisch Denkmalschutz). 'keine_aufteilung' = er entfaellt ganz, weil sie sie unmoeglich machen (Abs. 2). |

Beispiel:

```json
{
  "ausnahme": "keine",
  "brennstoff": "erdgas",
  "nichtwohngebaeude": false,
  "verbrauch": 15000,
  "wohnflaeche": 120
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brennstoff_label` | string | ja |  |  | Anzeigename des Brennstoffs |
| `einheit` | string | ja |  |  | Einheit des Verbrauchs ('kWh' oder 'Liter') |
| `co2_kg` | string | ja |  |  | Jahres-CO2-Ausstoss in kg |
| `co2_pro_m2` | string | ja |  |  | Spezifischer Ausstoss in kg CO2 je m2 Wohnflaeche und Jahr, auf eine Nachkommastelle gerundet (§5 Abs. 1 S. 3 CO2KostAufG). Genau dieser gerundete Wert wird in die Anlage-Tabelle eingeordnet (Abs. 2 S. 2), nicht der Rohwert. |
| `stufe_label` | string | ja |  |  | Angewandte Stufe der Anlage zu §§ 5 bis 7 CO2KostAufG, oder der Hinweis auf die haelftige Teilung bei Nichtwohngebaeuden. |
| `mieter_anteil_prozent` | string | ja |  |  | Anteil des Mieters in Prozent |
| `vermieter_anteil_prozent` | string | ja |  |  | Anteil des Vermieters in Prozent |
| `preis_min` | string | ja |  |  | Mindestpreis je Tonne CO2 in EUR (§10 Abs. 2 S. 4 BEHG, 2026: 55) |
| `preis_max` | string | ja |  |  | Hoechstpreis je Tonne CO2 in EUR (§10 Abs. 2 S. 4 BEHG, 2026: 65) |
| `kosten_jahr_min` | string | ja |  |  | Gesamte CO2-Kosten im Jahr beim Mindestpreis |
| `kosten_jahr_max` | string | ja |  |  | Gesamte CO2-Kosten im Jahr beim Hoechstpreis |
| `mieter_jahr_min` | string | ja |  |  | Anteil des Mieters beim Mindestpreis, EUR/Jahr |
| `mieter_jahr_max` | string | ja |  |  | Anteil des Mieters beim Hoechstpreis, EUR/Jahr |
| `vermieter_jahr_min` | string | ja |  |  | Anteil des Vermieters beim Mindestpreis, EUR/Jahr |
| `vermieter_jahr_max` | string | ja |  |  | Anteil des Vermieters beim Hoechstpreis, EUR/Jahr |
| `mieter_monat_max` | string | ja |  |  | Anteil des Mieters beim Hoechstpreis, EUR/Monat |
