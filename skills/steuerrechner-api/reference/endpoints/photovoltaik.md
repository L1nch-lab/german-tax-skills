# Photovoltaik-Steuer-Rechner (§ 12 Abs. 3 UStG + § 3 Nr. 72 EStG)

`POST /v1/photovoltaik`

Kategorie: Photovoltaik

Prueft Nullsteuersatz USt (§ 12 Abs. 3 UStG, automatisch bis 30 kWp) und Einkommensteuer-Befreiung (§ 3 Nr. 72 EStG, 30 kWp pro EFH/Gewerbe bzw. 15 kWp je Wohneinheit MFH, max 100 kWp Summe). Berechnet USt-Ersparnis bei Anschaffung und ESt-Ersparnis ueber Laufzeit (default 20 Jahre).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anlagenleistung_kwp` | number | ja |  |  | Bruttoleistung der Anlage in kWp (lt. Marktstammdatenregister) |
| `gebaeudetyp` | enum |  | "einfamilienhaus" | einfamilienhaus, mehrfamilienhaus, gewerbe | 'einfamilienhaus' / 'mehrfamilienhaus' / 'gewerbe' |
| `wohneinheiten` | integer |  | 1 |  | Anzahl Wohn- bzw. Gewerbeeinheiten (relevant bei Mehrfamilienhaus und Gewerbe, § 3 Nr. 72 EStG: 30 kWp je Einheit, max. 100 kWp) |
| `anschaffungskosten_netto` | number |  | "15000" |  | Netto-Anschaffungskosten in EUR (vor USt) |
| `jaehrlicher_gewinn` | number |  | "800" |  | Jaehrlicher Ueberschuss in EUR (Einspeisung + Eigenverbrauchs-Wert minus Wartung) |
| `steuersatz_prozent` | number |  | "35" |  | Marginal-Steuersatz in Prozent |
| `laufzeit_jahre` | integer |  | 20 |  | PV-Lebensdauer fuer Total-Berechnung |

Beispiel:

```json
{
  "anlagenleistung_kwp": 10,
  "gebaeudetyp": "einfamilienhaus"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anlagenleistung_kwp` | string | ja |  |  |  |
| `gebaeudetyp` | string | ja |  |  |  |
| `wohneinheiten` | integer | ja |  |  |  |
| `anschaffungskosten_netto` | string | ja |  |  |  |
| `jaehrlicher_gewinn` | string | ja |  |  |  |
| `steuersatz_prozent` | string | ja |  |  |  |
| `laufzeit_jahre` | integer | ja |  |  |  |
| `ust_befreit` | boolean | ja |  |  |  |
| `ust_grund` | string | ja |  |  |  |
| `ust_ersparnis` | string | ja |  |  | 19 % vom Netto-Preis bei Befreiung |
| `est_befreit` | boolean | ja |  |  |  |
| `est_grund` | string | ja |  |  |  |
| `est_grenze_kwp` | string | ja |  |  |  |
| `est_ersparnis_jaehrlich` | string | ja |  |  |  |
| `est_ersparnis_gesamt` | string | ja |  |  | ESt-Ersparnis ueber Laufzeit |
| `gesamt_ersparnis` | string | ja |  |  |  |
| `brutto_preis_ohne_befreiung` | string | ja |  |  |  |
| `gesamt_anlagen_warnung` | boolean | ja |  |  | True wenn Anlage > 100 kWp-Gesamtgrenze |
| `empfehlung` | string | ja |  |  |  |
| `kwp_grenze_efh` | string | ja |  |  | 30 kWp pro EFH/Gewerbe |
| `kwp_grenze_mfh_pro_we` | string | ja |  |  | 15 kWp je Wohneinheit MFH |
| `kwp_gesamtgrenze` | string | ja |  |  | 100 kWp Summengrenze pro Steuerpflichtigem |
| `ust_satz` | string | ja |  |  | 19 % Regelsteuersatz |
