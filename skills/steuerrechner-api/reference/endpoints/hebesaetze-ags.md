# Hebesatz nach AGS (Path-Variante, Backward-Compat)

`GET /v1/hebesaetze/{ags}`

Kategorie: Hebesaetze

Gibt das Hebesatz-Record einer Gemeinde anhand ihres 8-stelligen Amtlichen Gemeindeschluessels zurueck. Alternativer Zugang zum gleichen Datensatz wie GET /v1/hebesaetze?ags=...

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | path | string | ja | 8-stelliger Amtlicher Gemeindeschluessel |
