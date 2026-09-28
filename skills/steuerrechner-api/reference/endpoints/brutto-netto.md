# Brutto-Netto-Rechner

`POST /v1/brutto-netto`

Kategorie: Brutto-Netto

Berechnet das monatliche Nettogehalt aus dem Bruttogehalt. Beruecksichtigt Lohnsteuer (§32a EStG), Solidaritaetszuschlag, Kirchensteuer sowie alle Sozialversicherungsbeitraege (KV, PV, RV, AV) nach den Rechengroessen 2026. Liefert zusaetzlich AG-Kosten und Gehaltsszenarien (±500/±1.000/±5.000 EUR).

**Privat Krankenversicherte.** Mit `versicherungsart='pkv'` entfallen die gesetzlichen AN-Anteile KV und PV. Stattdessen zaehlen zwei verschiedene Zahlen aus derselben Police: `pkv_beitrag_gesamt` (tatsaechlich gezahlter Monatsbeitrag, begrenzt den Arbeitgeberzuschuss auf dessen Haelfte) und `pkv_basisbeitrag` (Basisanteil nach § 10 Abs. 1 Nr. 3 EStG, geht als PAP-Input PKPV in die Vorsorgepauschale). Der Zuschuss nach § 257 Abs. 2 SGB V und § 61 Abs. 2 SGB XI wird hergeleitet; `pkv_ag_zuschuss` uebersteuert ihn. Mit dem optionalen `pkv_pv_beitrag` greift der Haelfte-Deckel zweigweise statt gemeinsam – ohne ihn meldet die Antwort `pkv_zuschuss_exakt=false` plus Hinweistext.

⚠️ **`netto_monat` taugt nicht fuer den Vergleich GKV gegen PKV.** Es ist in beiden Faellen der Auszahlungsbetrag, bei PKV also inklusive des steuerfreien Arbeitgeberzuschusses. Nur ist im GKV-Fall der Kassenbeitrag darin schon abgezogen und im PKV-Fall die Praemie noch nicht. Wer die beiden Werte nebeneinanderstellt, laesst PKV besser aussehen, als es ist. Vergleichbar ist allein `netto_nach_pkv_monat`.

**Versicherungsfreie Beschaeftigte.** `sv_status='selbststaendig'` trifft den beherrschenden Gesellschafter-Geschaeftsfuehrer: steuerlich Arbeitnehmer, sozialversicherungsrechtlich nicht – RV, ALV, Umlagen und der Zuschussanspruch entfallen gemeinsam. `rv_pflichtversichert` und `alv_pflichtversichert` uebersteuern das einzeln, etwa bei Sperrminoritaet oder Befreiung zugunsten eines Versorgungswerks.

**Englische Feldnamen werden akzeptiert.** `salary`, `taxClass`, `state`, `churchTax`, `children` und `year` loest die API auf die deutschen Feldnamen auf; beim Bundesland gehen auch die ISO-Codes (`BW`, `BY`, `NW` …). Das Schema und die Antwort bleiben deutsch – die Aliasse sind eine Eingabe-Bequemlichkeit, kein zweites Format. Deshalb stehen sie hier und nicht als Beispiel: gegen das Schema mit `additionalProperties: false` waeren sie nicht valide.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `bruttolohn` | number | ja |  |  | Monatliches Bruttogehalt in EUR |
| `steuerklasse` | enum | ja |  | 1, 2, 3, 4, 5, 6 | Lohnsteuerklasse (1-6) |
| `bundesland` | enum |  | "Nordrhein-Westfalen" | Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen | Bundesland (relevant fuer Kirchensteuer-Satz). Akzeptiert ISO-Codes (BW, BY, ...). |
| `kirchensteuer` | boolean |  | false |  | True wenn Kirchensteuer abzufuehren ist |
| `kinder` | integer |  | 0 |  | Anzahl Kinder (fuer PV-Staffelung) |
| `geburtsjahr` | integer |  | 1985 |  | Geburtsjahr (fuer PV-Kinderlos-Zuschlag) |
| `kv_zusatzbeitrag` | number |  | "2.9" |  | KV-Zusatzbeitrag in Prozent. Default ist der durchschnittliche Zusatzbeitragssatz nach § 242a SGB V (2026: 2,9 %). Wer den Satz seiner Kasse kennt, sollte ihn setzen: die Saetze reichen von 2,18 bis 4,39 %. |
| `tax_year` | integer |  | 2026 |  | Steuerjahr (2024-2026) |
| `versicherungsart` | enum |  | "gkv" | gkv, pkv | `gkv` = gesetzlich krankenversichert (Default, Verhalten wie bisher). `pkv` = ausschliesslich privat krankenversichert (PAP-Merker PKV=1). Bei `pkv` entfallen die gesetzlichen AN-Anteile KV und PV; an ihre Stelle treten `pkv_beitrag_gesamt` und der Arbeitgeberzuschuss. |
| `pkv_beitrag_gesamt` | number |  | "0" |  | Tatsaechlich gezahlter **Monats**beitrag zur privaten Kranken- und Pflege-Pflichtversicherung, inklusive Wahlleistungen. Pflicht bei `versicherungsart='pkv'`. Er begrenzt den Arbeitgeberzuschuss auf dessen Haelfte (§ 257 Abs. 2 S. 2 SGB V, § 61 Abs. 2 S. 2 SGB XI) – steuerlich wirkt er nicht, dafuer zaehlt `pkv_basisbeitrag`. |
| `pkv_basisbeitrag` | number |  | "0" |  | Anteil des Monatsbeitrags, der auf die **Basis**absicherung nach § 10 Abs. 1 Nr. 3 EStG entfaellt (Basis-KV **und** private Pflege-Pflichtversicherung zusammen). Nur dieser Teil geht als PAP-Input PKPV in die Vorsorgepauschale ein. Der Versicherer bescheinigt ihn; er ist kleiner als `pkv_beitrag_gesamt`, sobald Wahlleistungen im Tarif stecken. Ohne Angabe wirkt der PKV-Beitrag steuerlich nicht. |
| `pkv_pv_beitrag` | number |  |  |  | Optional: der auf die private **Pflege**-Pflichtversicherung entfallende Teil von `pkv_beitrag_gesamt`. Mitgeschickt greift der Haelfte-Deckel zweigweise, also getrennt fuer KV und PV, wie es § 257 Abs. 2 SGB V und § 61 Abs. 2 SGB XI vorsehen – dann ist `pkv_zuschuss_exakt=true`. Weggelassen wird der Deckel auf den Gesamtbeitrag angewandt; das weicht ab, sobald genau einer der beiden Deckel bindet (typisch: hoher KV-Beitrag, kleiner PV-Beitrag), und die Antwort sagt es per `pkv_zuschuss_exakt=false` und `hinweise`. |
| `pkv_ag_zuschuss` | number |  |  |  | Optional: bekannter Arbeitgeberzuschuss aus der Abrechnung. Uebersteuert die Herleitung aus § 257 SGB V / § 61 SGB XI. Bei `sv_status='selbststaendig'` unwirksam – dort besteht kein Anspruch, und ein trotzdem gezahlter Betrag ist Arbeitslohn. |
| `sv_status` | enum |  | "angestellt" | angestellt, selbststaendig | Ergebnis der sozialversicherungsrechtlichen Statusfeststellung (§ 7a SGB IV), nicht die Frage nach einem Anstellungsvertrag. `selbststaendig` trifft den beherrschenden Gesellschafter-Geschaeftsfuehrer: steuerlich bleibt er Arbeitnehmer, sozialversicherungsrechtlich entfallen RV-, ALV- und Umlagepflicht sowie der Zuschussanspruch. Setzt `rv_pflichtversichert` und `alv_pflichtversichert` gemeinsam, solange die beiden Felder nicht selbst gesetzt sind. |
| `rv_pflichtversichert` | boolean |  |  |  | Uebersteuert den aus `sv_status` abgeleiteten Wert. `false` setzt den PAP-Merker KRV=1 und streicht den Rentenversicherungs-Teilbetrag der Vorsorgepauschale komplett – das ist der teuerste der drei Schalter. ⚠️ Wer zugunsten eines **Versorgungswerks** befreit ist (§ 6 Abs. 1 Nr. 1 SGB VI) oder sich freiwillig weiterversichert hat, bleibt KRV=0, also `true`: der PAP zaehlt beide ausdruecklich zum Nein-Zweig. |
| `alv_pflichtversichert` | boolean |  |  |  | Uebersteuert den aus `sv_status` abgeleiteten Wert. `false` setzt den PAP-Merker ALV=1; dann entfaellt neben dem AV-Beitrag auch die Hoechstbetragsberechnung MVSPHB (§ 39b Abs. 2 S. 5 Nr. 3 Buchst. e EStG). |

Beispiel:

```json
{
  "bruttolohn": 3500,
  "bundesland": "Nordrhein-Westfalen",
  "kv_zusatzbeitrag": "2.9",
  "steuerklasse": 1
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `brutto_monat` | string | ja |  |  | Bruttogehalt pro Monat in EUR |
| `brutto_jahr` | string | ja |  |  | Bruttogehalt pro Jahr in EUR |
| `netto_monat` | string | ja |  |  | Auszahlungsbetrag pro Monat in EUR. Bei `versicherungsart='pkv'` ist der steuerfreie Arbeitgeberzuschuss darin enthalten, weil er mit dem Gehalt ausgezahlt wird – das Feld bedeutet in beiden Faellen denselben Betrag, der auf dem Konto ankommt. ⚠️ **Nicht fuer den Vergleich GKV gegen PKV verwenden.** Im GKV-Fall ist der Kassenbeitrag hier bereits abgezogen, im PKV-Fall die Praemie noch nicht – nebeneinandergestellt sieht PKV dadurch besser aus, als es ist. Vergleichbar ist allein `netto_nach_pkv_monat`. |
| `netto_jahr` | string | ja |  |  | Nettogehalt pro Jahr in EUR (`netto_monat` × 12) |
| `abzuege_gesamt_monat` | string | ja |  |  | Alle Abzuege pro Monat in EUR |
| `lohnsteuer_monat` | string | ja |  |  | Lohnsteuer pro Monat in EUR |
| `soli_monat` | string | ja |  |  | Solidaritaetszuschlag pro Monat in EUR |
| `kirchensteuer_monat` | string | ja |  |  | Kirchensteuer pro Monat in EUR |
| `kv_an_monat` | string | ja |  |  | Krankenversicherung AN-Anteil pro Monat |
| `pv_an_monat` | string | ja |  |  | Pflegeversicherung AN-Anteil pro Monat |
| `rv_an_monat` | string | ja |  |  | Rentenversicherung AN-Anteil pro Monat |
| `av_an_monat` | string | ja |  |  | Arbeitslosenversicherung AN-Anteil pro Monat |
| `sv_gesamt_monat` | string | ja |  |  | Sozialversicherung gesamt (AN) pro Monat in EUR |
| `ag_kv` | string | ja |  |  | KV AG-Anteil pro Monat in EUR |
| `ag_pv` | string | ja |  |  | PV AG-Anteil pro Monat in EUR |
| `ag_rv` | string | ja |  |  | RV AG-Anteil pro Monat in EUR |
| `ag_av` | string | ja |  |  | AV AG-Anteil pro Monat in EUR |
| `ag_umlage` | string | ja |  |  | Umlage U1/U2/Insolvenzgeld pro Monat in EUR |
| `ag_gesamt` | string | ja |  |  | AG-SV-Anteil gesamt pro Monat in EUR |
| `ag_kosten_gesamt` | string | ja |  |  | Gesamtarbeitskosten (Brutto + AG-Anteil) pro Monat in EUR |
| `kv_satz` | string | ja |  |  | Angewendeter KV-Gesamtbeitragssatz in Prozent |
| `pv_satz` | string | ja |  |  | Angewendeter PV-AN-Beitragssatz in Prozent |
| `rv_satz` | string | ja |  |  | RV-Beitragssatz AN in Prozent |
| `av_satz` | string | ja |  |  | AV-Beitragssatz AN in Prozent |
| `versicherungsart` | string | ja |  |  | Angewendete Versicherungsart: `gkv` oder `pkv` |
| `sv_status` | string | ja |  |  | Angewendeter SV-Status: `angestellt` oder `selbststaendig` |
| `rv_pflichtversichert` | boolean | ja |  |  | Aufgeloester Merker: wurde der Rentenversicherungs-Teilbetrag der Vorsorgepauschale angesetzt (PAP-Input KRV=0)? Kommt aus `sv_status`, sofern das gleichnamige Eingabefeld ihn nicht uebersteuert hat. |
| `alv_pflichtversichert` | boolean | ja |  |  | Aufgeloester Merker: bestand Versicherungspflicht in der Arbeitslosenversicherung (PAP-Input ALV=0)? Steuert neben dem AV-Beitrag die Hoechstbetragsberechnung MVSPHB. |
| `pkv_beitrag_monat` | string | ja |  |  | Angesetzter PKV-Gesamtbeitrag pro Monat in EUR (0 bei GKV). Bemessung fuer den Haelfte-Deckel des Arbeitgeberzuschusses. |
| `pkv_basisbeitrag_monat` | string | ja |  |  | Davon der Basisanteil nach § 10 Abs. 1 Nr. 3 EStG in EUR (0 bei GKV). Nur dieser Teil ging als PAP-Input PKPV in die Vorsorgepauschale ein. |
| `pkv_zuschuss_monat` | string | ja |  |  | Steuerfreier Arbeitgeberzuschuss pro Monat in EUR nach § 257 Abs. 2 SGB V und § 61 Abs. 2 SGB XI (0 bei GKV und ohne Beschaeftigungsverhaeltnis). Ist `pkv_ag_zuschuss` gesetzt, steht hier dieser Wert. |
| `pkv_zuschuss_exakt` | boolean | ja |  |  | `false` bedeutet: der Haelfte-Deckel wurde auf den Gesamtbeitrag angewandt statt zweigweise auf KV und PV, weil `pkv_pv_beitrag` fehlte. Der Zuschuss kann dann zu hoch liegen, sobald genau einer der beiden Deckel bindet. Die Abweichung steht zusaetzlich als Klartext in `hinweise`. Bei GKV immer `true`. |
| `pkv_beitrag_an_monat` | string | ja |  |  | Eigenanteil des Arbeitnehmers am PKV-Beitrag pro Monat in EUR (`pkv_beitrag_monat` abzueglich `pkv_zuschuss_monat`, nie negativ). |
| `netto_nach_pkv_monat` | string | ja |  |  | Was nach Zahlung der PKV-Praemie uebrig bleibt: `netto_monat` abzueglich `pkv_beitrag_monat`. **Das ist das Feld fuer den Vergleich GKV gegen PKV** – bei GKV ist es gleich `netto_monat`, weil der Kassenbeitrag dort schon in den Abzuegen steckt. |
| `hinweise` | array<string> | ja |  |  | Klartext-Hinweise zur Berechnung, z. B. wenn der Zuschuss nur genaehert werden konnte oder ein uebergebener Zuschuss mangels Beschaeftigungsverhaeltnis nicht angesetzt wurde. Leer, wenn nichts anzumerken ist. |
| `szenarien` | array<object> | ja |  |  | Gehaltsszenarien ±500/±1.000/±5.000 EUR Brutto mit jeweiligem Netto |
