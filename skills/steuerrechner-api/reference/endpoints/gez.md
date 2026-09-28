# GEZ-Befreiungsrechner (§4 RBStV)

`POST /v1/gez`

Kategorie: GEZ-Befreiung

Prueft den Anspruch auf Befreiung vom Rundfunkbeitrag nach §4 Rundfunkbeitragsstaatsvertrag (RBStV). Entscheidungsbaum: 1) Nebenwohnung (§4 Abs. 2a), 2) Pflegeheim/Behinderteneinrichtung, 3) Katalog-Sozialleistung (§4 Abs. 1: Buergergeld, Sozialhilfe, BAfoeG, Asyl, Pflege, Blindenhilfe, Berufsausbildungsbeihilfe etc.), 4) Merkzeichen TBl (Taubblind, Vollbefreiung), 5) Merkzeichen RF (Ermaessigung 6,12 EUR), 6) Haertefall (§4 Abs. 6, knapp ueber Buergergeld-Grenze). Liefert Befreiungs-Status, Ampel, Ersparnis, Rechtsgrundlage und benoetigte Dokumente.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `wohnart` | enum | ja |  | haupt, neben, heim | 'haupt', 'neben' oder 'heim' |
| `hauptwohnung_zahlt` | boolean |  | false |  | Nur bei wohnart='neben': zahlt die Hauptwohnung bereits? |
| `sozialleistungen` | array<enum> |  |  |  | Liste bezogener Sozialleistungs-Keys |
| `schwerbehindertenausweis` | boolean |  | false |  | Schwerbehindertenausweis vorhanden? |
| `merkzeichen` | enum |  |  | tbl, rf | 'tbl' oder 'rf', sonst null |
| `nettoeinkommen` | number |  | "0" |  | Monatliches Nettoeinkommen in EUR (fuer Haertefall) |
| `warmmiete` | number |  | "0" |  | Monatliche Warmmiete in EUR (fuer Haertefall) |
| `kv_pv_beitrag` | number |  | "0" |  | Monatlicher KV+PV-Beitrag in EUR (fuer Haertefall) |

Beispiel:

```json
{
  "sozialleistungen": [
    "buergergeld"
  ],
  "wohnart": "haupt"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `status` | string | ja |  |  | VOLLBEFREIUNG \| ERMAESSIGUNG \| HAERTEFALL \| ABMELDUNG \| BEITRAGSPFLICHTIG |
| `ampel` | string | ja |  |  | GRUEN \| GELB \| ROT |
| `titel` | string | ja |  |  |  |
| `beschreibung` | string | ja |  |  |  |
| `ersparnis_monatlich` | string | ja |  |  |  |
| `ersparnis_jaehrlich` | string | ja |  |  |  |
| `beitrag_monatlich` | string | ja |  |  |  |
| `rechtsgrundlage` | string | ja |  |  |  |
| `dokumente` | array<string> | ja |  |  |  |
| `naechster_schritt` | string | ja |  |  |  |
| `link` | string | ja |  |  | URL zum offiziellen Antragsformular |
| `fristenhinweis` | string | ja |  |  |  |
