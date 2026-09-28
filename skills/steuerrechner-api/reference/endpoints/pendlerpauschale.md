# Pendlerpauschale / Entfernungspauschale (§9 EStG)

`POST /v1/pendlerpauschale`

Kategorie: Pendlerpauschale

Berechnet die Entfernungspauschale nach §9 Abs. 1 Nr. 4 EStG: 0,38 EUR je Entfernungskilometer (einfache Strecke) ab dem ersten km. Der Jahreshoechstbetrag von 4.500 EUR gilt fuer OePNV, Fahrrad und Mitfahrer, entfaellt aber bei eigenem oder zur Nutzung ueberlassenem Kraftwagen. Liefert zusaetzlich eine Steuerersparnis-Schaetzung.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `entfernung_km` | number | ja |  |  | Einfache Entfernung Wohnung-Arbeitsstaette in km |
| `arbeitstage` | integer |  | 220 |  | Anzahl Arbeitstage pro Jahr (typisch 220) |
| `verkehrsmittel` | enum |  | "eigenes_auto" | eigenes_auto, dienstwagen, familien_auto, oepnv, fahrrad, mitfahrer, zu_fuss | Verkehrsmittel. 'eigenes_auto', 'dienstwagen' oder 'familien_auto' heben den Jahreshoechstbetrag von 4.500 EUR auf. |
| `grenzsteuersatz` | number |  | "30" |  | Persoenlicher Grenzsteuersatz in Prozent fuer Steuerersparnis-Schaetzung |

Beispiel:

```json
{
  "entfernung_km": 25
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `pauschale_pro_km` | string | ja |  |  | Entfernungspauschale in EUR je km |
| `pauschale_pro_tag` | string | ja |  |  | Pauschale fuer eine einfache Strecke in EUR |
| `pauschale_jahr_ungedeckelt` | string | ja |  |  | Jahres-Pauschale vor Anwendung des Hoechstbetrags in EUR |
| `pauschale_jahr` | string | ja |  |  | Jahres-Pauschale nach Hoechstbetrags-Deckelung in EUR |
| `hoechstbetrag_greift` | boolean | ja |  |  | True wenn der Jahreshoechstbetrag von 4.500 EUR angewendet wurde |
| `jahreshoechstbetrag` | string | ja |  |  | Jahreshoechstbetrag 4.500 EUR (entfaellt bei eigenem Kraftwagen) |
| `steuerersparnis_jahr` | string | ja |  |  | Geschaetzte Steuerersparnis pro Jahr auf Basis des Grenzsteuersatzes |
