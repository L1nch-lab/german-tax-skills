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
| `titel` | string | ja |  |  | Kurze Überschrift zum Ergebnis, z. B. "Vollbefreiung – Sozialleistungsbezug" oder "Beitragspflichtig". |
| `beschreibung` | string | ja |  |  | Erklärender Text zum Ergebnis in Du-Form; beim Härtefall mit verfügbarem Einkommen und Schwellenwert. |
| `ersparnis_monatlich` | string | ja |  |  | Monatliche Ersparnis gegenüber dem vollen Rundfunkbeitrag in EUR: voller Beitrag bei Befreiung oder Abmeldung, Differenz zum ermäßigten Beitrag bei Merkzeichen RF, 0 bei Beitragspflicht. |
| `ersparnis_jaehrlich` | string | ja |  |  | ersparnis_monatlich × 12 in EUR. |
| `beitrag_monatlich` | string | ja |  |  | Nach dem Ergebnis noch zu zahlender Rundfunkbeitrag in EUR pro Monat (0 bei Befreiung, ermäßigter Beitrag bei RF, voller Beitrag bei Beitragspflicht). |
| `rechtsgrundlage` | string | ja |  |  | Norm, auf die sich das Ergebnis stützt, als Text, z. B. "§4 Abs. 1 Nr. 3 RBStV"; bei Sozialleistungen aus dem Katalog der ersten angegebenen Leistung. |
| `dokumente` | array<string> | ja |  |  | Liste der für den Antrag benötigten Nachweise; leere Liste bei Beitragspflicht. |
| `naechster_schritt` | string | ja |  |  | Feste Handlungsempfehlung "Antrag online stellen beim Beitragsservice"; steht unabhängig vom Status in jeder Antwort, auch bei Beitragspflicht. |
| `link` | string | ja |  |  | URL zum offiziellen Antragsformular |
| `fristenhinweis` | string | ja |  |  | Hinweis zu Beginn, Rückwirkung oder Dauer der Befreiung je Ergebnis; leerer String bei Beitragspflicht. |
