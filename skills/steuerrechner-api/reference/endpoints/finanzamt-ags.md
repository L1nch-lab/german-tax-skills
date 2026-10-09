# Zustaendige Finanzaemter einer Gemeinde

`GET /v1/finanzamt/{ags}`

Kategorie: Finanzamt

Liefert die fuer eine Gemeinde zustaendigen Finanzaemter samt Stammdaten (Adresse, Postfach, Telefon, URL, IBAN der Finanzkasse, Oeffnungszeiten) aus dem GemFa-Verzeichnis des Bundeszentralamts fuer Steuern (BZSt). Grossstaedte koennen mehrere Finanzaemter haben (Berlin: 17) – massgeblich ist der Steuerbescheid bzw. die ELSTER-Finanzamtssuche.

## Parameter

| Parameter | Ort | Typ | Pflicht | Beschreibung |
|---|---|---|---|---|
| `ags` | path | string | ja | 8-stelliger Amtlicher Gemeindeschluessel oder 5-stellige Postleitzahl. Gehoert die PLZ zu mehreren Gemeinden, kommt 409 mit den Kandidaten. |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ags` | string | ja |  |  | Angefragte Gemeinde-AGS (8-stellig) |
| `gemeinde_name` | string |  |  |  | Gemeindename laut GemFa-Verzeichnis |
| `stand` | string | ja |  |  | Export-Stand des BZSt-GemFa-Datenbestands (YYYY-MM-DD) |
| `hinweis` | string |  | "Zustaendigkeit nach dem GemFa-Verzeichnis des BZSt (Gemeinde-Finanzamt-Zuordnung). Bei mehreren Finanzaemtern je Gemeinde (z. B. Berlin) haengt die Zustaendigkeit von Bezirk und Aufgabe ab – massgeblich ist der Steuerbescheid bzw. die ELSTER-Finanzamtssuche." |  | Fester Hinweistext zur Zuständigkeit nach dem GemFa-Verzeichnis des BZSt; bei mehreren Finanzämtern je Gemeinde entscheiden Bezirk und Aufgabe. |
| `finanzaemter` | array<FinanzamtItem> | ja |  |  | Alle Finanzämter, die dem Gemeindeschlüssel zugeordnet sind, sortiert nach BuFa-Nummer; meist eins, in Großstädten mehrere (Berlin: 17). |
