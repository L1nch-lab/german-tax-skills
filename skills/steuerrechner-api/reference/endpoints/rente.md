# Gesetzlicher Rentenrechner (§§ 63-68 SGB VI)

`POST /v1/rente`

Kategorie: Rente

Berechnet die voraussichtliche gesetzliche Rente nach Rentenformel (Rentenpunkte × Zugangsfaktor × Rentenwert × Rentenartfaktor). Beruecksichtigt Regelaltersgrenze nach Geburtsjahr (gestaffelt 1947-1963), Abschlag 0,3 % pro Monat vor Regelalter (§ 77 SGB VI) / Zuschlag 0,5 % pro Monat nach Regelalter, Beitragsbemessungsgrenze RV (101.400 EUR/J 2026). Liefert Rentenluecke, ETF-Sparplan-Empfehlung, 4 Szenarien (63/65/67/70) und inflationsbereinigte Kaufkraft.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `geburtsjahr` | integer | ja |  |  | Geburtsjahr (1940-2005) |
| `bisherige_beitragsjahre` | integer | ja |  |  | Bereits geleistete Beitragsjahre |
| `aktuelles_brutto_monat` | number | ja |  |  | Aktuelles monatliches Bruttogehalt in EUR |
| `geplanter_renteneintritt` | integer | ja |  |  | Geplantes Renteneintrittsalter |
| `lohnwachstum` | number |  | "2.5" |  | Angenommenes jaehrl. Lohnwachstum in % |
| `rentenanpassung` | number |  | "1.5" |  | Angenommene jaehrl. Rentenanpassung in % |

Beispiel:

```json
{
  "aktuelles_brutto_monat": 4500,
  "bisherige_beitragsjahre": 15,
  "geburtsjahr": 1985,
  "geplanter_renteneintritt": 67
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `geburtsjahr` | integer | ja |  |  |  |
| `aktuelles_alter` | integer | ja |  |  |  |
| `geplanter_renteneintritt` | integer | ja |  |  |  |
| `bisherige_beitragsjahre` | integer | ja |  |  |  |
| `verbleibende_jahre` | integer | ja |  |  |  |
| `rentenpunkte_bisher` | string | ja |  |  |  |
| `rentenpunkte_projektion` | string | ja |  |  |  |
| `rentenpunkte_gesamt` | string | ja |  |  |  |
| `zugangsfaktor` | string | ja |  |  |  |
| `abschlag_monate` | integer | ja |  |  |  |
| `zuschlag_monate` | integer | ja |  |  |  |
| `abschlag_prozent` | string | ja |  |  |  |
| `zuschlag_prozent` | string | ja |  |  |  |
| `brutto_rente_monat` | string | ja |  |  |  |
| `netto_rente_monat` | string | ja |  |  |  |
| `brutto_rente_jahr` | string | ja |  |  |  |
| `regelaltersgrenze_jahre` | integer | ja |  |  |  |
| `regelaltersgrenze_monate` | integer | ja |  |  |  |
| `letztes_brutto_projektion` | string | ja |  |  |  |
| `letztes_netto_projektion` | string | ja |  |  |  |
| `bedarf_monat` | string | ja |  |  |  |
| `rentenluecke_monat` | string | ja |  |  |  |
| `etf_sparrate_monat` | string | ja |  |  |  |
| `etf_kapital_bedarf` | string | ja |  |  |  |
| `rentenwert` | string | ja |  |  | Aktueller Rentenwert (Stand 2026: 42,52 EUR) |
| `szenarien` | array<RenteSzenarioItem> | ja |  |  |  |
| `inflation_kaufkraft` | string | ja |  |  |  |
| `inflation_jahre` | integer | ja |  |  |  |
| `lohnwachstum` | string | ja |  |  |  |
| `rentenanpassung` | string | ja |  |  |  |
