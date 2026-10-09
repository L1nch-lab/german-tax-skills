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
| `asset` | string | ja |  |  | Echo des Asset-Symbols (z. B. BTC). Reiner Bezeichner ohne Einfluss auf die Rechnung. |
| `verkaufte_menge` | string | ja |  |  | Echo der verkauften Menge in Einheiten des Assets. Anschaffungskosten = verkaufte_menge × gleitender Durchschnittspreis. |
| `verkauf_erloese_eur` | string | ja |  |  | Echo des Verkaufserlöses in EUR für die verkaufte Menge. |
| `kaufdatum_aeltester` | string | ja |  |  | Frühestes Datum aller übergebenen Transaktionen. Allein dieses Datum entscheidet über den Altbestand, auch wenn spätere Käufe Neubestand sind. |
| `verkauf_datum` | string | ja |  |  | Echo des Verkaufsdatums; daraus wird die Haltedauer seit kaufdatum_aeltester in Tagen für die Altbestandsprüfung berechnet. |
| `acb_pro_einheit` | string | ja |  |  | ACB gleitender Durchschnittspreis |
| `anschaffungskosten` | string | ja |  |  | Anschaffungskosten der verkauften Menge in EUR = verkaufte_menge × gleitender Durchschnittspreis über alle Transaktionen, gerundet auf 2 Nachkommastellen. |
| `gewinn` | string | ja |  |  | Veräußerungsergebnis in EUR = verkauf_erloese_eur − anschaffungskosten; negativ bei Verlust. |
| `ist_altbestand` | boolean | ja |  |  | Kauf vor 01.03.2021 + >1 J gehalten = steuerfrei |
| `ist_steuerfrei` | boolean | ja |  |  | DEPRECATED (2026.52): irrefuehrend benannt, True auch bei Gewinn 0 oder Verlust. Identisch mit ohne_kest; fuer die Altbestandsfrage gilt ist_altbestand. Wird in einer kuenftigen API-Version entfernt. |
| `ohne_kest` | boolean | ja |  |  | True, wenn keine KESt anfällt: bei Altbestand, aber auch bei Gewinn 0 oder Verlust. Ob der Bestand steuerfrei ist, sagt ist_altbestand. |
| `kesteuer` | string | ja |  |  | KESt 27,5 % auf Gewinn (Neubestand) |
| `netto_erlos` | string | ja |  |  | Verkaufserlös nach KESt in EUR = verkauf_erloese_eur − kesteuer; ohne KESt gleich dem Erlös. |
| `verlust` | string | ja |  |  | Betrag des Verlusts als positive Zahl in EUR; 0 bei Gewinn und bei Altbestand mit Gewinn. |
| `hinweise` | array<string> | ja |  |  | Liste deutscher Hinweistexte: Altbestand, Verlustverrechnung über die Veranlagung oder Einbehalt durch inländische Plattformen. Nicht maschinenlesbar. |
