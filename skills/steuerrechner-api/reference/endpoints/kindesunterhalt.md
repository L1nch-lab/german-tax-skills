# Kindesunterhalt-Rechner (Duesseldorfer Tabelle 2026)

`POST /v1/kindesunterhalt`

Kategorie: Kindesunterhalt

Berechnet den Kindesunterhalt nach Duesseldorfer Tabelle 2026 (OLG Duesseldorf, gueltig ab 01.01.2026). Optionaler Abzug konkreter berufsbedingter Aufwendungen (Leitlinien NRW 2026 Ziff. 10.2.1: 5-%-Pauschale nur bei fiktiven Einkuenften), ermittelt Einkommensstufe (1-15) und berechnet Zahlbetraege pro Kind (Altersstufen 0-5/6-11/12-17/ab 18). Kindergeld-Anrechnung haelftig, Mangelfallpruefung gegen Selbstbehalt (1.450 EUR erwerbstaetig, 1.200 EUR sonst).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `nettoeinkommen` | number | ja |  |  | Nettoeinkommen des Unterhaltspflichtigen in EUR/Monat |
| `kinder` | array<KindInput> | ja |  |  | Liste der Kinder (max. 10) |
| `kindergeld_empfaenger` | enum | ja |  | pflichtig, berechtigt | 'pflichtig' oder 'berechtigt' |
| `erwerbstaetig` | boolean |  | true |  | True wenn der Pflichtige erwerbstaetig ist |
| `berufsbedingte_aufwendungen` | number |  | "0" |  | Konkrete berufsbedingte Aufwendungen in EUR/Monat. Nach Leitlinien NRW 2026 Ziff. 10.2.1 konkret darzulegen; kein 5-%-Pauschalautomatismus. |

Beispiel:

```json
{
  "erwerbstaetig": true,
  "kinder": [
    {
      "altersstufe": 1
    },
    {
      "altersstufe": 2
    }
  ],
  "kindergeld_empfaenger": "berechtigt",
  "nettoeinkommen": 3500
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bereinigtes_netto` | string | ja |  |  |  |
| `berufskosten` | string | ja |  |  |  |
| `einkommensstufe` | integer | ja |  |  | 1-basierte Stufe (1-15) |
| `ergebnisse` | array<KindErgebnisItem> | ja |  |  |  |
| `summe_zahlbetrag` | string | ja |  |  |  |
| `verbleibend_nach_unterhalt` | string | ja |  |  |  |
| `selbstbehalt` | string | ja |  |  |  |
| `mangelfall` | boolean | ja |  |  |  |
| `mangelfall_hinweis` | string |  |  |  |  |
