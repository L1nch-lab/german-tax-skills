# Duesseldorfer-Tabelle-Historie seit 2005

`GET /v1/duesseldorfer-tabelle/historie`

Kategorie: Duesseldorfer-Tabelle-Historie

Liefert die Historie der Duesseldorfer Tabelle (Kindesunterhalt, OLG Duesseldorf) seit 2005. Ohne Parameter: kompakte Jahrgangs-Liste (gueltig_ab, Stufenzahl, Mindestbedarf 0-5 Jahre, Selbstbehalte). Mit ?gueltig_ab=YYYY-MM-DD: volle Bedarfs-Matrix des Jahrgangs. Die Tabelle ist eine Leitlinie, keine Rechtsnorm; Zahlbetraege (nach Kindergeld-Abzug) sind nicht enthalten.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `gueltig_ab` | query | string |  | Exaktes Geltungs-Datum eines Jahrgangs (z. B. 2026-01-01; 2015 gibt es zweimal: 2015-01-01 und 2015-08-01). Ohne Parameter: Jahrgangs-Liste. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `stand` | string | ja |  |  | Abrufdatum der OLG-PDFs (YYYY-MM-DD) |
| `hinweis` | string |  | "Die Duesseldorfer Tabelle ist eine Leitlinie des OLG Duesseldorf, keine Rechtsnorm – Gerichte koennen im Einzelfall abweichen. Enthalten sind die BEDARFS-Betraege der Tabelle (Seite 1); die Zahlbetraege (nach Abzug des anteiligen Kindergelds) sind NICHT enthalten. 2006, 2012 und 2014 erschien keine neue Tabelle – die jeweils vorherige galt weiter." |  | Fester Hinweistext: Leitlinie des OLG Düsseldorf, keine Rechtsnorm; enthalten sind nur Bedarfsbeträge, keine Zahlbeträge nach Kindergeldabzug. |
| `jahrgaenge` | array<DuesseldorferJahrgangItem> |  |  |  | Kompakte Jahrgangs-Liste (ohne gueltig_ab-Parameter) |
| `tabelle` | DuesseldorferTabelleDetail |  |  |  | Volle Bedarfs-Matrix (mit gueltig_ab-Parameter) |
