# Rentenluecken-Rechner (Annahmen-Modell)

`POST /v1/rentenluecke`

Kategorie: Rente

Berechnet die monatliche Rentenluecke aus heutigem Netto, gewuenschtem Bedarf im Alter (in % des Nettos) und der erwarteten gesetzlichen Bruttorente (pauschaler Netto-Faktor). Daraus: Kapitalbedarf fuer die Entnahmephase, Aufzinsung vorhandenen Kapitals bis zum Renteneintritt und die noetige Monats-Sparrate (nachschuessige Rentenendwert-Formel). Annahmen-Modell – keine Steuer-/SV-Berechnung der Rentenphase.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `netto_heute` | number | ja |  |  | Heutiges monatliches Nettoeinkommen in EUR |
| `rente_brutto` | number | ja |  |  | Erwartete gesetzliche Bruttorente pro Monat in EUR (aus der DRV-Renteninformation) |
| `jahre_bis_rente` | integer | ja |  |  | Jahre bis zum Renteneintritt |
| `bedarf_prozent` | integer |  | 80 |  | Gewuenschter Bedarf im Alter in % des heutigen Nettos |
| `kapital_vorhanden` | number |  | "0" |  | Bereits vorhandenes Vorsorgekapital in EUR |
| `rendite_prozent` | number |  | "6.0" |  | Angenommene Rendite p.a. in % (Anspar- und Bestandsverzinsung) |
| `entnahme_jahre` | integer |  | 20 |  | Geplante Entnahmedauer im Ruhestand in Jahren (Kapitalverzehr) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bedarf_monat` | string | ja |  |  | Gewuenschter Alters-Bedarf/Monat in EUR |
| `rente_netto` | string | ja |  |  | Geschaetzte Netto-Rente (Brutto x pauschaler Netto-Faktor) |
| `luecke_monat` | string | ja |  |  | Monatliche Rentenluecke in EUR (>= 0) |
| `keine_luecke` | boolean | ja |  |  | True wenn die Rente den Bedarf deckt |
| `kapitalbedarf` | string | ja |  |  | Kapitalbedarf = Luecke x 12 x Entnahmejahre (ohne Verzinsung der Entnahme) |
| `kapital_vorhanden_endwert` | string | ja |  |  | Vorhandenes Kapital aufgezinst bis zum Renteneintritt |
| `restbedarf` | string | ja |  |  | Kapitalbedarf minus aufgezinstes Bestandskapital |
| `sparrate_monat` | string | ja |  |  | Noetige Monats-Sparrate (nachschuessige Rentenendwert-Formel) |
| `bedarf_inflationsbereinigt` | string | ja |  |  | Heutiger Bedarf inflationsindexiert zum Renteneintritt (2 % p.a.) |
