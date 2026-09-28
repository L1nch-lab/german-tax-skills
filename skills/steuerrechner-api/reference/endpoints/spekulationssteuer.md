# Spekulationssteuer Immobilien

`POST /v1/spekulationssteuer`

Kategorie: Spekulationssteuer

Berechnet die Steuer auf ein privates Veraeusserungsgeschaeft mit Grundstuecken und Immobilien nach §23 EStG.

**Zehnjahresfrist.** §23 Abs. 1 Nr. 1 S. 1 stellt auf einen Zeitraum von 'nicht mehr als zehn Jahren' ab. Ein Verkauf GENAU am Stichtag ist also noch steuerpflichtig, erst der Tag danach ist frei. Massgeblich sind die notariellen Vertraege (obligatorisches Geschaeft), nicht die Grundbucheintraege.

**Freigrenze, kein Freibetrag.** §23 Abs. 3 S. 5 stellt frei, wenn der Gesamtgewinn im Kalenderjahr 'weniger als 1 000 Euro' betragen hat. Bei genau 1.000 EUR ist die Grenze gerissen und der VOLLE Gewinn steuerpflichtig, nicht nur der uebersteigende Teil.

**Persoenlicher Tarif, keine Abgeltungsteuer.** Der Gewinn zaehlt nach §22 Nr. 2 zu den sonstigen Einkuenften und wird im persoenlichen Tarif versteuert. Ausgewiesen wird die MEHRSTEUER: Steuer auf `zve` plus Gewinn minus Steuer auf `zve` allein. Ohne `zve` rechnet der Endpoint ab dem Grundfreibetrag und liefert einen zu niedrigen Betrag.

⚠️ Nicht abgebildet: die Verlustverrechnungsbeschraenkung nach §23 Abs. 3 S. 7-8 (Verluste nur mit Gewinnen aus privaten Veraeusserungsgeschaeften verrechenbar). Ein Verlust wird als solcher ausgewiesen, aber nicht gegen andere Jahre verrechnet.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `kauf_datum` | string | ja |  |  | Datum des notariellen KAUF-Vertrags (obligatorisches Geschaeft), nicht der Grundbucheintrag. Format YYYY-MM-DD. |
| `verkauf_datum` | string | ja |  |  | Datum des notariellen VERKAUFS-Vertrags. Format YYYY-MM-DD. |
| `kaufpreis` | number | ja |  |  | Anschaffungskosten in EUR, inklusive Nebenkosten (Notar, Grunderwerbsteuer, Makler). |
| `verkaufspreis` | number | ja |  |  | Veraeusserungspreis in EUR |
| `verkaufskosten` | number |  | "0" |  | Werbungskosten des Verkaufs in EUR (Makler, Notar, Energieausweis) |
| `afa` | number |  | "0" |  | Bereits in Anspruch genommene AfA in EUR. Mindert die Anschaffungskosten (§23 Abs. 3 S. 4 EStG) und erhoeht damit den Gewinn. Bei vermieteten Objekten fast immer > 0. |
| `eigennutzung` | enum |  | "nie" | nie, durchgehend, verkaufsjahr_2vj | Nutzung zu eigenen Wohnzwecken (§23 Abs. 1 Nr. 1 S. 3 EStG). 'nie' = durchgehend vermietet; 'durchgehend' = seit Anschaffung ausschliesslich selbst bewohnt; 'verkaufsjahr_2vj' = im Jahr der Veraeusserung und in den beiden vorangegangenen Jahren selbst bewohnt. Beide Ausnahmen machen den Verkauf steuerfrei, unabhaengig von der Frist. |
| `zve` | number |  | "0" |  | Zu versteuerndes Einkommen OHNE den Veraeusserungsgewinn, in EUR. Der Gewinn wird nach §22 Nr. 2 EStG im persoenlichen Tarif versteuert – ohne diesen Wert wird die Mehrsteuer ab dem Grundfreibetrag gerechnet und faellt zu niedrig aus. |
| `splitting` | boolean |  | false |  | True = Zusammenveranlagung, Splittingtarif (§32a Abs. 5 EStG) und doppelte Soli-Freigrenze (§3 SolZG). Der uebergebene `zve` ist dann das GEMEINSAM zu versteuernde Einkommen. |

Beispiel:

```json
{
  "afa": 20000,
  "eigennutzung": "nie",
  "kauf_datum": "2018-03-01",
  "kaufpreis": 300000,
  "splitting": false,
  "verkauf_datum": "2024-06-01",
  "verkaufskosten": 15000,
  "verkaufspreis": 420000,
  "zve": 60000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `frist_ende` | string | ja |  |  | Ende der Zehnjahresfrist (§23 Abs. 1 Nr. 1 S. 1 EStG). Ein Verkauf AN diesem Tag ist noch steuerpflichtig. |
| `innerhalb_frist` | boolean | ja |  |  | True wenn der Verkauf innerhalb der Zehnjahresfrist liegt |
| `steuerfrei` | boolean | ja |  |  | True wenn kein steuerpflichtiger Gewinn anfaellt |
| `steuerfrei_grund` | string |  |  |  | Grund der Steuerfreiheit: 'frist' (Zehnjahresfrist abgelaufen), 'eigennutzung' (§23 Abs. 1 Nr. 1 S. 3), 'verlust' oder 'freigrenze' (§23 Abs. 3 S. 5). null wenn steuerpflichtig. |
| `ak_gemindert` | string | ja |  |  | Anschaffungskosten nach Minderung um die AfA (§23 Abs. 3 S. 4) in EUR |
| `gewinn` | string | ja |  |  | Veraeusserungsgewinn nach §23 Abs. 3 S. 1 EStG in EUR (negativ = Verlust) |
| `verlust` | boolean | ja |  |  | True wenn der Gewinn negativ ist |
| `freigrenze_unterschritten` | boolean | ja |  |  | True wenn der Gewinn unter der Freigrenze von 1.000 EUR liegt (§23 Abs. 3 S. 5: 'weniger als 1 000 Euro'). Freigrenze, kein Freibetrag – bei genau 1.000 EUR ist der volle Gewinn steuerpflichtig. |
| `steuer` | string | ja |  |  | Mehrsteuer (ESt + Soli) durch den Gewinn in EUR |
| `soli_anteil` | string | ja |  |  | Darin enthaltener Solidaritaetszuschlag in EUR |
| `effektiver_satz` | string | ja |  |  | Effektiver Steuersatz auf den Gewinn (0.2750 = 27,50 %) |
| `netto_nach_steuer` | string | ja |  |  | Gewinn nach Steuern in EUR |
