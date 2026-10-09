# BAfoeG-Rechner (§§13, 13a, 23, 25, 29 BAfoeG)

`POST /v1/bafoeg`

Kategorie: BAfoeG

Berechnet den voraussichtlichen BAfoeG-Foerderbetrag aus Grundbedarf (§13), Wohnpauschale, KV/PV-Zuschlag (§13a), Elterneinkommen mit Freibetraegen (§25), Eigeneinkommen (§23) und Vermoegensanrechnung (§29). Die Altersgrenze des §10 Abs. 3 stellt auf das Alter BEI BEGINN des Ausbildungsabschnitts ab (`alter_bei_ausbildungsbeginn`) und kennt sechs Ausnahmen (`altersgrenze_ausnahme`); greift sie, zeigt `rechnerischer_betrag` weiterhin, was ohne die Sperre herauskaeme. Stand 2026-04: Werte aus BAfoeG-Reformgesetz 2024, Erhoehung zum WS 2026/27 noch nicht beschlossen. Unverbindliche Orientierung, keine Rechtsberatung i.S.d. RDG/StBerG.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `ausbildungstyp` | enum | ja |  | schule, hochschule | 'schule' (Abendgymnasium/Kolleg) oder 'hochschule' (Uni/FH) |
| `bei_eltern` | boolean | ja |  |  | True wenn bei Eltern wohnend, sonst auswaerts |
| `alter` | integer | ja |  |  | Alter in vollen Jahren |
| `kvpv_variante` | enum |  | "standard" | standard, aeltere_freiwillig, privat | 'standard' (U30 gesetzl./familienversichert) \| 'aeltere_freiwillig' (Ue30 freiwillig) \| 'privat' |
| `elterneinkommen_netto` | number |  | "0" |  | Monatliches Elterneinkommen netto gesamt in EUR |
| `eltern_verheiratet` | boolean |  | true |  | True wenn die Eltern verheiratet/zusammenlebend sind – bestimmt den Eltern-Grundfreibetrag (§ 25 Abs. 1 BAfoeG) |
| `weitere_kinder_ohne_foerderung` | integer |  | 0 |  | Weitere Kinder der Eltern, die NICHT selbst BAfoeG/§56-SGB-III-gefoerdert werden – je +770 EUR Freibetrag (§ 25 Abs. 3 Nr. 2 BAfoeG). Geschwister in eigener foerderbarer Ausbildung zaehlen NICHT. |
| `weitere_unterhalt_personen` | integer |  | 0 |  | Weitere unterhaltsberechtigte Personen der Eltern ohne eigene Ausbildungsfoerderung (Freibetrag § 25 Abs. 3 BAfoeG) |
| `eigenes_einkommen_netto` | number |  | "0" |  | Eigenes Netto-Einkommen in EUR/Monat (z.B. Nebenjob) – Anrechnung nach Freibetrag gemaess § 23 BAfoeG |
| `eigene_kinder` | integer |  | 0 |  | Eigene Kinder des Auszubildenden – erhoehen den Freibetrag vom eigenen Einkommen (§ 23 Abs. 1 BAfoeG) |
| `eigener_ehegatte` | boolean |  | false |  | True wenn verheiratet/verpartnert – erhoeht den Freibetrag vom eigenen Einkommen (§ 23 Abs. 1 BAfoeG) |
| `vermoegen` | number |  | "0" |  | Eigenes verwertbares Vermoegen in EUR – Freibetrag nach § 29 BAfoeG, darueber liegender Teil wird angerechnet |
| `alter_bei_ausbildungsbeginn` | integer |  |  |  | Alter bei Beginn des Ausbildungsabschnitts – der Stichtag der Altersgrenze des § 10 Abs. 3 BAfoeG. Ohne Angabe wird `alter` verwendet. Nicht dasselbe wie `alter`: § 29 Abs. 1 Satz 2 stellt fuer den Vermoegensfreibetrag auf den Zeitpunkt der Antragstellung ab |
| `altersgrenze_ausnahme` | boolean |  | false |  | True, wenn ein Ausnahmetatbestand des § 10 Abs. 3 Satz 2 BAfoeG vorliegt (zweiter Bildungsweg, Hochschulzugang ueber berufliche Qualifikation, weitere Ausbildung nach § 7 Abs. 2 Nr. 2/3, Anschlussstudium nach Bachelor, Kindererziehung/familiaere Hinderungsgruende, Beduerftigkeit nach einschneidender Veraenderung). Dann entfaellt die Sperre der Altersgrenze |

Beispiel:

```json
{
  "alter": 22,
  "ausbildungstyp": "hochschule",
  "bei_eltern": false
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `grundbedarf` | string | ja |  |  | §13 Grundbedarf in EUR/Monat |
| `wohnpauschale` | string | ja |  |  | §13 Wohnpauschale in EUR/Monat |
| `kvpv_zuschlag` | string | ja |  |  | §13a KV/PV-Zuschlag in EUR/Monat |
| `gesamtbedarf` | string | ja |  |  | Monatlicher Bedarf in EUR: grundbedarf + wohnpauschale + kvpv_zuschlag, vor Anrechnung von Einkommen und Vermögen. |
| `elterneinkommen_netto` | string | ja |  |  | Echo des monatlichen Nettoeinkommens beider Eltern zusammen in EUR. |
| `elternfreibetrag` | string | ja |  |  | §25 Elternfreibetrag |
| `anrechenbares_elterneinkommen` | string | ja |  |  | Elterneinkommen, das den Bedarf mindert, in EUR pro Monat: Überschuss über elternfreibetrag, davon bleiben 50 % plus 5 % je weiterem Kind ohne Förderung anrechnungsfrei. |
| `eigenes_einkommen_netto` | string | ja |  |  | Echo des monatlichen Nettoeinkommens des Antragstellers in EUR. |
| `eigener_freibetrag` | string | ja |  |  | §23 Eigenfreibetrag |
| `anrechenbares_eigenes_einkommen` | string | ja |  |  | Eigenes Einkommen über eigener_freibetrag in EUR pro Monat, nie unter 0; wird voll vom Bedarf abgezogen. |
| `vermoegen` | string | ja |  |  | Echo des Gesamtvermögens des Antragstellers in EUR (Bestand, kein Monatswert). |
| `vermoegen_freibetrag` | string | ja |  |  | §29 Vermoegensfreibetrag |
| `vermoegen_anrechnung_monat` | string | ja |  |  | Anrechenbares Vermoegen / 12 |
| `rechnerischer_betrag` | string | ja |  |  | Rechnerischer Foerderbetrag vor der Altersgrenze des §10 Abs. 3. Weicht nur ab, wenn ueber_altersgrenze=true – dann zeigt dieses Feld, was bei einem Ausnahmetatbestand (Abs. 3 Satz 2) herauskaeme. |
| `foerderbetrag_monat` | string | ja |  |  | Voraussichtliche Förderung in EUR pro Monat: gesamtbedarf minus angerechnetes Einkommen und Vermögen, nicht unter 0. 0, wenn ueber_altersgrenze true ist (der rechnerische Wert steht dann in rechnerischer_betrag). |
| `foerderbetrag_jahr` | string | ja |  |  | foerderbetrag_monat × 12 in EUR. |
| `has_anspruch` | boolean | ja |  |  | True, wenn foerderbetrag_monat größer 0 ist. |
| `ueber_altersgrenze` | boolean | ja |  |  | True, wenn §10 Abs. 3 Satz 1 greift (45 J. bei Ausbildungsbeginn) |
| `altersgrenze_ausnahme` | boolean | ja |  |  | Echo: es wurde mit einer Ausnahme nach §10 Abs. 3 Satz 2 gerechnet |
| `ausbildungstyp` | string | ja |  |  | Echo des Ausbildungstyps: "schule" (Abendgymnasium, Kolleg, Berufsfachschule) oder "hochschule"; bestimmt den Grundbedarf. |
| `wohnsituation` | string | ja |  |  | "bei_eltern" oder "auswaerts", abgeleitet aus der Eingabe bei_eltern; bestimmt die Wohnpauschale. |
| `alter` | integer | ja |  |  | Echo des Alters des Antragstellers in vollen Jahren; bestimmt den Vermögensfreibetrag (ab 30 höhere Stufe) und ersetzt alter_bei_ausbildungsbeginn, wenn dieses fehlt. |
| `alter_bei_ausbildungsbeginn` | integer | ja |  |  | Stichtagsalter des §10 Abs. 3 – ohne Angabe gleich `alter` |
| `hinweise` | array<string> | ja |  |  | Liste von Texthinweisen, z. B. zur Altersgrenze, zu fehlendem Anspruch oder zum erhöhten KV/PV-Zuschlag; enthält immer den Hinweis, dass das BAföG-Amt den Betrag festsetzt. |
