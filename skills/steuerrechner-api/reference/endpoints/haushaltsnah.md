# Haushaltsnahe Leistungen (§ 35a EStG)

`POST /v1/haushaltsnah`

Kategorie: Haushaltsnah

Berechnet die Steuerermaessigung fuer drei Kategorien nach § 35a EStG: Abs. 1 haushaltsnaher Minijob (Cap 510 EUR/Jahr), Abs. 2 Dienstleistungen (Cap 4.000 EUR), Abs. 3 Handwerker (Cap 1.200 EUR). 20 % Ermaessigung auf den Lohn-Anteil; Material ist nicht absetzbar. Cap-Flags pro Kategorie im Response. Voraussetzungen (§ 35a Abs. 5 EStG): Rechnung mit Lohn-Anteil + Bankueberweisung (kein Bar), inlaendischer Haushalt, kein Doppelfoerderungs-Konflikt mit § 35c (energetische Sanierung).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `aufwand_minijob` | number |  | "0" |  | Aufwand haushaltsnaher Minijob (Abs. 1) in EUR/Jahr |
| `aufwand_dienstleistung` | number |  | "0" |  | Aufwand fuer Dienstleistungen (Abs. 2) – Putzfrau, Garten, Pflege. Nur Lohn-Anteil, kein Material. |
| `aufwand_handwerker` | number |  | "0" |  | Aufwand fuer Handwerker (Abs. 3) – Renovierung/Reparatur. Nur Lohn-Anteil, KEIN Material. |

Beispiel:

```json
{
  "aufwand_dienstleistung": 2000,
  "aufwand_handwerker": 3000
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `aufwand_minijob` | string | ja |  |  | Echo des Jahresaufwands für einen Minijob im Haushalt in EUR (Kategorie Abs. 1). |
| `aufwand_dienstleistung` | string | ja |  |  | Echo des Jahresaufwands für haushaltsnahe Dienstleistungen in EUR, nur Lohnanteil (Kategorie Abs. 2). |
| `aufwand_handwerker` | string | ja |  |  | Echo des Jahresaufwands für Handwerkerleistungen in EUR, nur Lohnanteil ohne Material (Kategorie Abs. 3). |
| `total_aufwand` | string | ja |  |  | Summe der drei eingegebenen Aufwände in EUR, ungekappt. |
| `ermaessigung_minijob` | string | ja |  |  | Steuerermäßigung Minijob in EUR = 20 % des Aufwands, höchstens cap_minijob (510). 0 bei Aufwand 0. |
| `ermaessigung_dienstleistung` | string | ja |  |  | Steuerermäßigung Dienstleistungen in EUR = 20 % des Aufwands, höchstens cap_dienstleistung (4.000). 0 bei Aufwand 0. |
| `ermaessigung_handwerker` | string | ja |  |  | Steuerermäßigung Handwerker in EUR = 20 % des Aufwands, höchstens cap_handwerker (1.200). 0 bei Aufwand 0. |
| `total_ermaessigung` | string | ja |  |  | Summe der drei Ermäßigungen in EUR. Wird direkt von der Einkommensteuer abgezogen, nicht vom Einkommen. |
| `ist_gekappt_minijob` | boolean | ja |  |  | True, wenn 20 % des Minijob-Aufwands den Höchstbetrag erreichen oder überschreiten. Auch bei exakt erreichtem Höchstbetrag true. |
| `ist_gekappt_dienstleistung` | boolean | ja |  |  | True, wenn 20 % des Dienstleistungs-Aufwands den Höchstbetrag erreichen oder überschreiten. Auch bei exakt erreichtem Höchstbetrag true. |
| `ist_gekappt_handwerker` | boolean | ja |  |  | True, wenn 20 % des Handwerker-Aufwands den Höchstbetrag erreichen oder überschreiten. Auch bei exakt erreichtem Höchstbetrag true. |
| `empfehlung` | string | ja |  |  | Deutscher Hinweistext in Du-Form: Beispiele bei Ermäßigung 0, Kappungshinweise je gekappter Kategorie, sonst Ersparnis plus Nachweispflichten. Nicht maschinenlesbar. |
| `prozent` | string | ja |  |  | 20 % Ermaessigung |
| `cap_minijob` | string | ja |  |  | 510 EUR § 35a Abs. 1 EStG |
| `cap_dienstleistung` | string | ja |  |  | 4.000 EUR § 35a Abs. 2 EStG |
| `cap_handwerker` | string | ja |  |  | 1.200 EUR § 35a Abs. 3 EStG |
| `max_aufwand_minijob` | string | ja |  |  | 2.550 EUR = 510 / 0,20 |
| `max_aufwand_dienstleistung` | string | ja |  |  | 20.000 EUR = 4.000 / 0,20 |
| `max_aufwand_handwerker` | string | ja |  |  | 6.000 EUR = 1.200 / 0,20 |
