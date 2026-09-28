# Werte-Bundle zu einem Stichtag

`GET /v1/werte/{stichtag}`

Kategorie: Werte-Bundle

Wie /v1/werte/current, aber fuer einen frei waehlbaren Stichtag im ISO-Format YYYY-MM-DD. Stichtag-Jahr muss in den unterstuetzten Jahren sein ([2024, 2025, 2026]).

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `stichtag` | path | string | ja | Stichtag im Format YYYY-MM-DD |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `stichtag` | string | ja |  |  | Aufgeloester Stichtag (ISO YYYY-MM-DD) |
| `jahr` | integer | ja |  |  | Steuerjahr aus Stichtag abgeleitet |
| `sozialversicherung` | WerteBundleSV | ja |  |  |  |
| `einkommensteuer` | WerteBundleEStTarif | ja |  |  |  |
| `lohnsteuer_pap` | WerteBundleLohnsteuerPAP | ja |  |  |  |
| `pfaendung` | WerteBundlePfaendung | ja |  |  |  |
| `firmenwagen` | WerteBundleFirmenwagen | ja |  |  |  |
| `bundeslaender` | array<WerteBundleBundesland> | ja |  |  | Alle 16 Bundeslaender |
| `basiszins_reihe` | array<WerteBundleBasiszinsJahr> | ja |  |  | Basiszins §16 InvStG seit 2018 |
| `sachbezug` | WerteBundleSachbezug | ja |  |  |  |
| `reisekosten_inland` | WerteBundleReisekostenInland | ja |  |  |  |
| `quellen` | array<WerteBundleQuelle> | ja |  |  | Primaerquellen mit URL + Abrufdatum |
