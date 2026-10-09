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
| `regelbedarf` | string | ja |  |  | Summe der Regelbedarfe aller Haushaltsmitglieder in EUR pro Monat (Erwachsene nach Single/Paar, Kinder nach Altersstufe). |
| `regelbedarf_details` | array<BuergergeldRegelbedarfDetail> | ja |  |  | Aufschlüsselung des Regelbedarfs je Person mit Regelbedarfsstufe, Bezeichnung und Betrag. |
| `mehrbedarf` | string | ja |  |  | Summe der Mehrbedarfe (Schwangerschaft, Alleinerziehende, Teilhabe) in EUR pro Monat, gedeckelt auf den maßgebenden Regelbedarf der betroffenen Person; 0 ohne Mehrbedarf. |
| `mehrbedarf_details` | array<string> | ja |  |  | Textzeilen je berücksichtigtem Mehrbedarf mit Prozentsatz und Betrag vor der Deckelung; leere Liste ohne Mehrbedarf. |
| `kdu` | string | ja |  |  | Kosten der Unterkunft in EUR pro Monat: kaltmiete + heizkosten, ohne Angemessenheitsprüfung. |
| `kaltmiete` | string | ja |  |  | Echo der Kaltmiete inklusive kalter Nebenkosten in EUR pro Monat. |
| `heizkosten` | string | ja |  |  | Echo der Heizkosten in EUR pro Monat. |
| `gesamtbedarf` | string | ja |  |  | Bedarf des Haushalts in EUR pro Monat: regelbedarf + mehrbedarf + kdu, vor Anrechnung des Einkommens. |
| `bruttoeinkommen` | string | ja |  |  | Echo des Brutto-Erwerbseinkommens in EUR pro Monat; Bemessungsgrundlage der Erwerbstätigen-Freibeträge. Bei 0 und positivem Netto wird der Freibetrag ersatzweise am Netto berechnet (mit Hinweis). |
| `nettoeinkommen` | string | ja |  |  | Echo des Netto-Erwerbseinkommens in EUR pro Monat; davon wird freibetrag_erwerbseinkommen abgezogen. |
| `sonstiges_einkommen` | string | ja |  |  | Echo des sonstigen Einkommens (z. B. Kindergeld, Unterhalt) in EUR pro Monat; wird ohne Freibetrag voll angerechnet. |
| `einkommen_gesamt` | string | ja |  |  | Netto-Erwerbseinkommen plus sonstiges Einkommen in EUR pro Monat, vor Abzug der Freibeträge. |
| `anrechenbares_einkommen` | string | ja |  |  | Einkommen, das den Bedarf mindert, in EUR pro Monat: Netto minus Freibetrag (nicht unter 0) plus sonstiges Einkommen. |
| `freibetrag_erwerbseinkommen` | string | ja |  |  | Erwerbstätigen-Freibetrag in EUR pro Monat (Grundfreibetrag plus Staffelstufen), bemessen am Brutto; obere Stufengrenze höher, wenn Kinder im Haushalt sind. 0 ohne Erwerbseinkommen. |
| `freibetrag_details` | array<string> | ja |  |  | Textzeilen je Freibetragsstufe mit Spanne und Betrag; leere Liste ohne Erwerbseinkommen. |
| `anspruch_monat` | string | ja |  |  | Rechnerischer Anspruch in EUR pro Monat: gesamtbedarf minus anrechenbares_einkommen, nicht unter 0. Wird bei zu hohem Vermögen nicht auf 0 gesetzt; dann ist nur has_anspruch false. |
| `anspruch_jahr` | string | ja |  |  | anspruch_monat × 12 in EUR; ebenfalls ohne Berücksichtigung der Vermögensprüfung. |
| `has_anspruch` | boolean | ja |  |  | True, wenn anspruch_monat größer 0 ist und das Vermögen die Grenze nicht überschreitet. |
| `vermoegen` | string | ja |  |  | Echo des verwertbaren Vermögens des Haushalts in EUR (Bestand, kein Monatswert). |
| `vermoegen_ok` | boolean | ja |  |  | True, wenn vermoegen kleiner oder gleich vermoegen_grenze ist. |
| `vermoegen_grenze` | string | ja |  |  | Schonvermögen des Haushalts in EUR: Summe der altersgestaffelten Freibeträge je Erwachsenem und Kind. Für Erwachsene ohne Altersangabe zählt die unterste Stufe. |
| `erwachsene` | integer | ja |  |  | Echo der Anzahl Erwachsener: 1 (Single) oder 2 (Paar). |
| `anzahl_kinder` | integer | ja |  |  | Anzahl der Kinder, abgeleitet aus der Länge von kinder_alter. |
| `haushaltsgroesse` | integer | ja |  |  | Personen in der Bedarfsgemeinschaft: erwachsene + anzahl_kinder. |
| `alleinerziehend` | boolean | ja |  |  | Echo der Angabe alleinerziehend; bei true wird der Alleinerziehenden-Mehrbedarf nach Zahl und Alter der minderjährigen Kinder berechnet. |
| `schwanger` | boolean | ja |  |  | Echo der Angabe Schwangerschaft; bei true fließt ein Mehrbedarf von 17 % des maßgebenden Regelbedarfs ein. |
| `schwerbehindert` | boolean | ja |  |  | Echo des Flags für den 35-%-Mehrbedarf bei Leistungen zur Teilhabe am Arbeitsleben oder Eingliederungshilfe. Trotz des Namens nicht an einen Schwerbehindertenausweis oder ein Merkzeichen geknüpft. |
| `hinweise` | array<string> | ja |  |  | Liste von Texthinweisen zur Einordnung, z. B. fehlende Altersangabe, fehlendes Brutto, Vermögen über der Grenze, hohe Kaltmiete; enthält immer die Hinweise zur Wohnkostenprüfung und zur Umbenennung in Grundsicherungsgeld. |
