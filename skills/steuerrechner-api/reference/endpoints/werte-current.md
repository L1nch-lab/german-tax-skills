# Werte-Bundle zum heutigen Tag

`GET /v1/werte/current`

Kategorie: Werte-Bundle

Aggregiert alle deutschen Lohn- und Steuerwerte (Sozialversicherung, Einkommensteuer-Tarif, Lohnsteuer-PAP-Hilfsbetraege, Pfaendung, Firmenwagen, 16 Bundeslaender mit KiSt+GrESt, Basiszins-Reihe seit 2018, Sachbezug SvEV, Inland-Reisekostenpauschalen) als 1-Call-Snapshot. ETag-Roundtrip: ETag als If-None-Match zurueckschicken gibt 304 ohne Body (Status pruefen, bevor der Client den Body parst).

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
