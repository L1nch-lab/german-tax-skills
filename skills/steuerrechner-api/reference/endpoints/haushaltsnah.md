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
| `aufwand_minijob` | string | ja |  |  |  |
| `aufwand_dienstleistung` | string | ja |  |  |  |
| `aufwand_handwerker` | string | ja |  |  |  |
| `total_aufwand` | string | ja |  |  |  |
| `ermaessigung_minijob` | string | ja |  |  |  |
| `ermaessigung_dienstleistung` | string | ja |  |  |  |
| `ermaessigung_handwerker` | string | ja |  |  |  |
| `total_ermaessigung` | string | ja |  |  |  |
| `ist_gekappt_minijob` | boolean | ja |  |  |  |
| `ist_gekappt_dienstleistung` | boolean | ja |  |  |  |
| `ist_gekappt_handwerker` | boolean | ja |  |  |  |
| `empfehlung` | string | ja |  |  |  |
| `prozent` | string | ja |  |  | 20 % Ermaessigung |
| `cap_minijob` | string | ja |  |  | 510 EUR § 35a Abs. 1 EStG |
| `cap_dienstleistung` | string | ja |  |  | 4.000 EUR § 35a Abs. 2 EStG |
| `cap_handwerker` | string | ja |  |  | 1.200 EUR § 35a Abs. 3 EStG |
| `max_aufwand_minijob` | string | ja |  |  | 2.550 EUR = 510 / 0,20 |
| `max_aufwand_dienstleistung` | string | ja |  |  | 20.000 EUR = 4.000 / 0,20 |
| `max_aufwand_handwerker` | string | ja |  |  | 6.000 EUR = 1.200 / 0,20 |
