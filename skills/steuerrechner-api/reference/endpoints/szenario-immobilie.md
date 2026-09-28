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
| `kaufpreis` | string | ja |  |  |  |
| `grunderwerbsteuer` | string | ja |  |  |  |
| `grunderwerbsteuer_prozent` | string | ja |  |  |  |
| `notar_schaetzung` | string | ja |  |  |  |
| `grundbuch_schaetzung` | string | ja |  |  |  |
| `makler_schaetzung` | string | ja |  |  |  |
| `kaufnebenkosten_gesamt` | string | ja |  |  |  |
| `gesamtkosten` | string | ja |  |  |  |
| `grundsteuer_jahr` | string | ja |  |  |  |
| `grundsteuer_modell` | string | ja |  |  |  |
| `hinweise` | array<string> | ja |  |  |  |
