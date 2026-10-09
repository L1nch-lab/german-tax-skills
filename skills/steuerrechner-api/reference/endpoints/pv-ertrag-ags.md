# PV-Ertrag einer Gemeinde (kWh je kWp, PVGIS)

`GET /v1/pv-ertrag/{ags}`

Kategorie: PV-Ertrag

Jaehrlicher Standard-PV-Ertrag am geografischen Mittelpunkt der Gemeinde aus PVGIS 5.3 (EU-Kommission/JRC): 1 kWp, 14 % Systemverluste, optimale Neigung und Ausrichtung. Dazu Globalstrahlung auf Modulebene und die Einordnung in die bundesweite Spanne (Min/Median/Max aller ~10.950 Gemeinden). Koordinaten: Destatis-Gemeindeverzeichnis (GV100).

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | path | string | ja | 8-stelliger Amtlicher Gemeindeschluessel oder 5-stellige Postleitzahl. Gehoert die PLZ zu mehreren Gemeinden, kommt 409 mit den Kandidaten. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  | Gemeinde-AGS (8-stellig) |
| `gemeinde_name` | string | ja |  |  | Gemeindename laut Destatis-GV100 |
| `kwh_pro_kwp` | string | ja |  |  | Jahresertrag in kWh je kWp (1 kWp, 14 % Verluste, optimal ausgerichtet) |
| `globalstrahlung_kwh_m2` | string | ja |  |  | Globalstrahlung auf Modulebene, kWh/m2 p.a. |
| `sd_jahr` | string |  |  |  | Standardabweichung der Jahreswerte (PVGIS) |
| `neigung_opt_grad` | integer | ja |  |  | Optimale Modulneigung in Grad |
| `azimut_opt_grad` | integer | ja |  |  | Optimaler Azimut in Grad (0 = Sued) |
| `lat` | number | ja |  |  | Gemeinde-Mittelpunkt (GV100), Breitengrad |
| `lon` | number | ja |  |  | Gemeinde-Mittelpunkt (GV100), Laengengrad |
| `radiation_db` | string | ja |  |  | PVGIS-Strahlungsdatenbank, z. B. PVGIS-SARAH3 |
| `stand` | string | ja |  |  | Abrufdatum des PVGIS-Batches (YYYY-MM-DD) |
| `hinweis` | string |  | "Standard-Vergleichswert am Gemeinde-Mittelpunkt (PVGIS 5.3, EU-Kommission/JRC). Der Ertrag einer realen Anlage haengt von Dachneigung, Ausrichtung, Verschattung und Anlagentechnik ab. Einspeiseverguetung: siehe /v1/eeg-verguetung." |  | Fester Hinweistext: Standard-Vergleichswert am Gemeinde-Mittelpunkt (PVGIS 5.3); der Ertrag einer realen Anlage hängt von Dach, Ausrichtung, Verschattung und Technik ab. |
| `bundesweit` | PvErtragBundesweit | ja |  |  | Einordnung der Gemeinde in die Werte aller Gemeinden der Tabelle: Anzahl, Minimum, Median, Maximum und Perzentil des Jahresertrags. |
