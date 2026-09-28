# Kuendigungsfrist-Rechner (§ 622 BGB)

`POST /v1/kuendigungsfrist`

Kategorie: Kuendigungsfrist

Berechnet die gesetzliche Kuendigungsfrist fuer Arbeitsverhaeltnisse und den naechstmoeglichen Beendigungstermin. Arbeitnehmer-Kuendigung: immer 4 Wochen zum 15. oder zum Monatsende (§ 622 Abs. 1 BGB). Arbeitgeber-Kuendigung: verlaengerte Fristen nach Betriebszugehoerigkeit (2 J. -> 1 Monat bis 20 J. -> 7 Monate, jeweils zum Monatsende, § 622 Abs. 2 BGB). Probezeit: 2 Wochen taggenau (§ 622 Abs. 3 BGB). Die Betriebszugehoerigkeit wird zum Zugangsdatum der Kuendigung bemessen.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `kuendigung_durch` | enum | ja |  | arbeitnehmer, arbeitgeber | Wer kuendigt: 'arbeitnehmer' (immer Grundfrist § 622 Abs. 1) oder 'arbeitgeber' (verlaengerte Fristen nach Abs. 2) |
| `beschaeftigt_seit` | string | ja |  |  | Beginn des Arbeitsverhaeltnisses |
| `zugang` | string | ja |  |  | Tag, an dem die Kuendigung zugeht (Stichtag der Fristberechnung) |
| `probezeit` | boolean |  | false |  | True wenn vereinbarte Probezeit laeuft (max. 6 Monate, § 622 Abs. 3) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `jahre_zugehoerigkeit` | integer | ja |  |  | Volle Jahre Betriebszugehoerigkeit zum Zugangsdatum |
| `frist_text` | string | ja |  |  | Frist in Worten inkl. Rechtsgrundlage |
| `frist_monate` | integer | ja |  |  | Frist in Monaten (§ 622 Abs. 2); 0 bei Grundfrist/Probezeit |
| `ende_datum` | string | ja |  |  | Naechstmoeglicher Beendigungstermin |
| `stufe_jahre` | integer | ja |  |  | Angewendete Abs.-2-Stufe in Jahren (0 = Grundfrist Abs. 1) |
| `naechste_stufe_jahre` | integer | ja |  |  | Zugehoerigkeitsjahre bis zur naechsten laengeren AG-Frist (null = Maximum) |
| `naechste_stufe_monate` | integer | ja |  |  | Fristmonate der naechsten Stufe (null = Maximum erreicht) |
