# KapESt 25 % + Soli 5,5 % + KiSt mit §51a-Spezialformel

`POST /v1/kapitalertragsteuer`

Kategorie: Kapitalertragsteuer

Berechnet die abgeltende Quellensteuer auf eine bereits bereinigte Bemessungsgrundlage (nach Sparer-Pauschbetrag und Verlustverrechnung): Kapitalertragsteuer 25 % nach §43a EStG, Solidaritaetszuschlag 5,5 % auf KapESt (kein Phase-Out beim Quellenabzug, §4 SolzG) und Kirchensteuer 8 % (BY/BW) bzw. 9 % (uebrige Laender). Bei aktiver Kirchensteuer greift die §51a Abs. 2c EStG-Spezialformel KapESt = e / (4 + k), die viele Online-Rechner falsch ansetzen. Liefert Effektivsatz und Netto-Auszahlung.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bemessungsgrundlage` | number | ja |  |  | Steuerpflichtige Kapitalertraege in EUR (nach Sparer-Pauschbetrag und nach Verlustverrechnung). Negative Werte sind ein Verlust und werden hier nicht berechnet – dafuer /v1/verlustverrechnung nutzen. |
| `bundesland` | enum | ja |  | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland fuer die Kirchensteuer-Hoehe. 8 % in Bayern und Baden-Württemberg, 9 % in allen uebrigen. |
| `kirchensteuerpflichtig` | boolean |  | false |  | True wenn KiSt einbehalten werden soll (§51a Abs. 2c EStG-Formel). |

Beispiel:

```json
{
  "bemessungsgrundlage": "10000",
  "bundesland": "Nordrhein-Westfalen",
  "kirchensteuerpflichtig": false
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bemessungsgrundlage` | string | ja |  |  | Eingabe-Bemessungsgrundlage in EUR (nach Sparer-Pauschbetrag und Verlustverrechnung) |
| `kapest` | string | ja |  |  | Kapitalertragsteuer 25 % nach §43a Abs. 1 Satz 1 Nr. 1 EStG, bei Kirchensteuerpflicht reduziert via §51a Abs. 2c EStG-Spezialformel |
| `soli` | string | ja |  |  | Solidaritaetszuschlag 5,5 % auf KapESt, kein Phase-Out (§4 SolzG) |
| `kirchensteuer` | string | ja |  |  | Kirchensteuer auf KapESt, 8 % (BY/BW) bzw. 9 % (uebrige) |
| `steuer_summe` | string | ja |  |  | Summe KapESt + Soli + KiSt in EUR |
| `netto` | string | ja |  |  | Auszahlbar nach Quellenabzug = Bemessungsgrundlage - Steuer-Summe |
| `effektivsatz_prozent` | string | ja |  |  | Steuer-Summe / Bemessungsgrundlage in Prozent (4 Nachkommastellen) |
| `kirchensteuer_satz_prozent` | string | ja |  |  | Verwendeter KiSt-Satz in Prozent (8 / 9 / 0 wenn nicht pflichtig) |
| `bundesland` | string | ja |  |  |  |
| `kirchensteuerpflichtig` | boolean | ja |  |  |  |
| `rechtsgrundlage` | string | ja |  |  |  |
