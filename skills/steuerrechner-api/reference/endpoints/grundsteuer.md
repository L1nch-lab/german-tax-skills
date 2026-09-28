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
| `bodenrichtwert_gemeinde_durchschnitt_eur_m2` | number |  | "0" |  | Gemeinde-Durchschnittsbodenrichtwert (Hessen) |
| `bodenrichtwert_landesdurchschnitt_eur_m2` | number |  | "0" |  | Landesdurchschnitts-Bodenrichtwert (Niedersachsen) |
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
| `bundesland` | string | ja |  |  |  |
| `modell` | string | ja |  |  | 'bundesmodell' \| 'bw_bodenwert' \| 'by_flaechenmodell' \| 'he_flaechen_faktor' \| 'hh_wohnlage' \| 'ni_flaechen_lage' |
| `grundsteuerwert` | string |  |  |  | Grundsteuerwert in EUR (nur Bundesmodell und BW) |
| `messbetrag` | string | ja |  |  | Steuermessbetrag (EUR bei Flaechenmodellen) |
| `steuermesszahl_promille` | string |  |  |  | Steuermesszahl in ‰ (nur Bundesmodell und BW) |
| `hebesatz_prozent` | string | ja |  |  |  |
| `grundsteuer_jahr` | string | ja |  |  | Jahres-Grundsteuer in EUR |
| `jahresrohertrag` | string |  |  |  |  |
| `reinertrag` | string |  |  |  |  |
| `kapitalisierter_reinertrag` | string |  |  |  |  |
| `abgezinster_bodenwert` | string |  |  |  |  |
| `grundmiete_eur_m2` | string |  |  |  |  |
| `mietniveaustufe` | integer |  |  |  |  |
| `nutzungsart` | string |  |  |  |  |
| `aequivalenzbetrag_grund` | string |  |  |  |  |
| `aequivalenzbetrag_gebaeude` | string |  |  |  |  |
| `lagefaktor` | string |  |  |  |  |
| `wohnlage` | string |  |  |  |  |
| `ueberwiegend_wohnen` | boolean |  |  |  |  |
| `ermaessigung_prozent` | string |  |  |  |  |
| `baudenkmal` | boolean |  |  |  |  |
| `hinweise` | array<string> | ja |  |  |  |
