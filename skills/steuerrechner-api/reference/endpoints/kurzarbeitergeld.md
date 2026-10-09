# Kurzarbeitergeld-Rechner (§§ 95 ff. SGB III)

`POST /v1/kurzarbeitergeld`

Kategorie: Kurzarbeitergeld

Berechnet das Kurzarbeitergeld nach §§ 95-109 SGB III. Leistungssatz 60 % (ohne Kinder) bzw. 67 % (mit Kindern) auf die pauschalierte Nettoentgeltdifferenz (§106 SGB III). SV-Pauschale 21 % seit 2026 (§153 SGB III). Altfallregel: Betriebe, die vor 01.01.2026 bereits in KUG waren, koennen die Sonderverlaengerung auf 24 Monate bis 31.12.2026 nutzen (3. KugBeV). KUG ist steuerfrei, erhoeht aber den Steuersatz auf uebriges Einkommen (Progressionsvorbehalt, §32b EStG).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_regulaer` | number | ja |  |  | Regulaeres monatliches Bruttogehalt in EUR |
| `ausfallstunden_prozent` | number | ja |  |  | Anteil Arbeitsausfall in Prozent (0-100) |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) |
| `hat_kinder` | boolean |  | false |  | True wenn mind. 1 Kind (67 % statt 60 % Leistungssatz) |
| `altfall_vor_2026` | boolean |  | false |  | True, falls der Betrieb vor dem 01.01.2026 bereits in Kurzarbeit war – Sonderverlaengerung auf 24 Monate gemaess 3. KugBeV bis 31.12.2026. |

Beispiel:

```json
{
  "ausfallstunden_prozent": 50,
  "brutto_regulaer": 4000,
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_regulaer` | string | ja |  |  | Echo des regulären Bruttogehalts ohne Kurzarbeit in EUR pro Monat. |
| `brutto_kurzarbeit` | string | ja |  |  | Bruttogehalt während der Kurzarbeit in EUR pro Monat: brutto_regulaer × (1 − ausfallstunden_prozent / 100). |
| `netto_regulaer` | string | ja |  |  | Vereinfachtes Netto ohne Kurzarbeit in EUR pro Monat: Brutto minus Lohnsteuer minus 20 % SV-Pauschale (auf höchstens die BBG RV/AV). Soli und Kirchensteuer zieht der Code hier nicht ab. |
| `netto_kurzarbeit` | string | ja |  |  | Vereinfachtes Netto aus dem Kurzarbeitsbrutto in EUR pro Monat, ohne Kurzarbeitergeld; gleiche Rechnung wie netto_regulaer. |
| `kug_betrag` | string | ja |  |  | KUG-Zuschuss in EUR pro Monat |
| `gesamtnetto_kug` | string | ja |  |  | Netto-Kurzarbeit + KUG (insgesamt verfuegbar) |
| `differenz` | string | ja |  |  | Gesamtnetto mit KUG - regulaeres Netto |
| `differenz_prozent` | string | ja |  |  | Veränderung des Gesamtnettos mit Kurzarbeitergeld gegenüber netto_regulaer in Prozent (Skala 0-100, eine Nachkommastelle); negativ bedeutet Einbuße, 0 bei netto_regulaer <= 0. |
| `leistungssatz` | string | ja |  |  | 0.60 oder 0.67 |
| `soll_entgelt` | string | ja |  |  | Soll-Entgelt in EUR pro Monat: brutto_regulaer auf den nächsten durch 20 teilbaren Euro-Betrag gerundet und an der BBG RV/AV gekappt. |
| `ist_entgelt` | string | ja |  |  | Ist-Entgelt in EUR pro Monat: brutto_kurzarbeit auf den nächsten durch 20 teilbaren Euro-Betrag gerundet und an der BBG RV/AV gekappt. |
| `pauschal_netto_soll` | string | ja |  |  | Pauschaliertes Nettoentgelt aus dem Soll-Entgelt in EUR pro Monat: minus Lohnsteuer, Soli und 20 % SV-Pauschale. Grundlage der KUG-Berechnung. |
| `pauschal_netto_ist` | string | ja |  |  | Pauschaliertes Nettoentgelt aus dem Ist-Entgelt in EUR pro Monat, gleiche Rechnung wie pauschal_netto_soll; 0 bei Ist-Entgelt 0. |
| `ausfallstunden_prozent` | string | ja |  |  | Echo des Arbeitsausfalls in Prozent (Skala 0-100). |
| `bezugsdauer_monate` | integer | ja |  |  | 12 (Regel) oder 24 (Altfall-Sonderregel) |
| `sonderverlaengerung_moeglich` | boolean | ja |  |  | True, wenn altfall_vor_2026 gesetzt ist; dann gilt die verlängerte Bezugsdauer von 24 statt 12 Monaten. |
| `progressionsvorbehalt_hinweis` | boolean | ja |  |  | Immer True: Kurzarbeitergeld ist steuerfrei, unterliegt aber dem Progressionsvorbehalt (§ 32b EStG) und erhöht den Steuersatz auf das übrige Einkommen. |
| `hinweise` | array<string> | ja |  |  | Liste erläuternder Texte: Progressionsvorbehalt, angewendeter Leistungssatz und Bezugsdauer (Regelfall oder Sonderverlängerung). |
