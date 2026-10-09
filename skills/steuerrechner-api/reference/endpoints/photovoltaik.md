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
| `anlagenleistung_kwp` | string | ja |  |  | Bruttoleistung der Anlage in kWp aus der Anfrage, auf 2 Nachkommastellen gerundet. |
| `gebaeudetyp` | string | ja |  |  | "einfamilienhaus", "mehrfamilienhaus" oder "gewerbe" aus der Anfrage. Leerer String, wenn anlagenleistung_kwp oder anschaffungskosten_netto 0 ist. |
| `wohneinheiten` | integer | ja |  |  | Anzahl Wohn- bzw. Gewerbeeinheiten aus der Anfrage. Wirkt nur bei Mehrfamilienhaus und Gewerbe (30 kWp je Einheit), beim Einfamilienhaus ohne Einfluss. 0 bei leerem Ergebnis. |
| `anschaffungskosten_netto` | string | ja |  |  | Netto-Anschaffungskosten der Anlage in EUR (vor Umsatzsteuer) aus der Anfrage. |
| `jaehrlicher_gewinn` | string | ja |  |  | Jährlicher Überschuss der Anlage in EUR aus der Anfrage (Default 800). Grundlage der ESt-Ersparnis. 0 bei leerem Ergebnis. |
| `steuersatz_prozent` | string | ja |  |  | Angenommener Grenzsteuersatz in Prozent (35 = 35 %, Default) für die ESt-Ersparnis. 0 bei leerem Ergebnis. |
| `laufzeit_jahre` | integer | ja |  |  | Betrachtete Lebensdauer der Anlage in Jahren (Default 20), multipliziert die jährliche ESt-Ersparnis. 0 bei leerem Ergebnis. |
| `ust_befreit` | boolean | ja |  |  | True, wenn anlagenleistung_kwp höchstens 30 kWp beträgt; dann gilt der Nullsteuersatz als automatisch erfüllt. Darüber immer false, auch wenn eine Einzelprüfung ihn ergeben könnte. |
| `ust_grund` | string | ja |  |  | Erklärungstext zur USt-Prüfung (30-kWp-Grenze erfüllt oder Einzelprüfung nötig). Leer bei leerem Ergebnis. |
| `ust_ersparnis` | string | ja |  |  | 19 % vom Netto-Preis bei Befreiung |
| `est_befreit` | boolean | ja |  |  | True, wenn anlagenleistung_kwp die ESt-Grenze est_grenze_kwp nicht überschreitet; dann sind Einnahmen und Entnahmen steuerfrei. |
| `est_grund` | string | ja |  |  | Erklärungstext zur ESt-Prüfung mit Anlagenleistung und angewandter Grenze. Leer bei leerem Ergebnis. |
| `est_grenze_kwp` | string | ja |  |  | Angewandte ESt-Grenze in kWp: 30 beim Einfamilienhaus, sonst 30 × wohneinheiten, höchstens 100. Modelliert Neuanlagen; die frühere 15-kWp-Regel für Altanlagen ist nicht abgebildet. |
| `est_ersparnis_jaehrlich` | string | ja |  |  | Jährliche Einkommensteuer-Ersparnis in EUR = jaehrlicher_gewinn × steuersatz_prozent / 100, wenn est_befreit; sonst 0. |
| `est_ersparnis_gesamt` | string | ja |  |  | ESt-Ersparnis ueber Laufzeit |
| `gesamt_ersparnis` | string | ja |  |  | Gesamtersparnis in EUR: USt-Ersparnis bei Anschaffung plus ESt-Ersparnis über die Laufzeit, nicht abgezinst. |
| `brutto_preis_ohne_befreiung` | string | ja |  |  | DEPRECATED (2026.52): Netto-Anschaffungskosten plus USt-Ersparnis in EUR; bei nicht befreiter Anlage steht hier trotz des Namens nur der Nettopreis. Stattdessen preis_mit_regulaerer_ust verwenden. Wird in einer kuenftigen API-Version entfernt. |
| `preis_mit_regulaerer_ust` | string | ja |  |  | Netto-Anschaffungskosten plus 19 % USt in EUR (§ 12 Abs. 1 UStG), unabhängig davon, ob die Anlage unter den Nullsteuersatz fällt. Bei befreiter Anlage ist das der Preis ohne Befreiung. |
| `gesamt_anlagen_warnung` | boolean | ja |  |  | True wenn Anlage > 100 kWp-Gesamtgrenze |
| `empfehlung` | string | ja |  |  | Text je nach Kombination aus USt- und ESt-Befreiung mit den Ersparnisbeträgen, ergänzt um eine Warnung bei mehr als 100 kWp. |
| `kwp_grenze_efh` | string | ja |  |  | 30 kWp pro EFH/Gewerbe |
| `kwp_grenze_mfh_pro_we` | string | ja |  |  | 15 kWp je Wohneinheit MFH |
| `kwp_gesamtgrenze` | string | ja |  |  | 100 kWp Summengrenze pro Steuerpflichtigem |
| `ust_satz` | string | ja |  |  | 19 % Regelsteuersatz |
