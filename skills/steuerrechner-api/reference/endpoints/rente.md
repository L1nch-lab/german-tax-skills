# Gesetzlicher Rentenrechner (§§ 63-68 SGB VI)

`POST /v1/rente`

Kategorie: Rente

Berechnet die voraussichtliche gesetzliche Rente nach Rentenformel (Rentenpunkte × Zugangsfaktor × Rentenwert × Rentenartfaktor). Beruecksichtigt Regelaltersgrenze nach Geburtsjahr (gestaffelt 1947-1963), Abschlag 0,3 % pro Monat vor Regelalter (§ 77 SGB VI) / Zuschlag 0,5 % pro Monat nach Regelalter, Beitragsbemessungsgrenze RV (101.400 EUR/J 2026). Liefert Rentenluecke, ETF-Sparplan-Empfehlung, 4 Szenarien (63/65/67/70) und inflationsbereinigte Kaufkraft.

## Request-Body (JSON)

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `geburtsjahr` | integer | ja |  |  | Geburtsjahr (1940-2005) |
| `bisherige_beitragsjahre` | integer | ja |  |  | Bereits geleistete Beitragsjahre |
| `aktuelles_brutto_monat` | number | ja |  |  | Aktuelles monatliches Bruttogehalt in EUR |
| `geplanter_renteneintritt` | integer | ja |  |  | Geplantes Renteneintrittsalter |
| `lohnwachstum` | number |  | "2.5" |  | Angenommenes jaehrl. Lohnwachstum in %. Wirkt auf das Endgehalt und damit auf den Bedarf im Alter. Die Entgeltpunkte je Jahr bleiben gleich, weil Durchschnittsentgelt und BBG mitwachsen (§ 70 Abs. 1 SGB VI, seit 2026.52). |
| `rentenanpassung` | number |  | "1.5" |  | Angenommene jaehrl. Rentenanpassung in %. Rechnet brutto_rente_monat auf den Rentenbeginn hoch. 0 = Rente in heutigen Werten wie in der DRV-Renteninformation; so auch fuer /v1/rentenluecke verwenden. |

Beispiel:

```json
{
  "aktuelles_brutto_monat": 4500,
  "bisherige_beitragsjahre": 15,
  "geburtsjahr": 1985,
  "geplanter_renteneintritt": 67
}
```

## Antwort: Felder in `data`

| Feld | Typ | Pflicht | Default | Werte | Beschreibung |
|---|---|---|---|---|---|
| `geburtsjahr` | integer | ja |  |  | Geburtsjahr aus der Eingabe, unverändert zurückgegeben. Bestimmt Regelaltersgrenze und aktuelles Alter. |
| `aktuelles_alter` | integer | ja |  |  | Alter in ganzen Jahren, gerechnet als 2026 minus Geburtsjahr. Der Geburtstag im Jahr wird nicht berücksichtigt. |
| `geplanter_renteneintritt` | integer | ja |  |  | Geplantes Renteneintrittsalter in ganzen Jahren aus der Eingabe (63–70). Der Abgleich mit der Regelaltersgrenze erfolgt in vollen Jahren ohne Monatsanteil. |
| `bisherige_beitragsjahre` | integer | ja |  |  | Bereits geleistete Beitragsjahre aus der Eingabe. Zählt zusammen mit verbleibende_jahre für die 45-Jahre-Prüfung der abschlagsfreien Rente nach § 236b SGB VI. |
| `verbleibende_jahre` | integer | ja |  |  | Jahre bis zum geplanten Renteneintritt (geplanter_renteneintritt minus aktuelles_alter), mindestens 0. Laufzeit für Punkteprojektion, Rentenanpassung, ETF-Sparplan und Inflationsabzinsung. |
| `rentenpunkte_bisher` | string | ja |  |  | Geschätzte bisher erworbene Entgeltpunkte: bisherige_beitragsjahre mal Punkte pro Jahr aus dem aktuellen Bruttogehalt (an der BBG gekappt, geteilt durch das Durchschnittsentgelt). Unterstellt, dass in allen bisherigen Jahren das heutige Gehalt verdient wurde. |
| `rentenpunkte_projektion` | string | ja |  |  | Entgeltpunkte, die bis zum Renteneintritt noch hinzukommen. Seit 2026.52 wachsen Gehalt, Durchschnittsentgelt und BBG gemeinsam mit lohnwachstum, die Punkte je Jahr bleiben dadurch konstant. |
| `rentenpunkte_gesamt` | string | ja |  |  | Summe aus rentenpunkte_bisher und rentenpunkte_projektion, auf 2 Nachkommastellen gerundet. Grundlage der Bruttorente. |
| `zugangsfaktor` | string | ja |  |  | Faktor 0–1+ für Abschlag oder Zuschlag (1.0 = abschlagsfrei): minus 0,003 je Monat vor, plus 0,005 je Monat nach der Regelaltersgrenze. 1.0 auch bei vorzeitigem Eintritt, wenn 45 Versicherungsjahre erreicht sind und das Eintrittsalter die Grenze nach § 236b SGB VI erreicht. |
| `abschlag_monate` | integer | ja |  |  | Anzahl Monate zwischen geplantem Eintritt und Regelaltersgrenze, für die ein Abschlag anfällt. 0 bei Eintritt zur oder nach der Regelaltersgrenze oder bei abschlagsfreier Rente nach § 236b SGB VI. |
| `zuschlag_monate` | integer | ja |  |  | Anzahl Monate, um die der Eintritt nach der Regelaltersgrenze liegt; 0 bei früherem oder pünktlichem Eintritt. |
| `abschlag_prozent` | string | ja |  |  | Abschlag in Prozent (0–100-Skala, z. B. 14.4): abschlag_monate mal 0,3. |
| `zuschlag_prozent` | string | ja |  |  | Zuschlag in Prozent (0–100-Skala, z. B. 18.0): zuschlag_monate mal 0,5. |
| `brutto_rente_monat` | string | ja |  |  | Monatliche Bruttorente in EUR: rentenpunkte_gesamt × zugangsfaktor × rentenwert, nominal mit rentenanpassung über verbleibende_jahre auf den Rentenbeginn hochgerechnet. Mit rentenanpassung = 0 in heutigen Werten. |
| `netto_rente_monat` | string | ja |  |  | Monatliche Nettorente in EUR: brutto_rente_monat nach KV und PV der Rentner (§ 249a SGB V, § 59 SGB XI) und Einkommensteuer auf den steuerpflichtigen Rentenanteil (§ 22 EStG, Rentenbeginn = Geburtsjahr + Eintrittsalter). Die Quote wird mit Werten 2026 auf die Rente in heutigen Euro gerechnet und auf die projizierte Rente übertragen. Annahmen: KVdR, mit Kindern, durchschnittlicher Zusatzbeitrag, ledig, ohne Kirchensteuer. Bis 2026.51 pauschal 85 % ohne Steuer. |
| `brutto_rente_jahr` | string | ja |  |  | Jährliche Bruttorente in EUR, brutto_rente_monat mal 12 (ohne Anpassung innerhalb des Jahres). |
| `regelaltersgrenze_jahre` | integer | ja |  |  | Jahresanteil der Regelaltersgrenze nach Geburtsjahr (65 bis 67). |
| `regelaltersgrenze_monate` | integer | ja |  |  | Monatsanteil der Regelaltersgrenze (0–11), ergänzt regelaltersgrenze_jahre; bei Jahrgang 1964 und jünger 0. |
| `letztes_brutto_projektion` | string | ja |  |  | Projiziertes monatliches Bruttogehalt in EUR im letzten Beitragsjahr: aktuelles Brutto mit lohnwachstum über verbleibende_jahre minus 1 Jahre fortgeschrieben; ohne verbleibende Jahre das heutige Brutto. |
| `letztes_netto_projektion` | string | ja |  |  | Projiziertes monatliches Nettogehalt in EUR im letzten Beitragsjahr, pauschal 60 % von letztes_brutto_projektion. Keine echte Lohnsteuer- oder SV-Berechnung. |
| `bedarf_monat` | string | ja |  |  | Angenommener monatlicher Nettobedarf im Alter in EUR: 80 % von letztes_netto_projektion. |
| `rentenluecke_monat` | string | ja |  |  | Monatliche Rentenlücke in EUR: bedarf_monat minus netto_rente_monat, nie negativ. Der Bedarf folgt lohnwachstum, die Rente rentenanpassung; beide sind nominale Werte. |
| `etf_sparrate_monat` | string | ja |  |  | Monatliche Sparrate in EUR, die bei angenommenen 6 % Rendite p. a. bis zum Renteneintritt etf_kapital_bedarf erreicht. 0, wenn keine Lücke besteht oder verbleibende_jahre 0 ist. |
| `etf_kapital_bedarf` | string | ja |  |  | Kapital in EUR, das zum Schließen der Lücke nötig wäre: rentenluecke_monat × 12 × 20 Jahre Entnahme, ohne Verzinsung in der Entnahmephase. 0 ohne Lücke oder ohne verbleibende Jahre. |
| `rentenwert` | string | ja |  |  | Aktueller Rentenwert (Stand 2026: 42,52 EUR) |
| `szenarien` | array<RenteSzenarioItem> | ja |  |  | Liste mit vier Vergleichsrechnungen für Renteneintritt mit 63, 65, 67 und 70 Jahren, jeweils mit denselben Annahmen wie die Hauptrechnung. |
| `inflation_kaufkraft` | string | ja |  |  | brutto_rente_monat in heutiger Kaufkraft (EUR), mit pauschal 2 % Inflation p. a. über verbleibende_jahre abgezinst. |
| `inflation_jahre` | integer | ja |  |  | Anzahl Jahre, über die für inflation_kaufkraft abgezinst wurde; identisch mit verbleibende_jahre. |
| `lohnwachstum` | string | ja |  |  | Angenommenes jährliches Lohnwachstum in Prozent (2.5 = 2,5 %), Echo der Eingabe. Wirkt seit 2026.52 nur noch auf das Endgehalt und damit auf Bedarf und Rentenlücke, nicht auf die Entgeltpunkte. |
| `rentenanpassung` | string | ja |  |  | Angenommene jährliche Rentenanpassung in Prozent (1.5 = 1,5 %), Echo der Eingabe. Rechnet brutto_rente_monat und die Szenario-Renten nominal auf den Rentenbeginn hoch; 0 liefert Werte in heutigen Rentenwerten. |
