# Nachtzuschlag-Rechner mit beiden Kappungsgrenzen (§ 3b EStG + § 1 SvEV)

`POST /v1/nachtzuschlag`

Kategorie: Nachtzuschlag

Berechnet Zuschlaege fuer Nacht-, Sonntags- und Feiertagsarbeit nach § 3b EStG (25/40/50/125/150 %) und weist BEIDE Kappungsgrenzen getrennt aus: steuerfrei nur bis 50 EUR Grundlohn je Stunde (§ 3b Abs. 2 S. 1 EStG), beitragsfrei nur bis 25 EUR (§ 1 Abs. 1 S. 1 Nr. 1 SvEV). Zwischen 25 und 50 EUR ist der Zuschlag steuerfrei, aber beitragspflichtig – dieser Bereich steht als nur_sv_pflichtig im Ergebnis. Die 40 % fuer 0-4 Uhr gelten nur bei Schichtbeginn vor 0 Uhr (§ 3b Abs. 3 Nr. 1). Optional weist netto_ausweisen die Steuer- und SV-Last auf den pflichtigen Teil aus (BMF-PAP-Differenzrechnung auf zwei getrennten Bemessungsgrundlagen).

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `grundlohn_stunde` | number |  | "0" |  | Grundlohn je Stunde in EUR. Bei 0 wird er aus monatsbrutto und wochenstunden umgerechnet |
| `stunden_nacht_rand` | number |  | "0" |  | Nachtstunden 20-24 Uhr und 4-6 Uhr im Monat (25 %, § 3b Abs. 1 Nr. 1) |
| `stunden_nacht_kernzeit` | number |  | "0" |  | Nachtstunden 0-4 Uhr im Monat (40 % nur bei Schichtbeginn vor 0 Uhr, § 3b Abs. 3 Nr. 1; sonst 25 %) |
| `stunden_sonntag` | number |  | "0" |  | Sonntagsstunden im Monat (50 %, § 3b Abs. 1 Nr. 2) |
| `stunden_feiertag` | number |  | "0" |  | Stunden an gesetzlichen Feiertagen und am 31.12. ab 14 Uhr (125 %, § 3b Abs. 1 Nr. 3) |
| `stunden_feiertag_hoch` | number |  | "0" |  | Stunden am 24.12. ab 14 Uhr, 25./26.12. und 1. Mai (150 %, § 3b Abs. 1 Nr. 4) |
| `schicht_vor_mitternacht` | boolean |  | true |  | True wenn die Nachtarbeit vor 0 Uhr aufgenommen wurde – nur dann gelten fuer 0-4 Uhr die 40 % (§ 3b Abs. 3 Nr. 1) |
| `monatsbrutto` | number |  | "0" |  | Monatliches Bruttoentgelt in EUR – Alternative zum Stundenlohn und Basis fuer den Netto-Ausweis |
| `wochenstunden` | number |  | "0" |  | Regelmaessige Wochenarbeitszeit, nur fuer die Umrechnung |
| `netto_ausweisen` | boolean |  | false |  | True: zusaetzlich ausweisen, was vom Zuschlag netto bleibt (braucht monatsbrutto als Basis) |
| `steuerklasse` | enum |  | 1 | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse 1-6, nur fuer den Netto-Ausweis |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland, nur fuer den Netto-Ausweis (Kirchensteuer-Satz, PV Sachsen). Akzeptiert ISO-Codes (BW, BY, ...). |
| `kirchensteuer` | boolean |  | false |  | Kirchensteuerpflicht, nur fuer den Netto-Ausweis |
| `kinder` | integer |  | 0 |  | Anzahl Kinder (PV-Abschlag), nur fuer den Netto-Ausweis |
| `geburtsjahr` | integer |  | 1990 |  | Geburtsjahr (PV-Kinderlos-Zuschlag), nur fuer den Netto-Ausweis |

Beispiel:

```json
{
  "bundesland": "Nordrhein-Westfalen",
  "grundlohn_stunde": 30,
  "schicht_vor_mitternacht": true,
  "steuerklasse": 1,
  "stunden_nacht_kernzeit": 20,
  "stunden_nacht_rand": 40
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `grundlohn_stunde` | string | ja |  |  | Angesetzter Grundlohn je Stunde |
| `grundlohn_geschaetzt` | boolean | ja |  |  | True wenn der Grundlohn aus monatsbrutto/wochenstunden umgerechnet wurde |
| `grundlohn_steuer` | string | ja |  |  | Fuer die Steuerfreiheit angesetzter Grundlohn (max 50 EUR, § 3b Abs. 2 EStG) |
| `grundlohn_sv` | string | ja |  |  | Fuer die Beitragsfreiheit angesetzter Grundlohn (max 25 EUR, § 1 SvEV) |
| `steuerkappung_greift` | boolean | ja |  |  |  |
| `svkappung_greift` | boolean | ja |  |  |  |
| `positionen` | array<NachtzuschlagPosition> | ja |  |  | Eine Zeile je Zuschlagsart mit Stunden > 0 |
| `stunden_gesamt` | string | ja |  |  |  |
| `zuschlag_gesamt` | string | ja |  |  | Gezahlter Zuschlag gesamt pro Monat |
| `steuerfrei_gesamt` | string | ja |  |  |  |
| `steuerpflichtig_gesamt` | string | ja |  |  |  |
| `beitragsfrei_gesamt` | string | ja |  |  |  |
| `beitragspflichtig_gesamt` | string | ja |  |  |  |
| `nur_sv_pflichtig` | string | ja |  |  | Steuerfrei, aber beitragspflichtig – der Bereich zwischen den beiden Kappungsgrenzen (Grundlohn 25-50 EUR/h) |
| `nacht_kernzeit_satz` | string | ja |  |  | Angewendeter Satz fuer 0-4 Uhr (40 oder 25) |
| `schicht_vor_mitternacht` | boolean | ja |  |  |  |
| `netto_ausgewiesen` | boolean | ja |  |  | True wenn der Netto-Effekt berechnet wurde |
| `steuer_auf_zuschlag` | string | ja |  |  | Lohnsteuer+Soli+KiSt auf den steuerpflichtigen Teil (Differenzrechnung) |
| `sv_auf_zuschlag` | string | ja |  |  | SV-Beitraege auf den beitragspflichtigen Teil (Differenzrechnung) |
| `zuschlag_netto` | string | ja |  |  | Zuschlag nach Steuer und SV (nur bei Ausweis) |
