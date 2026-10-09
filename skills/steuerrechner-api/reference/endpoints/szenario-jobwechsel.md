# Bundle: Jobwechsel + Abfindung + Arbeitslosigkeit

`POST /v1/szenario/jobwechsel`

Kategorie: Szenario-Bundles

Aggregiert Brutto-Netto (alt + neu), Abfindung mit Fuenftelregel, ALG1-Anspruch und Progressionsvorbehalt-Mehrbelastung in einem Aufruf. Ideal fuer Szenario-Planung bei Arbeitgeberwechsel mit Abfindung und Zwischenarbeitslosigkeit.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `altes_brutto_monat` | number | ja |  |  | Bisheriges monatliches Bruttogehalt in EUR |
| `neues_brutto_monat` | number |  | "0" |  | Neues monatliches Bruttogehalt in EUR (0 = noch kein neuer Job) |
| `abfindung` | number |  | "0" |  | Abfindung in EUR – wird nach der Fuenftelregelung (§ 34 EStG) versteuert (0 = keine Abfindung) |
| `arbeitslos_monate` | integer |  | 0 |  | Monate Arbeitslosigkeit zwischen den Jobs – loest ALG-I-Berechnung inkl. Progressionsvorbehalt (§ 32b EStG) aus. Der Progressionsvorbehalt rechnet ein Kalenderjahr: hoechstens 12 Monate und hoechstens die ALG-Bezugsdauer gehen ein. |
| `versicherungsmonate` | integer |  | 24 |  | Versicherungspflichtige Monate in den letzten 5 Jahren, fuer die ALG-Bezugsdauer (mit dem Alter aus geburtsjahr). Default 24 = 12 Monate Bezugsdauer, wie bis 2026.51 fest angenommen. |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (Kirchensteuersatz, PV-Sachsen-Sonderregel) |
| `kirchenmitglied` | boolean |  | false |  | Kirchensteuerpflichtig |
| `kinder` | integer |  | 0 |  | Anzahl Kinder |
| `geburtsjahr` | integer |  | 1985 |  | Geburtsjahr (fuer PV-Zuschlag) |

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `altes_netto_monat` | string | ja |  |  | Monatliches Nettogehalt im bisherigen Job in EUR, aus dem Brutto-Netto-Rechner (berechne_brutto_netto) mit altes_brutto_monat sowie Steuerklasse, Bundesland, Kirchensteuer, Kindern und Geburtsjahr der Anfrage. |
| `neues_netto_monat` | string | ja |  |  | Monatliches Nettogehalt im neuen Job in EUR, aus dem Brutto-Netto-Rechner mit neues_brutto_monat und denselben übrigen Parametern. 0, wenn neues_brutto_monat 0 ist. |
| `netto_differenz_monat` | string | ja |  |  | Netto-Unterschied neuer gegen alten Job in EUR/Monat (neues_netto_monat minus altes_netto_monat), negativ bei weniger Netto. |
| `abfindung_netto_fuenftel` | string | ja |  |  | Abfindung nach Steuern in EUR (Einmalbetrag) bei Anwendung der Fünftelregelung, aus dem Abfindungsrechner (berechne_abfindung, Feld netto_fuenftel). Abgezogen wird nur die auf die Abfindung entfallende ESt, Soli und ggf. KiSt (Grundtarif, Veranlagung); Bezugsbasis ist altes_brutto_monat × 12. 0 ohne Abfindung. |
| `abfindung_netto_normal` | string | ja |  |  | Abfindung nach Steuern in EUR (Einmalbetrag) ohne Fünftelregelung, also bei voller Besteuerung zusammen mit dem regulären Einkommen, aus berechne_abfindung (Feld netto_normal). 0 ohne Abfindung. |
| `abfindung_ersparnis` | string | ja |  |  | Steuerersparnis durch die Fünftelregelung in EUR (Einmalbetrag): Steuer auf die Abfindung ohne minus mit Fünftelregelung, entspricht abfindung_netto_fuenftel minus abfindung_netto_normal. Aus berechne_abfindung (ersparnis_gesamt); 0 ohne Abfindung. |
| `alg1_monat` | string | ja |  |  | Monatliches Arbeitslosengeld I in EUR aus dem ALG-I-Rechner (berechne_alg1), berechnet aus altes_brutto_monat (Tagessatz × 30); erhöhter Leistungssatz, wenn kinder > 0. Nur bei arbeitslos_monate > 0, sonst 0. |
| `alg1_bezugsdauer_monate` | integer | ja |  |  | Maximale ALG-I-Anspruchsdauer in Monaten aus berechne_alg1, nicht die angefragte Dauer der Arbeitslosigkeit. Der Bundle übergibt weder Alter noch Versicherungsmonate, es greifen die Defaults des ALG-I-Rechners (alter=30, versicherungsmonate=24), daher ist der Wert bei arbeitslos_monate > 0 immer 12, sonst 0. |
| `progression_mehrbelastung_jahr` | string | ja |  |  | Zusätzliche Jahressteuer in EUR (ESt + Soli + ggf. KiSt) durch den Progressionsvorbehalt, aus berechne_progressionsvorbehalt im Grundtarif. Lohnersatzleistung = alg1_monat × arbeitslos_monate (nicht auf die Bezugsdauer begrenzt); als Einkommen geht das zvE (berechne_zve) aus neues_brutto_monat × (12 − arbeitslos_monate) ein, nicht das Brutto und nicht der alte Lohn. 0 ohne Arbeitslosigkeit oder wenn dieses zvE 0 ist. |
| `hinweise` | array<string> | ja |  |  | Liste fester Hinweistexte: immer ein Hinweis auf den Bundle-Charakter, dazu je ein Hinweis zur Fünftelregelung (bei Abfindung > 0) und zum Progressionsvorbehalt bei ALG I (bei arbeitslos_monate > 0). |
