# Grunderwerbsteuer-Rechner

`POST /v1/grunderwerbsteuer`

Kategorie: Grunderwerbsteuer

Berechnet die Grunderwerbsteuer beim Immobilienkauf sowie alle Kaufnebenkosten (Notar ca. 1,5%, Grundbuch ca. 0,5%, optional Makler). Liefert zusaetzlich einen Vergleich aller 16 Bundeslaender nach Steuersatz. Steuersaetze Stand 2026 (§1, §9, §11 GrEStG).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `kaufpreis` | number | ja |  |  | Kaufpreis der Immobilie in EUR |
| `bundesland` | enum | ja |  | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland des Kaufobjekts |
| `mit_makler` | boolean |  | false |  | True wenn Maklerprovision anfaellt |
| `makler_prozent` | number |  | "3.57" |  | Maklerprovision in Prozent inkl. MwSt (Standard: 3,57%) |

Beispiel:

```json
{
  "bundesland": "Bayern",
  "kaufpreis": 300000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `kaufpreis` | string | ja |  |  | Kaufpreis der Immobilie in EUR |
| `bundesland` | string | ja |  |  | Bundesland |
| `steuersatz` | string | ja |  |  | Grunderwerbsteuersatz in Prozent |
| `grunderwerbsteuer` | string | ja |  |  | Grunderwerbsteuer in EUR |
| `notarkosten` | string | ja |  |  | Notarkosten in EUR (ca. 1,5%) |
| `notar_prozent` | string | ja |  |  | Notarkosten-Satz in Prozent |
| `grundbuchkosten` | string | ja |  |  | Grundbuchkosten in EUR (ca. 0,5%) |
| `grundbuch_prozent` | string | ja |  |  | Grundbuchkosten-Satz in Prozent |
| `maklerkosten` | string | ja |  |  | Maklerprovision in EUR (0 wenn kein Makler) |
| `makler_prozent` | string | ja |  |  | Maklerprovisions-Satz in Prozent |
| `nebenkosten_gesamt` | string | ja |  |  | Alle Kaufnebenkosten in EUR |
| `nebenkosten_prozent` | string | ja |  |  | Nebenkosten als % des Kaufpreises |
| `kaufpreis_gesamt` | string | ja |  |  | Kaufpreis inkl. aller Nebenkosten in EUR |
| `bundeslaender_vergleich` | array<GrunderwerbsteuerBundeslandItem> | ja |  |  | Vergleich aller Bundeslaender nach Steuersatz sortiert |
