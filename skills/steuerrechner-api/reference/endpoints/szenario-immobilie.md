# Bundle: Immobilienkauf (GrESt + Grundsteuer + Nebenkosten)

`POST /v1/szenario/immobilie`

Kategorie: Szenario-Bundles

Aggregiert Grunderwerbsteuer, laufende Jahres-Grundsteuer und Kaufnebenkosten (Notar, Grundbuch, optional Makler) in einem Aufruf. Die Grundsteuer wird modellabhaengig mit den vorhandenen Eingaben berechnet; fehlende modellspezifische Parameter werden mit plausiblen Defaults gefuellt (z.B. Lagefaktor 1 in HE/NI).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `kaufpreis` | number | ja |  |  | Kaufpreis der Immobilie in EUR |
| `bundesland` | enum | ja |  | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland des Kaufobjekts – bestimmt GrESt-Satz (§ 11 GrEStG) und Grundsteuer-Modell |
| `grundstuecksflaeche_m2` | number |  | "0" |  | Grundstuecksflaeche in m² (fuer die Grundsteuer-Schaetzung, 0 = keine) |
| `wohnflaeche_m2` | number |  | "0" |  | Wohnflaeche in m² (fuer die Grundsteuer-Schaetzung, 0 = keine) |
| `bodenrichtwert_eur_m2` | number |  | "0" |  | Bodenrichtwert in EUR/m² (Bundesmodell/Bodenwertmodell; 0 = Pauschal-Schaetzung) |
| `hebesatz_grundsteuer_prozent` | number |  | "470" |  | Grundsteuer-B-Hebesatz der Gemeinde in Prozent |
| `mit_makler` | boolean |  | false |  | True wenn Maklerprovision anfaellt |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `kaufpreis` | string | ja |  |  | Kaufpreis der Immobilie in EUR aus der Anfrage. |
| `grunderwerbsteuer` | string | ja |  |  | Grunderwerbsteuer in EUR = Kaufpreis × Steuersatz des Bundeslands, aus dem Grunderwerbsteuer-Rechner. |
| `grunderwerbsteuer_prozent` | string | ja |  |  | Grunderwerbsteuersatz des Bundeslands in Prozent (z. B. 3.5 = 3,5 %). |
| `notar_schaetzung` | string | ja |  |  | Pauschale Schätzung der Notarkosten in EUR: 1,5 % des Kaufpreises. Keine Gebührenberechnung. |
| `grundbuch_schaetzung` | string | ja |  |  | Pauschale Schätzung der Grundbuchkosten in EUR: 0,5 % des Kaufpreises. |
| `makler_schaetzung` | string | ja |  |  | Maklerprovision in EUR: 3,57 % des Kaufpreises (fester Default, im Bundle nicht einstellbar), wenn mit_makler=true, sonst 0. |
| `kaufnebenkosten_gesamt` | string | ja |  |  | Summe der Kaufnebenkosten in EUR: Grunderwerbsteuer + Notar + Grundbuch + Makler. |
| `gesamtkosten` | string | ja |  |  | Kaufpreis plus Kaufnebenkosten in EUR. Ohne laufende Grundsteuer. |
| `grundsteuer_jahr` | string | ja |  |  | Geschätzte jährliche Grundsteuer in EUR nach dem Modell des Bundeslands, mit vereinfachten Defaults (z. B. Lagefaktor 1 in HE/NI, Wohnlage normal in HH). 0, wenn grundstuecksflaeche_m2 0 ist oder die Modellrechnung einen Fehler wirft (Grund dann in hinweise). |
| `grundsteuer_modell` | string | ja |  |  | Name des Grundsteuermodells des Bundeslands ("bundesmodell", "bw_bodenwert", "by_flaechenmodell", "he_flaechen_faktor", "hh_wohnlage", "ni_flaechen_lage"). Wird auch gesetzt, wenn keine Grundsteuer berechnet wurde. |
| `hinweise` | array<string> | ja |  |  | Liste fester Texte zum Bundle und zu den Pauschalschätzungen, plus ein Hinweis, wenn die Grundsteuer mangels Grundstücksfläche nicht berechnet wurde, oder mit dem Grund, wenn die Modellrechnung einen Fehler wirft. |
