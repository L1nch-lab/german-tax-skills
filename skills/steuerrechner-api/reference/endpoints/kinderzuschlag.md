# Kinderzuschlag-Rechner (§ 6a BKGG)

`POST /v1/kinderzuschlag`

Kategorie: Kinderzuschlag

Berechnet den Kinderzuschlag nach § 6a BKGG: Hoechstbetrag 297 EUR je Kind (inkl. 25 EUR Sofortzuschlag), gemindert um 45 % des Kindeseinkommens (Abs. 3) und um das den Gesamtbedarf der Eltern uebersteigende Eltern-Einkommen (Abs. 6: Erwerbseinkommen 45 %, sonstiges 100 %). Der Gesamtbedarf der Eltern folgt Abs. 5 (Regelbedarf RBSFV 2026 + Mehrbedarf Alleinerziehende § 21 Abs. 3 SGB II + Wohnkosten-Anteil nach dem 12. Existenzminimumbericht), die Einkommensbereinigung § 11b SGB II. Prueft die Mindesteinkommensgrenze (900 EUR Paare / 600 EUR Alleinerziehende, Abs. 1 Nr. 2). Die Buergergeld-Gegenprobe (Abs. 1 Nr. 3) erscheint als Hinweis, nicht als harter Ausschluss – die exakte Pruefung braeuchte eine Wohngeld-Fiktion.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `konstellation` | enum | ja |  | paar, alleinerziehend | 'paar' oder 'alleinerziehend' |
| `kinder_alter` | array<integer> | ja |  |  | Alter jedes Kindes in Jahren (0-17) |
| `kinder_einkommen` | array<number> |  |  |  | Monatliches Einkommen je Kind (Unterhalt/UVG/Halbwaisenrente) in EUR, gleiche Reihenfolge wie kinder_alter; null = alle 0, je Kind 0 bis 50000. Anrechnung 45 % (§ 6a Abs. 3 S. 3 BKGG) |
| `wohnkosten` | number |  | "0" |  | Gesamte Unterkunfts- und Heizkosten des Haushalts in EUR/Monat |
| `brutto_erwerb` | number |  | "0" |  | Erwerbseinkommen der Eltern brutto in EUR/Monat (fuer die Mindesteinkommensgrenze 900/600 EUR, § 6a Abs. 1 Nr. 2 BKGG) |
| `netto_erwerb` | number |  | "0" |  | Erwerbseinkommen der Eltern netto in EUR/Monat (Basis der § 11b-SGB-II-Bereinigung und der 45-%-Anrechnung) |
| `sonstiges_einkommen` | number |  | "0" |  | Sonstiges Eltern-Einkommen in EUR/Monat, ohne Wohngeld/Kindergeld/KiZ (Anrechnung 100 %, § 6a Abs. 6 S. 4 BKGG) |

Beispiel:

```json
{
  "brutto_erwerb": 2600,
  "kinder_alter": [
    4,
    9
  ],
  "konstellation": "paar",
  "netto_erwerb": 1900,
  "wohnkosten": 800
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `status` | string | ja |  |  | anspruch \| kein_mindesteinkommen \| abgeschmolzen |
| `kiz_monat` | string | ja |  |  | Kinderzuschlag gesamt pro Monat |
| `kiz_sechs_monate` | string | ja |  |  | Summe ueber den 6-Monats-Bewilligungszeitraum (§ 6a Abs. 7 BKGG) |
| `hoechstbetrag_gesamt` | string | ja |  |  | Hoechstbetrag 297 EUR × Kinderzahl (inkl. 25 EUR Sofortzuschlag) |
| `kinder` | array<KinderzuschlagKind> | ja |  |  |  |
| `anzahl_kinder` | integer | ja |  |  |  |
| `konstellation` | string | ja |  |  |  |
| `regelbedarf_eltern` | string | ja |  |  | RBS 1 bzw. 2× RBS 2 (RBSFV 2026) |
| `mehrbedarf_eltern` | string | ja |  |  | Mehrbedarf Alleinerziehende (§ 21 Abs. 3 SGB II) |
| `eltern_kdu_anteil` | string | ja |  |  | Eltern-Anteil an den Wohnkosten (12. Existenzminimumbericht) |
| `eltern_kdu_prozent` | string | ja |  |  |  |
| `wohnkosten` | string | ja |  |  |  |
| `gesamtbedarf_eltern` | string | ja |  |  | Gesamtbedarf der Eltern (§ 6a Abs. 5) |
| `mindesteinkommen_grenze` | string | ja |  |  | 900 EUR Paar / 600 EUR alleinerziehend |
| `brutto_gesamt` | string | ja |  |  |  |
| `mindesteinkommen_erfuellt` | boolean | ja |  |  |  |
| `freibetrag_11b` | string | ja |  |  | Erwerbstaetigen-Freibetrag (§ 11b SGB II) |
| `bereinigtes_erwerb` | string | ja |  |  |  |
| `sonstiges_einkommen` | string | ja |  |  |  |
| `anrechenbares_eltern` | string | ja |  |  |  |
| `minderung_eltern` | string | ja |  |  | Minderung des Gesamt-KiZ durch Eltern-Einkommen (§ 6a Abs. 6) |
| `kindergeld_gesamt` | string | ja |  |  | Kindergeld 259 EUR × Kinderzahl (Kontext) |
| `familie_leistung_gesamt` | string | ja |  |  | KiZ + Kindergeld pro Monat |
| `hinweise` | array<string> | ja |  |  | Einordnungen, u.a. Buergergeld-Gegenprobe (§ 6a Abs. 1 Nr. 3) |
