# Rentenpunkte-Rechner (§§ 63 ff. SGB VI)

`POST /v1/rentenpunkte`

Kategorie: Rente

Berechnet Entgeltpunkte (Rentenpunkte) aus dem Bruttoeinkommen: Jahresbrutto (gedeckelt auf die BBG von 101.400 EUR) geteilt durch das vorlaeufige Durchschnittsentgelt 51.944 EUR (SVBezGrV 2026). Liefert den Renten-Gegenwert eines Beitragsjahres (Rentenwert 42,52 EUR ab 01.07.2026) und optional eine Projektion ueber mehrere Beitragsjahre mit konstantem relativem Einkommen.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto` | number | ja |  |  | Rentenversicherungspflichtiges Bruttoeinkommen in EUR |
| `zeitraum` | enum |  | "monat" | monat, jahr | Bezugszeitraum des Bruttoeinkommens |
| `beitragsjahre` | integer |  | 0 |  | Optionale Beitragsjahre mit diesem Einkommen fuer die Renten-Projektion (0 = keine Projektion) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `jahresbrutto` | string | ja |  |  | Jahresbrutto in EUR (Monatswert x 12) |
| `jahresbrutto_angerechnet` | string | ja |  |  | Angerechnetes Jahresbrutto, gedeckelt auf BBG RV 101.400 EUR |
| `bbg_gedeckelt` | boolean | ja |  |  | True wenn das Brutto ueber der BBG lag |
| `entgeltpunkte_jahr` | string | ja |  |  | Entgeltpunkte pro Jahr = Brutto / Durchschnittsentgelt 51.944 EUR |
| `max_entgeltpunkte_jahr` | string | ja |  |  | Maximal erreichbare Entgeltpunkte/Jahr (~1,95 an der BBG) |
| `vergleich_durchschnitt_prozent` | string | ja |  |  | Eigenes Einkommen relativ zum Durchschnittsverdiener in % |
| `rente_pro_jahr_arbeit` | string | ja |  |  | Monatsrente, die EIN Beitragsjahr mit diesem Einkommen bringt (EUR) |
| `rentenwert` | string | ja |  |  | Aktueller Rentenwert 42,52 EUR (ab 01.07.2026) |
| `rentenwert_alt` | string | ja |  |  | Rentenwert bis 30.06.2026 (40,79 EUR) |
| `entgeltpunkte_gesamt` | string | ja |  |  | Projektion: Entgeltpunkte ueber alle angegebenen Beitragsjahre |
| `monatsrente_gesamt` | string | ja |  |  | Projektion: Brutto-Monatsrente aus allen Beitragsjahren in EUR |
