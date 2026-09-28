# Buergergeld-Rechner (SGB II)

`POST /v1/buergergeld`

Kategorie: Buergergeld

Berechnet den voraussichtlichen Buergergeld-Anspruch aus Regelbedarf, Mehrbedarfen (§21 SGB II), Kosten der Unterkunft und anrechenbarem Einkommen mit Erwerbstaetigen-Freibetraegen (§11b SGB II, inkl. neuer 10%-Stufe 1.000-1.200/1.500 EUR). Vermoegenspruefung gegen das altersgestaffelte Schonvermoegen nach §12 Abs. 2 SGB II (5.000 EUR bis 30, 10.000 EUR ab 31, 12.500 EUR ab 41, 20.000 EUR ab 51 Jahren, je Person der Bedarfsgemeinschaft); die Vermoegens-Karenzzeit ist zum 30.06.2026 entfallen. Unverbindliche Orientierung, keine Rechtsberatung.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `erwachsene` | integer | ja |  |  | Anzahl Erwachsener im Haushalt (1 = Single, 2 = Paar) |
| `kinder_alter` | array<integer> |  |  |  | Alter der minderjaehrigen Kinder im Haushalt in vollen Jahren (0-17). Volljaehrige Angehoerige bildet der Rechner nicht ab. |
| `erwachsene_alter` | array<integer> |  |  |  | Alter der Erwachsenen in vollen Jahren (18-120) – Basis fuer das altersgestaffelte Schonvermoegen nach § 12 Abs. 2 SGB II. Fehlt die Angabe fuer eine Person, gilt fuer sie der unterste Freibetrag (5.000 EUR). |
| `kaltmiete` | number | ja |  |  | Kaltmiete inkl. kalter Nebenkosten in EUR/Monat |
| `heizkosten` | number | ja |  |  | Heizkosten in EUR/Monat |
| `bruttoeinkommen` | number |  | "0" |  | Brutto-Erwerbseinkommen in EUR/Monat – Basis fuer die Erwerbstaetigen-Freibetraege nach § 11b Abs. 3 SGB II |
| `nettoeinkommen` | number |  | "0" |  | Netto-Erwerbseinkommen in EUR/Monat – wird nach Abzug der Freibetraege auf das Buergergeld angerechnet (§ 11 SGB II) |
| `sonstiges_einkommen` | number |  | "0" |  | Kindergeld, Unterhalt, Wohngeld etc. in EUR/Monat |
| `vermoegen` | number |  | "0" |  | Verwertbares Vermoegen in EUR – Pruefung gegen das altersgestaffelte Schonvermoegen nach § 12 Abs. 2 SGB II |
| `schwanger` | boolean |  | false |  | Schwangerschaft ab 13. Woche (17 % Mehrbedarf, § 21 Abs. 2 SGB II) |
| `alleinerziehend` | boolean |  | false |  | Alleinerziehend (Mehrbedarf nach § 21 Abs. 3 SGB II) |
| `schwerbehindert` | boolean |  | false |  | 35 % Mehrbedarf bei Leistungen zur Teilhabe am Arbeitsleben (§ 21 Abs. 4 SGB II, § 49 SGB IX) – nicht an Merkzeichen G geknuepft |

Beispiel:

```json
{
  "erwachsene": 1,
  "heizkosten": 100,
  "kaltmiete": 500
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `regelbedarf` | string | ja |  |  |  |
| `regelbedarf_details` | array<BuergergeldRegelbedarfDetail> | ja |  |  |  |
| `mehrbedarf` | string | ja |  |  |  |
| `mehrbedarf_details` | array<string> | ja |  |  |  |
| `kdu` | string | ja |  |  |  |
| `kaltmiete` | string | ja |  |  |  |
| `heizkosten` | string | ja |  |  |  |
| `gesamtbedarf` | string | ja |  |  |  |
| `bruttoeinkommen` | string | ja |  |  |  |
| `nettoeinkommen` | string | ja |  |  |  |
| `sonstiges_einkommen` | string | ja |  |  |  |
| `einkommen_gesamt` | string | ja |  |  |  |
| `anrechenbares_einkommen` | string | ja |  |  |  |
| `freibetrag_erwerbseinkommen` | string | ja |  |  |  |
| `freibetrag_details` | array<string> | ja |  |  |  |
| `anspruch_monat` | string | ja |  |  |  |
| `anspruch_jahr` | string | ja |  |  |  |
| `has_anspruch` | boolean | ja |  |  |  |
| `vermoegen` | string | ja |  |  |  |
| `vermoegen_ok` | boolean | ja |  |  |  |
| `vermoegen_grenze` | string | ja |  |  |  |
| `erwachsene` | integer | ja |  |  |  |
| `anzahl_kinder` | integer | ja |  |  |  |
| `haushaltsgroesse` | integer | ja |  |  |  |
| `alleinerziehend` | boolean | ja |  |  |  |
| `schwanger` | boolean | ja |  |  |  |
| `schwerbehindert` | boolean | ja |  |  |  |
| `hinweise` | array<string> | ja |  |  |  |
