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
| `brutto_regulaer` | string | ja |  |  |  |
| `brutto_kurzarbeit` | string | ja |  |  |  |
| `netto_regulaer` | string | ja |  |  |  |
| `netto_kurzarbeit` | string | ja |  |  |  |
| `kug_betrag` | string | ja |  |  | KUG-Zuschuss in EUR pro Monat |
| `gesamtnetto_kug` | string | ja |  |  | Netto-Kurzarbeit + KUG (insgesamt verfuegbar) |
| `differenz` | string | ja |  |  | Gesamtnetto mit KUG - regulaeres Netto |
| `differenz_prozent` | string | ja |  |  |  |
| `leistungssatz` | string | ja |  |  | 0.60 oder 0.67 |
| `soll_entgelt` | string | ja |  |  |  |
| `ist_entgelt` | string | ja |  |  |  |
| `pauschal_netto_soll` | string | ja |  |  |  |
| `pauschal_netto_ist` | string | ja |  |  |  |
| `ausfallstunden_prozent` | string | ja |  |  |  |
| `bezugsdauer_monate` | integer | ja |  |  | 12 (Regel) oder 24 (Altfall-Sonderregel) |
| `sonderverlaengerung_moeglich` | boolean | ja |  |  |  |
| `progressionsvorbehalt_hinweis` | boolean | ja |  |  |  |
| `hinweise` | array<string> | ja |  |  |  |
