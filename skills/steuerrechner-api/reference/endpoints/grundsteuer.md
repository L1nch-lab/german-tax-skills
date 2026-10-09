# Grundsteuer-Rechner ab 2025 (Bundesmodell + 5 Landesmodelle)

`POST /v1/grundsteuer`

Kategorie: Grundsteuer

Berechnet die Grundsteuer nach dem fuer das Bundesland gueltigen Modell: Bundesmodell (11 Laender, vereinfachtes Ertragswertverfahren §§252 ff. BewG), Baden-Wuerttemberg (Bodenwertmodell), Bayern (Flaechenmodell), Hessen (Flaechen-Faktor), Hamburg (Wohnlage), Niedersachsen (Flaechen-Lage). Welche Felder im Request zu befuellen sind, haengt vom Modell ab – siehe OpenAPI-Examples. Disclaimer: Orientierungshilfe, kein Bescheid, Verfassungsbeschwerden anhaengig (BFH II B 78/23 + II B 79/23).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bundesland` | enum | ja |  | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Eines der 16 Bundeslaender |
| `hebesatz_prozent` | number | ja |  |  | Kommunaler Hebesatz Grundsteuer B in Prozent |
| `grundstuecksflaeche_m2` | number |  | "0" |  | Gesamte Grundstuecksflaeche in m² |
| `gebaeudeflaeche_m2` | number |  | "0" |  | Gebaeude-/Wohnflaeche in m² (Bayern/Hessen/Hamburg/NI) |
| `wohnflaeche_m2` | number |  | "0" |  | Wohnflaeche in m² (Bundesmodell) |
| `bodenrichtwert_eur_m2` | number |  | "0" |  | Bodenrichtwert Stichtag 01.01.2022 (Bundesmodell/BW) |
| `bodenrichtwert_lage_eur_m2` | number |  | "0" |  | Bodenrichtwert der Lage (Hessen/Niedersachsen) |
| `bodenrichtwert_gemeinde_durchschnitt_eur_m2` | number |  | "0" |  | Durchschnittsbodenwert der Gemeinde (Hessen § 7 HGrStG, Niedersachsen § 5 NGrStG: Median der Bodenrichtwerte der Gemeinde) |
| `bodenrichtwert_landesdurchschnitt_eur_m2` | number |  | "0" |  | Veraltet seit 2026.52. Niedersachsen rechnet mit dem Durchschnittsbodenwert der Gemeinde; ist bodenrichtwert_gemeinde_durchschnitt_eur_m2 leer, wird dieser Wert als solcher verwendet. |
| `mietniveaustufe` | integer |  | 3 |  | Mietniveaustufe 1-7 nach MietNEinV (nur Bundesmodell) |
| `nutzungsart` | enum |  | "wohnen" | wohnen, gemischt, gewerbe, unbebaut, landwirtschaft | Nutzungsart (nur Bundesmodell) |
| `ueberwiegend_wohnen` | boolean |  | true |  | True bei ueberwiegender Wohnnutzung (BW/BY/HE/HH/NI) |
| `wohnlage` | enum |  | "normal" | normal, gut | Wohnlage (nur Hamburg) |
| `sozialer_wohnungsbau_oder_denkmal` | boolean |  | false |  | 25 % Messzahl-Abschlag fuer sozialen Wohnungsbau / foerderfaehigen Wohnraum (§15 Abs. 2-4 GrStG). Fuer reine Baudenkmaeler stattdessen baudenkmal=true (10 %). |
| `baudenkmal` | boolean |  | false |  | 10 % Messzahl-Abschlag fuer Baudenkmaeler (§15 Abs. 5 GrStG). Stapelbar mit sozialer_wohnungsbau_oder_denkmal. |

Beispiel:

```json
{
  "bodenrichtwert_eur_m2": 350,
  "bundesland": "Nordrhein-Westfalen",
  "grundstuecksflaeche_m2": 400,
  "hebesatz_prozent": 490,
  "mietniveaustufe": 3,
  "wohnflaeche_m2": 120
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bundesland` | string | ja |  |  | Bundesland aus der Anfrage. Bestimmt das Rechenmodell (Bundesmodell oder eines der Landesmodelle BW, BY, HE, HH, NI). |
| `modell` | string | ja |  |  | 'bundesmodell' \| 'bw_bodenwert' \| 'by_flaechenmodell' \| 'he_flaechen_faktor' \| 'hh_wohnlage' \| 'ni_flaechen_lage' |
| `grundsteuerwert` | string |  |  |  | Grundsteuerwert in EUR (nur Bundesmodell und BW) |
| `messbetrag` | string | ja |  |  | Steuermessbetrag (EUR bei Flaechenmodellen) |
| `steuermesszahl_promille` | string |  |  |  | Steuermesszahl in ‰ (nur Bundesmodell und BW) |
| `hebesatz_prozent` | string | ja |  |  | Kommunaler Grundsteuer-Hebesatz in Prozent, wie übergeben (490 = 490 %). Grundsteuer = Messbetrag × Hebesatz / 100. |
| `grundsteuer_jahr` | string | ja |  |  | Jahres-Grundsteuer in EUR |
| `jahresrohertrag` | string |  |  |  | Nur Bundesmodell: Jahresrohertrag in EUR = Wohnfläche × Grundmiete (EUR/m² und Monat) × 12. Sonst null. |
| `reinertrag` | string |  |  |  | Nur Bundesmodell: Jahresrohertrag in EUR abzüglich pauschaler Bewirtschaftungskosten (23 % Wohnen, 19 % bei nutzungsart "gewerbe"). Sonst null. |
| `kapitalisierter_reinertrag` | string |  |  |  | Nur Bundesmodell: Reinertrag × fester Vervielfältiger 20 in EUR. Vereinfachung statt Liegenschaftszins und Restnutzungsdauer. Sonst null. |
| `abgezinster_bodenwert` | string |  |  |  | Nur Bundesmodell: Grundstücksfläche × Bodenrichtwert × pauschaler Faktor 0,45 in EUR. Vereinfachte Näherung, keine echte Abzinsung. Sonst null. |
| `grundmiete_eur_m2` | string |  |  |  | Nur Bundesmodell: angesetzte monatliche Grundmiete in EUR/m², vereinfacht aus einem Basiswert je Bundesland × Faktor der Mietniveaustufe. Sonst null. |
| `mietniveaustufe` | integer |  |  |  | Nur Bundesmodell: verwendete Mietniveaustufe 1 bis 7 (3 = Normalstufe, Default). Sonst null. |
| `nutzungsart` | string |  |  |  | Nur Bundesmodell: verwendete Nutzungsart ("wohnen", "gemischt", "gewerbe", "unbebaut", "landwirtschaft"). Nur "gewerbe" ändert Bewirtschaftungskosten und Messzahl, alle anderen rechnen wie Wohnen. Sonst null. |
| `aequivalenzbetrag_grund` | string |  |  |  | Nur Flächenmodelle (BY, HE, HH, NI): Grundstücksfläche × 0,04 EUR/m² in EUR, vor Lagefaktor. Sonst null. |
| `aequivalenzbetrag_gebaeude` | string |  |  |  | Nur Flächenmodelle (BY, HE, HH, NI): Gebäudefläche × 0,50 EUR/m² × Ermäßigungsfaktor in EUR (Wohnen 0,7; BY zusätzlich Denkmal/sozialer Wohnungsbau; HH Wohnlage), vor Lagefaktor. Sonst null. |
| `lagefaktor` | string |  |  |  | Nur Hessen und Niedersachsen: (Bodenrichtwert Lage / Vergleichs-Bodenrichtwert) hoch 0,3, im Code auf 0,5 bis 1,5 begrenzt und auf 4 Stellen gerundet. Multipliziert die Summe beider Äquivalenzbeträge. Sonst null. |
| `wohnlage` | string |  |  |  | Nur Hamburg: verwendete Wohnlage "normal" oder "gut". Wirkt nur bei ueberwiegend_wohnen=true. Sonst null. |
| `ueberwiegend_wohnen` | boolean |  |  |  | Echo des Eingabeflags in den Landesmodellen (BW, BY, HE, HH, NI). Bei true wird der Wohnabschlag angewandt. Beim Bundesmodell null, weil es das Flag nicht verwendet; dort steuert nutzungsart die Messzahl. |
| `ermaessigung_prozent` | string |  |  |  | Nur Baden-Württemberg: Summe der Messzahl-Ermäßigungen in Prozentpunkten (Wohnen 30, Förderung 25, Kulturdenkmal 10), bezogen auf die Messzahl 1,30 ‰. Sonst null. |
| `baudenkmal` | boolean |  |  |  | Echo des Denkmal-Flags beim Bundesmodell, in Baden-Württemberg und Bayern. In Hessen, Hamburg und Niedersachsen null, dort ist das Feld keine Eingabe. |
| `hinweise` | array<string> | ja |  |  | Liste von Texten: zuerst vier feste Disclaimer (Orientierungshilfe, anhängige Verfahren, Übernachweis, keine Beratung), danach modellspezifische Hinweise wie angewandte Abschläge oder Lagefaktor. |
