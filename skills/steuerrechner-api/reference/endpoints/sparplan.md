# Sparplan- und Zinseszinsrechner

`POST /v1/sparplan`

Kategorie: Sparplan

Berechnet die Entwicklung eines Sparplans oder einer Einmalanlage mit Zinseszins und deutscher Kapitalertragsteuer (25% KapESt + 5,5% Soli + optional Kirchensteuer). Beruecksichtigt Sparerpauschbetrag (1.000/2.000 EUR) und optionale Sparraten-Dynamik.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `startkapital` | number |  | "0" |  | Einmalanlage zu Beginn in EUR |
| `monatliche_sparrate` | number |  | "0" |  | Monatlicher Sparbetrag in EUR |
| `laufzeit_jahre` | integer |  | 10 |  | Laufzeit in Jahren |
| `rendite_pa` | number |  | "7" |  | Erwartete Rendite pro Jahr in Prozent |
| `sparerpauschbetrag` | number |  | "1000" |  | Jaehrlicher Sparerpauschbetrag in EUR (1.000 Einzel / 2.000 Zusammenveranlagung) |
| `kirchensteuer_satz` | number |  | "0" |  | Kirchensteuersatz: 0 (keine), 0.08 (BY/BW), 0.09 (uebrige) |
| `dynamik_pa` | number |  | "0" |  | Jaehrliche Erhoehung der Sparrate in % |
| `fondstyp` | enum |  | "kein_fonds" | kein_fonds, aktienfonds, mischfonds, immobilienfonds, auslands_immobilienfonds | Anlagetyp fuer die Teilfreistellung nach § 20 InvStG (Privatvermoegen): kein_fonds = Tagesgeld/Festgeld/Anleihen (0 %), aktienfonds (30 %), mischfonds (15 %), immobilienfonds (60 %), auslands_immobilienfonds (80 %). Default kein_fonds – ein generischer Sparplan ist nicht per se ein Fonds, deshalb konservativ ohne Teilfreistellung, bis der Anlagetyp genannt wird. |
| `detail` | boolean |  | false |  | Jahresverlauf in Response einschliessen |

Beispiel:

```json
{
  "laufzeit_jahre": 20,
  "monatliche_sparrate": 500,
  "rendite_pa": "7"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `endkapital_brutto` | string | ja |  |  | Endkapital vor Steuern in EUR |
| `endkapital_netto` | string | ja |  |  | Endkapital nach Steuern in EUR |
| `einzahlungen_gesamt` | string | ja |  |  | Summe aller Einzahlungen in EUR |
| `ertraege_brutto` | string | ja |  |  | Brutto-Ertraege (Zinsen/Rendite) in EUR |
| `ertraege_netto` | string | ja |  |  | Netto-Ertraege nach Steuern in EUR |
| `steuer_gesamt` | string | ja |  |  | Kapitalertragsteuer gesamt in EUR |
| `steuersatz_effektiv` | string | ja |  |  | Effektiver Steuersatz inkl. Soli/KiSt in Prozent |
| `fondstyp` | string | ja |  |  | Angewandter Anlagetyp (§ 20 InvStG): kein_fonds/aktienfonds/mischfonds/immobilienfonds/auslands_immobilienfonds |
| `teilfreistellung_prozent` | string | ja |  |  | Angewandte Teilfreistellung in Prozent (§ 20 InvStG), abgeleitet aus fondstyp: 0 (kein_fonds), 15 (misch), 30 (aktien), 60/80 (immobilien). Macht sichtbar, mit welcher Quote steuer_gesamt gerechnet wurde. |
| `jahresverlauf` | array<SparplanJahrModel> |  |  |  | Jaehrliche Entwicklung (nur bei detail=true) |
