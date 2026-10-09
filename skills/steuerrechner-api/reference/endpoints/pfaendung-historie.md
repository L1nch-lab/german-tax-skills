# Historie der Pfaendungsfreigrenzen seit 2005

`GET /v1/pfaendung/historie`

Kategorie: Pfaendungsfreigrenzen-Historie

Liefert alle wertsetzenden Pfaendungsfreigrenzenbekanntmachungen seit 2005 (monatlicher unpfaendbarer Grundbetrag nach § 850c ZPO, Erhoehungen fuer unterhaltsberechtigte Personen, Hoechstgrenze) samt BGBl-Fundstelle. Quelle: amtliche Bekanntmachungen im Bundesgesetzblatt.

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `stand` | string | ja |  |  | Abrufdatum der Primaerquellen (YYYY-MM-DD) |
| `hinweis` | string |  | "Monatliche Nettolohn-Grundbetraege nach § 850c ZPO aus den amtlichen Pfaendungsfreigrenzenbekanntmachungen (BGBl.). 2007 und 2009 blieben die Betraege per Bekanntmachung unveraendert (keine eigenen Jahrgaenge) – die Werte von 2005 galten bis 30.06.2011. Wochen-/Tagesbetraege und die 10-Euro-Tabellenschwellen stehen in der jeweiligen Bekanntmachung." |  | Fester Hinweistext: monatliche Grundbeträge nach § 850c ZPO aus den Bekanntmachungen; 2007 und 2009 ohne eigene Jahrgänge, Wochen- und Tagesbeträge stehen nur in der Bekanntmachung. |
| `jahrgaenge` | array<PfaendungHistorieItem> | ja |  |  | Alle wertsetzenden Pfändungsfreigrenzen-Bekanntmachungen seit 2005, aufsteigend nach gueltig_ab. |
