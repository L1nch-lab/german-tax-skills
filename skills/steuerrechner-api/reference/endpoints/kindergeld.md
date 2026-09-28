# Kindergeldrechner (§ 66 EStG)

`POST /v1/kindergeld`

Kategorie: Kindergeld

Berechnet das monatliche und jaehrliche Kindergeld nach § 66 Abs. 1 EStG. Seit 2023 gilt ein einheitlicher Satz je Kind (2026: 259 EUR, 2025: 255 EUR, 2024: 250 EUR); es gibt keine Staffelung nach Kinderzahl mehr. Liefert zusaetzlich den Kinderfreibetrag-Gesamtwert (§ 32 Abs. 6 EStG) als Kontext-Info – die Guenstigerpruefung Kindergeld vs. Freibetrag macht das Finanzamt bei der Veranlagung automatisch.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `anzahl_kinder` | integer | ja |  |  | Anzahl der kindergeldberechtigten Kinder |
| `jahr` | integer |  | 2026 |  | Bezugsjahr (2024-2026); Satz je Kind: 250/255/259 EUR (§ 66 Abs. 1 EStG) |

Beispiel:

```json
{
  "anzahl_kinder": 2,
  "jahr": 2026
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `jahr` | integer | ja |  |  | Angewendetes Bezugsjahr |
| `anzahl_kinder` | integer | ja |  |  |  |
| `satz_pro_kind` | string | ja |  |  | Kindergeld je Kind und Monat (§ 66 Abs. 1 EStG) |
| `kindergeld_monat` | string | ja |  |  | Kindergeld gesamt pro Monat |
| `kindergeld_jahr` | string | ja |  |  | Kindergeld gesamt pro Jahr |
| `kinderfreibetrag_gesamt` | string |  |  |  | Kinderfreibetrag inkl. BEA, beide Elternteile (§ 32 Abs. 6 EStG) – Kontext-Info fuer die Guenstigerpruefung, null wenn fuer das Jahr nicht hinterlegt |
