# Policenvergleich – Bruttopolice gegen Nettopolice

`POST /v1/policenvergleich`

Kategorie: Altersvorsorgedepot

Vergleicht die Kapitalentwicklung einer privaten Rentenversicherung als Bruttopolice (Provisionstarif) und als Nettopolice (Honorartarif) bei gleichen Beiträgen, Zuzahlungen, Entnahmen und Rendite. Tagesgenaue Simulation: Alpha (Abschlusskosten, verteilt auf die Beitragstermine), Beta (je Beitrag), Gamma, Kappa, Fonds- und Transaktionskosten (täglich abgegrenzt, am Monatsende gebucht), Rückvergütungen, Beitragsdynamik, Gamma-Staffeln und Kostendeckel. Liefert Guthaben, nominale Kosten je Kostenart, entgangene Erträge, Guthabenvorteil, Kostenersparnis nach externem Honorar und den Jahresverlauf. Alle Kosten sind Tarifeingaben; Steuern, Garantien und Rentenphase sind nicht abgebildet. Fehlercode COSTS_EXCEED_BALANCE (422), wenn eine Kostenbuchung das Guthaben übersteigt.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `versicherungsbeginn` | string | ja |  |  | Vertragsbeginn, immer der Erste eines Monats. |
| `laufzeit_jahre` | integer | ja |  |  | Laufzeit in ganzen Jahren |
| `monatsbeitrag` | number | ja |  |  | Monatlicher Grundbeitrag in EUR. Bei anderer Zahlweise wird das Vielfache fällig. |
| `zahlweise` | enum |  | "monatlich" | monatlich, vierteljaehrlich, halbjaehrlich, jaehrlich | Beitragszahlweise |
| `rendite_prozent` | number | ja |  |  | Angenommene Bruttorendite in Prozent pro Jahr, vor Fondskosten. |
| `dynamik_prozent` | number |  | "0" |  | Jährliche Beitragserhöhung in Prozent, jeweils zum Vertragsjahr. |
| `einmalbeitrag` | number |  | "0" |  | Einmalbeitrag am Versicherungsbeginn in EUR. |
| `stichtag` | string |  |  |  | Berechnungsstichtag. Ohne Angabe das Vertragsende (letzter Tag vor dem nominellen Ablauf). |
| `zuzahlungen` | array<PolicenEreignis> |  |  |  | Zuzahlungen, höchstens eine je Tag. |
| `entnahmen` | array<PolicenEreignis> |  |  |  | Teilentnahmen. Ausgeführt nur, wenn danach in beiden Tarifen mindestens mindest_restguthaben bleibt, sonst abgelehnt (in beiden Tarifen). |
| `mindest_restguthaben` | number |  | "250" |  | Mindestguthaben nach einer Teilentnahme in EUR. |
| `bruttotarif` | BruttotarifKosten | ja |  |  | Kosten der Bruttopolice (Provisionstarif) |
| `nettotarif` | NettotarifKosten | ja |  |  | Kosten der Nettopolice (Honorartarif) |
| `honorar_eur` | number |  | "0" |  | Extern gezahltes Beratungshonorar zur Nettopolice in EUR. Mindert nur die nominale Kostenersparnis, nicht das Guthaben. |
| `honorar_zahlweise` | enum |  | "einmalig" | einmalig, raten | Zahlungsmodell des Honorars |
| `honorar_raten` | integer |  | 12 |  | Anzahl monatlicher Raten bei honorar_zahlweise raten. |
| `honorar_erste_zahlung` | string |  |  |  | Datum der ersten Honorarzahlung. Ohne Angabe der Versicherungsbeginn. |

Beispiel:

```json
{
  "bruttotarif": {
    "alpha_prozent": 2.5,
    "alpha_zuzahlung_prozent": 2,
    "beta_prozent": 7,
    "fondskosten_prozent": 0.2,
    "gamma_prozent": 0.3,
    "kappa_eur_jahr": 24
  },
  "laufzeit_jahre": 36,
  "monatsbeitrag": 200,
  "nettotarif": {
    "beta_prozent": 2,
    "fondskosten_prozent": 0.2,
    "gamma_prozent": 0.3,
    "kappa_eur_jahr": 36,
    "transaktionskosten_prozent": 0.05
  },
  "rendite_prozent": 6,
  "versicherungsbeginn": "2026-01-01"
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `vertragsende` | string | ja |  |  | Letzter Tag vor dem nominellen Ablauf (Monatsultimo). |
| `stichtag` | string | ja |  |  | Angewandter Berechnungsstichtag (höchstens das Vertragsende). |
| `zwischenstand` | boolean | ja |  |  | true, wenn der Stichtag vor dem Vertragsende liegt. |
| `brutto` | PolicenTarif | ja |  |  | Ergebnis der Bruttopolice (Provisionstarif). |
| `netto` | PolicenTarif | ja |  |  | Ergebnis der Nettopolice (Honorartarif). |
| `vergleich` | PolicenVergleichKennzahlen | ja |  |  | Vergleichskennzahlen Netto gegen Brutto. |
| `entnahmen` | array<PolicenEntnahme> | ja |  |  | Prüfprotokoll aller angefragten Teilentnahmen. |
| `aktuell_entnehmbar` | string | ja |  |  | Zum Stichtag in beiden Tarifen entnehmbarer Betrag über dem Mindest-Restguthaben, in EUR. |
| `jahresverlauf` | array<PolicenVerlaufJahr> | ja |  |  | Guthaben beider Tarife am Ende jedes Vertragsjahrs, letzter Eintrag zum Stichtag. |
