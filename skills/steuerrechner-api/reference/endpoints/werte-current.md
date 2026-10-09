# Werte-Bundle zum heutigen Tag

`GET /v1/werte/current`

Kategorie: Werte-Bundle

Aggregiert alle deutschen Lohn- und Steuerwerte (Sozialversicherung, Einkommensteuer-Tarif, Lohnsteuer-PAP-Hilfsbetraege, Pfaendung, Firmenwagen, 16 Bundeslaender mit KiSt+GrESt, Basiszins-Reihe seit 2018, Sachbezug SvEV, Inland-Reisekostenpauschalen) als 1-Call-Snapshot. ETag-Roundtrip: ETag als If-None-Match zurueckschicken gibt 304 ohne Body (Status pruefen, bevor der Client den Body parst).

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `stichtag` | string | ja |  |  | Aufgeloester Stichtag (ISO YYYY-MM-DD) |
| `jahr` | integer | ja |  |  | Steuerjahr aus Stichtag abgeleitet |
| `sozialversicherung` | WerteBundleSV | ja |  |  | Sozialversicherungswerte für das Jahr des Stichtags: Beitragsbemessungsgrenzen, AN- und AG-Beitragssätze, Minijob-/Midijob-Grenzen und Mindestlohn. Quelle ist die Tabelle steuerjahr_parameter; die Sachsen-Sätze kommen aus der Bundesland-Tabelle ohne Jahresbezug (aktueller Stand), pv_ag folgt pv_an_basis des Jahres. |
| `einkommensteuer` | WerteBundleEStTarif | ja |  |  | Einkommensteuer-Tarif des Stichtagsjahres (Grundfreibetrag, Zonengrenzen und Koeffizienten aus der Tabelle est_tarif), dazu Soli-Freigrenzen, Soli-Satz, Kapitalertragsteuer-Satz und Sparer-Pauschbeträge. |
| `lohnsteuer_pap` | WerteBundleLohnsteuerPAP | ja |  |  | Hilfsbeträge aus dem Lohnsteuer-Programmablaufplan für das Stichtagsjahr: Pauschbeträge, Entlastungsbetrag für Alleinerziehende, Kinderfreibeträge, Vorsorgepauschalen-Maxima und die StKl-5-Grenzen W1 bis W3, alle in EUR pro Jahr. |
| `pfaendung` | WerteBundlePfaendung | ja |  |  | Pfändungsfreigrenzen der Bekanntmachung, die am Stichtag gilt (gueltig_ab <= Stichtag <= gueltig_bis). Gibt es keine passende Bekanntmachung, antwortet der Endpunkt mit 404 PFAENDUNG_NOT_FOUND. |
| `firmenwagen` | WerteBundleFirmenwagen | ja |  |  | Sätze der Firmenwagen-Pauschalversteuerung (Standard, PHEV, BEV, BEV-Listenpreisgrenzen, Zuschlag für Fahrten Wohnung–Arbeit) für das Jahr des Stichtags aus der Tabelle firmenwagen_regelung. |
| `bundeslaender` | array<WerteBundleBundesland> | ja |  |  | Alle 16 Bundeslaender |
| `basiszins_reihe` | array<WerteBundleBasiszinsJahr> | ja |  |  | Basiszins §16 InvStG seit 2018 |
| `sachbezug` | WerteBundleSachbezug | ja |  |  | Sachbezugswerte nach SvEV § 2 für Verpflegung, Unterkunft und Wohnung in EUR. Es werden immer die Werte 2026 geliefert, unabhängig vom Stichtag. |
| `reisekosten_inland` | WerteBundleReisekostenInland | ja |  |  | Inland-Reisekostenpauschalen nach § 9 EStG: Verpflegungspauschalen, Übernachtungspauschalen und Mahlzeitenkürzung in EUR. Konstanten im Code, nicht nach Stichtag unterschieden. |
| `quellen` | array<WerteBundleQuelle> | ja |  |  | Primaerquellen mit URL + Abrufdatum |
