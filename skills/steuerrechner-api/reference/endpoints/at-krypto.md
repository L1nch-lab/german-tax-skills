# Krypto-KESt Oesterreich (§ 27b EStG AT)

`POST /v1/at-krypto`

Kategorie: AT-Krypto

Berechnet die oesterreichische Kapitalertragsteuer auf Kryptowaehrungen nach § 27b EStG (AT) mit fixem KESt-Satz 27,5 % unabhaengig von Haltefrist und Einkommen. ACB-Bewertungsmethode (gleitender Durchschnittspreis, Pflicht seit 01.01.2023). Altbestand-Pruefung: Kauf vor 01.03.2021 + ueber 1 Jahr gehalten = steuerfrei. KESt wird von inlaendischen Plattformen (Bitpanda, Coinfinity) automatisch einbehalten.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `asset` | string | ja |  |  | Asset-Symbol (BTC, ETH, ...) |
| `transaktionen` | array<AtKryptoTransaktion> | ja |  |  | Kauf-Historie fuer ACB |
| `verkaufte_menge` | number | ja |  |  | Verkaufte Menge |
| `verkauf_erloese_eur` | number | ja |  |  | Verkaufserloes in EUR |
| `verkauf_datum` | string | ja |  |  | Verkaufsdatum |

Beispiel:

```json
{
  "asset": "BTC",
  "transaktionen": [
    {
      "datum": "2024-03-15",
      "kurs_eur": 45000,
      "menge": 0.5
    }
  ],
  "verkauf_datum": "2026-04-20",
  "verkauf_erloese_eur": 18000,
  "verkaufte_menge": 0.3
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `asset` | string | ja |  |  |  |
| `verkaufte_menge` | string | ja |  |  |  |
| `verkauf_erloese_eur` | string | ja |  |  |  |
| `kaufdatum_aeltester` | string | ja |  |  |  |
| `verkauf_datum` | string | ja |  |  |  |
| `acb_pro_einheit` | string | ja |  |  | ACB gleitender Durchschnittspreis |
| `anschaffungskosten` | string | ja |  |  |  |
| `gewinn` | string | ja |  |  |  |
| `ist_altbestand` | boolean | ja |  |  | Kauf vor 01.03.2021 + >1 J gehalten = steuerfrei |
| `ist_steuerfrei` | boolean | ja |  |  |  |
| `kesteuer` | string | ja |  |  | KESt 27,5 % auf Gewinn (Neubestand) |
| `netto_erlos` | string | ja |  |  |  |
| `verlust` | string | ja |  |  |  |
| `hinweise` | array<string> | ja |  |  |  |
