# BAS-IK-Verzeichnis Lookup (echte IK-Nummern, ~1083 Eintraege)

`GET /v1/gkv-ik-verzeichnis`

Kategorie: GKV-Zusatzbeitrag

Schlaegt Institutionskennzeichen (IK) im offiziellen BAS-Verzeichnis nach. Lookup via IK-Nummer (9-stellig) oder Name-Substring (fuzzy). Quelle: ITSG/BAS EDIFACT KOTR-KE-Dateien (Krankenkassen-Verzeichnis). Enthaelt Hauptstellen + Aussenstellen aller 6 Kassentypen (AOK/BKK/Knappschaft/Ersatzkasse/IKK/Landwirt).

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ik` | query | string |  | 9-stellige IK-Nummer fuer exakten Lookup |
| `name` | query | string |  | Name-Substring (fuzzy), mind. 2 Zeichen |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `eintraege` | array<GkvIkVerzeichnisItem> | ja |  |  |  |
