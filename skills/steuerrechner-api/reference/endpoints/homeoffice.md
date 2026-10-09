# Homeoffice-Pauschale-Rechner (§ 4 Abs. 5 Nr. 6c EStG)

`POST /v1/homeoffice`

Kategorie: Homeoffice

Berechnet die optimale Aufteilung zwischen Homeoffice-Tagespauschale (6 EUR/Tag, max 1.260 EUR p.a. bei 210 Tagen) und Pendlerpauschale (§ 9 Abs. 1 Nr. 4 EStG, 0,38 EUR/km einheitlich ab 2026). Brute-force alle Aufteilungen und liefert den maximalen Abzug, die Break-even-Entfernung (~15,8 km), Steuerersparnis im Marginalsteuersatz und die Differenz zur Eigen-Aufteilung.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `arbeitstage_gesamt` | integer |  | 220 |  | Arbeitstage pro Jahr (typisch 220 nach Urlaub/Krankheit) |
| `homeoffice_tage` | integer |  | 80 |  | Davon Homeoffice-Tage. Cap fuer Tagespauschale: 210 Tage |
| `entfernung_km` | number |  | "20" |  | Einfache Entfernung Wohnung-Buero in km |
| `grenzsteuersatz` | number |  | "0.35" |  | Persoenlicher Grenzsteuersatz als Faktor (0.35 = 35 %) |

Beispiel:

```json
{
  "arbeitstage_gesamt": 220,
  "entfernung_km": 20,
  "grenzsteuersatz": "0.35",
  "homeoffice_tage": 80
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `arbeitstage_gesamt` | integer | ja |  |  | Echo der Arbeitstage pro Jahr (0–366, Default 220). Die Optimierung prüft jede Aufteilung von 0 bis zu diesem Wert. |
| `homeoffice_tage` | integer | ja |  |  | Eingegebene HO-Tage |
| `ho_tage_eff` | integer | ja |  |  | Effektiv abrechenbare HO-Tage (gedeckelt 210) |
| `buerotage` | integer | ja |  |  | Buerotage = arbeitstage - homeoffice_tage |
| `entfernung_km` | string | ja |  |  | Echo der einfachen Entfernung Wohnung–Büro in km. Pendlerpauschale je Bürotag = entfernung_km × 0,38 EUR. |
| `grenzsteuersatz` | string | ja |  |  | Echo des Grenzsteuersatzes als Faktor 0–1 (0.35 = 35 %), nicht in Prozent. Multipliziert den anrechenbaren Abzug zur Steuerersparnis. |
| `homeoffice_pauschale` | string | ja |  |  | 6 EUR × ho_tage_eff in EUR |
| `pendlerpauschale_pro_tag` | string | ja |  |  | 0,38 EUR/km × Entfernung |
| `pendlerpauschale` | string | ja |  |  | Gesamt-Pendlerpauschale aller Buerotage |
| `gesamtabzug` | string | ja |  |  | HO + Pendler-Pauschale in EUR |
| `arbeitnehmer_pauschbetrag` | string | ja |  |  | Arbeitnehmer-Pauschbetrag § 9a EStG (1.230 EUR) |
| `anrechenbarer_abzug` | string | ja |  |  | Teil des Gesamtabzugs ueber dem Pauschbetrag: max(gesamtabzug - 1.230, 0) |
| `steuerersparnis` | string | ja |  |  | Anrechenbarer Abzug × Grenzsteuersatz (nur der Teil ueber dem Arbeitnehmer-Pauschbetrag senkt die Steuer zusaetzlich) |
| `optimale_ho_tage` | integer | ja |  |  | Anzahl HO-Tage fuer maximalen Abzug |
| `optimaler_gesamtabzug` | string | ja |  |  | Höchster erreichbarer Werbungskostenabzug in EUR (Homeoffice-Pauschale plus Pendlerpauschale) über alle Aufteilungen, vor Abzug des Arbeitnehmer-Pauschbetrags. |
| `optimaler_anrechenbarer_abzug` | string | ja |  |  | Optimaler Abzug ueber dem Pauschbetrag |
| `optimale_steuerersparnis` | string | ja |  |  | Steuerersparnis in EUR bei optimaler Aufteilung = optimaler_anrechenbarer_abzug × grenzsteuersatz. 0, wenn auch das Optimum unter dem Arbeitnehmer-Pauschbetrag bleibt. |
| `differenz_zu_optimal` | string | ja |  |  | Abzugs-Differenz Optimum minus Eingabe (roher Werbungskosten-Betrag) |
| `differenz_steuer_zu_optimal` | string |  | "0" |  | Echtes Optimierungspotenzial in EUR Steuerersparnis (optimale minus aktuelle Ersparnis). 0, wenn beide Aufteilungen unter dem § 9a-Pauschbetrag bleiben. |
| `break_even_km` | string | ja |  |  | Ab dieser km lohnt sich Buerotag mehr (~15,8) |
