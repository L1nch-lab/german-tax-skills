# Liste aller aktiven gesetzlichen Krankenkassen

`GET /v1/gkv-kassen`

Kategorie: GKV-Zusatzbeitrag

Liefert alle aktiven GKV-Kassen mit IK-Nummer (oder synthetischem Slug-ID), Name, Kassen-Typ und Geltungsbereich. Quelle: gkv-spitzenverband.de PDF + Wayback-Snapshots 2021-2026.

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `kassen` | array<GkvKasseItem> | ja |  |  | Alle aktiven Krankenkassen (aktiv = 1), alphabetisch nach Name sortiert. |
