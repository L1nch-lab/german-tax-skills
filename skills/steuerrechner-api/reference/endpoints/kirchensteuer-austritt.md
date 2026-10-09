# Kirchensteuer-Austrittsrechner (KiStG + § 10 Abs. 1 Nr. 4 EStG)

`POST /v1/kirchensteuer-austritt`

Kategorie: Kirchensteuer-Austritt

Berechnet die jaehrliche Kirchensteuer-Ersparnis durch Kirchenaustritt (KiSt 8 % BY/BW, 9 % uebrige), den Sonderausgaben-Effekt (KiSt als Sonderausgabe nach § 10 Abs. 1 Nr. 4 EStG = Steuerminderung × Grenzsteuersatz), die effektive Netto-Ersparnis, den Break-even-Zeitpunkt (Tage bis Austrittsgebuehr amortisiert) und 10/20/30-J-Projektionen. Austrittsgebuehren je Bundesland (0 EUR BY/BW/SN/TH bis 30 EUR uebrige).

Eingabe ist zvE direkt – wer mit brutto+steuerklasse arbeitet, ruft zuerst /v1/brutto-netto auf und nutzt das `lohnsteuer_grundlage_zve` als Input.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `zve` | number | ja |  |  | Zu versteuerndes Einkommen (Jahr) in EUR |
| `bundesland` | enum | ja |  | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (KiSt 8 % BY/BW, 9 % uebrige; eigene Gebuehrenordnung) |
| `zusammenveranlagung` | boolean |  | false |  | Ehegatten-Splitting? |
| `steuerjahr` | integer |  | 2026 |  | Steuerjahr 2024-2026 |
| `kinder` | integer |  | 0 |  | Zahl der Kinder mit Kinderfreibetrag. Fuer die KiSt wird die ESt nach § 51a Abs. 2 EStG mit den Kinderfreibetraegen (§ 32 Abs. 6) angesetzt. |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "zve": 45000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `kirchensteuer_brutto` | string | ja |  |  | KiSt vor Sonderausgaben-Effekt |
| `sonderausgaben_effekt` | string | ja |  |  | Steuerminderung durch §10 EStG |
| `netto_ersparnis` | string | ja |  |  | Tatsaechliche jaehrliche Ersparnis |
| `austrittsgebuehr` | string | ja |  |  | Einmalige Gebuehr je Bundesland |
| `break_even_tage` | string | ja |  |  | Tage bis Gebuehr amortisiert |
| `projektion_10` | string | ja |  |  | Ersparnis ueber 10 Jahre |
| `projektion_20` | string | ja |  |  | Netto-Ersparnis über 20 Jahre in EUR = netto_ersparnis × 20, ohne Einkommensentwicklung, Tarifänderung oder Verzinsung. |
| `projektion_30` | string | ja |  |  | Netto-Ersparnis über 30 Jahre in EUR = netto_ersparnis × 30, ohne Einkommensentwicklung, Tarifänderung oder Verzinsung. |
| `est` | integer | ja |  |  | Einkommensteuer auf zvE |
| `grenzsteuersatz` | string | ja |  |  | Grenzsteuersatz in % |
| `kist_satz` | string | ja |  |  | 0.08 (BY/BW) oder 0.09 (uebrige) |
| `bundesland` | string | ja |  |  | Echo des Bundeslands als voller deutscher Name. Bestimmt Kirchensteuersatz (8 % oder 9 %), Austrittsgebühr und kappung_moeglich (nie in Bayern). |
| `steuerjahr` | integer | ja |  |  | Echo des Steuerjahrs (2024–2026), nach dessen Tarif est und Kirchensteuer berechnet werden. |
| `kinder` | integer |  | 0 |  | Beruecksichtigte Kinderfreibetraege (§ 51a) |
| `kappung_moeglich` | boolean |  | false |  | True, wenn eine Kappung der KiSt (2,75-4 % zvE, auf Antrag) greifen koennte |
