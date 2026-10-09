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
| `bereinigtes_netto` | string | ja |  |  | Unterhaltsrechtlich bereinigtes Nettoeinkommen des Pflichtigen in EUR/Monat: nettoeinkommen minus berufskosten, nicht kleiner als 0. Nach diesem Wert wird die Einkommensgruppe der Düsseldorfer Tabelle bestimmt. |
| `berufskosten` | string | ja |  |  | Abgezogene berufsbedingte Aufwendungen in EUR/Monat, übernommen aus der Eingabe berufsbedingte_aufwendungen (negative Werte werden zu 0). Es gibt keinen automatischen Pauschalabzug, ohne Eingabe ist der Wert 0. |
| `einkommensstufe` | integer | ja |  |  | 1-basierte Stufe (1-15) |
| `ergebnisse` | array<KindErgebnisItem> | ja |  |  | Liste mit einem Ergebnisobjekt (KindErgebnisItem) je Kind, in derselben Reihenfolge wie die Eingabeliste kinder. |
| `summe_zahlbetrag` | string | ja |  |  | Summe der Zahlbeträge aller Kinder in EUR/Monat, auf 2 Nachkommastellen gerundet. Das ist der gesamte monatliche Unterhalt laut Tabelle, ohne Kürzung im Mangelfall. |
| `verbleibend_nach_unterhalt` | string | ja |  |  | Dem Pflichtigen verbleibendes Einkommen in EUR/Monat: bereinigtes_netto minus summe_zahlbetrag. Kann negativ werden, wenn der Unterhalt das bereinigte Netto übersteigt. |
| `selbstbehalt` | string | ja |  |  | Angesetzter notwendiger Selbstbehalt des Pflichtigen in EUR/Monat. Abhängig von der Eingabe erwerbstaetig: Konstante SELBSTBEHALT_ERWERBSTAETIG (1450) bzw. SELBSTBEHALT_NICHT_ERWERBSTAETIG (1200). |
| `mangelfall` | boolean | ja |  |  | true, wenn verbleibend_nach_unterhalt unter dem selbstbehalt liegt. Das Flag zeigt den Mangelfall nur an; die Zahlbeträge werden nicht anteilig gekürzt. |
| `mangelfall_hinweis` | string |  |  |  | Fester Hinweistext für den Mangelfall (unter dem Selbstbehalt, Unterhalt kann anteilig gekürzt werden, Fachanwalt fragen). null, wenn mangelfall false ist. |
