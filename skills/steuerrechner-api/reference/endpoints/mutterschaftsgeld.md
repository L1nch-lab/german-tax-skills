# Mutterschaftsgeldrechner (§ 24i SGB V + § 20 MuSchG)

`POST /v1/mutterschaftsgeld`

Kategorie: Mutterschaftsgeld

Berechnet fuer GKV-Mitglieder das Mutterschaftsgeld der Krankenkasse (kalendertaegliches Nettoentgelt der letzten 3 abgerechneten Monate, hoechstens 13 EUR/Kalendertag, § 24i Abs. 2 SGB V) und den Arbeitgeberzuschuss (uebersteigender Betrag, § 20 Abs. 1 MuSchG) ueber die Schutzfrist nach § 3 MuSchG (14 Wochen; 18 Wochen bei Fruehgeburt, Mehrlingsgeburt oder aerztlich festgestellter Behinderung des Kindes – letzteres nur auf Antrag). Liefert als Kontext den 210-EUR-Deckel fuer Frauen ohne GKV-Mitgliedschaft (§ 19 Abs. 2 MuSchG).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `netto_monat` | number | ja |  |  | Durchschnittliches monatliches Nettoentgelt der letzten 3 abgerechneten Kalendermonate vor Beginn der Schutzfrist in EUR |
| `verlaengerte_schutzfrist` | boolean |  | false |  | True bei Fruehgeburt, Mehrlingsgeburt oder aerztlich festgestellter Behinderung des Kindes (§ 3 Abs. 2 S. 2 MuSchG): 12 statt 8 Wochen nach der Entbindung; der dritte Fall verlaengert nur auf Antrag |

Beispiel:

```json
{
  "netto_monat": 2400,
  "verlaengerte_schutzfrist": false
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `netto_monat` | string | ja |  |  |  |
| `netto_kalendertag` | string | ja |  |  | Nettoentgelt je Kalendertag (Monat / 30) |
| `kk_hoechstbetrag_pro_tag` | string | ja |  |  | GKV-Deckel je Kalendertag (§ 24i Abs. 2 SGB V: 13 EUR) |
| `hoechstbetrag_ohne_gkv` | string | ja |  |  | Kontext-Info: Deckel fuer Frauen ohne GKV-Mitgliedschaft, gesamt (§ 19 Abs. 2 S. 1 MuSchG: 210 EUR) – geht in keine Berechnung ein |
| `kk_pro_tag` | string | ja |  |  | Mutterschaftsgeld der Krankenkasse je Kalendertag |
| `ag_zuschuss_pro_tag` | string | ja |  |  | Arbeitgeberzuschuss je Kalendertag (§ 20 Abs. 1 MuSchG) |
| `verlaengerte_schutzfrist` | boolean | ja |  |  |  |
| `schutzfrist_tage` | integer | ja |  |  | Schutzfrist in Kalendertagen (98 bzw. 126) |
| `schutzfrist_wochen` | integer | ja |  |  | Schutzfrist in Wochen (14 bzw. 18) |
| `kk_gesamt` | string | ja |  |  | Krankenkassen-Anteil ueber die gesamte Schutzfrist |
| `ag_gesamt` | string | ja |  |  | Arbeitgeberzuschuss ueber die gesamte Schutzfrist |
| `gesamt` | string | ja |  |  | Gesamtleistung ueber die Schutzfrist |
| `hat_ag_zuschuss` | boolean | ja |  |  | True wenn das Netto ueber 13 EUR/Kalendertag liegt |
