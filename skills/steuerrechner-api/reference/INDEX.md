# Endpoint-Index

Erzeugt aus der OpenAPI-Spezifikation (API-Version 2026.50) mit `tools/build_reference.py`.
Nicht von Hand bearbeiten.

| Kategorie | Methode | Pfad | Zweck | Referenz |
|---|---|---|---|---|
| Abfindung | POST | `/v1/abfindung` | Abfindungsrechner | [endpoints/abfindung.md](endpoints/abfindung.md) |
| AfA | POST | `/v1/afa` | AfA-Rechner – Linear vs degressiv 2025-2027 | [endpoints/afa.md](endpoints/afa.md) |
| Aktivrente | POST | `/v1/aktivrente` | Aktivrente-Freibetrag-Rechner (Aktivrentengesetz 2026) | [endpoints/aktivrente.md](endpoints/aktivrente.md) |
| Aktivrente | POST | `/v1/aktivrente/batch` | Aktivrente-Batch (max 1.000 Rentner) | [endpoints/aktivrente-batch.md](endpoints/aktivrente-batch.md) |
| ALG I | POST | `/v1/alg1` | Arbeitslosengeld-I-Rechner | [endpoints/alg1.md](endpoints/alg1.md) |
| Altersvorsorgedepot | POST | `/v1/altersvorsorgedepot` | Altersvorsorgedepot – Riester-Nachfolger (ab 2027) | [endpoints/altersvorsorgedepot.md](endpoints/altersvorsorgedepot.md) |
| Arbeitgeber-Kosten | POST | `/v1/arbeitgeber-kosten` | Arbeitgeber-Gesamtkosten-Rechner | [endpoints/arbeitgeber-kosten.md](endpoints/arbeitgeber-kosten.md) |
| Arbeitgeber-Kosten | POST | `/v1/arbeitgeber-kosten/batch` | Arbeitgeber-Kosten-Batch (max 1.000 Mitarbeiter) | [endpoints/arbeitgeber-kosten-batch.md](endpoints/arbeitgeber-kosten-batch.md) |
| AT-Krypto | POST | `/v1/at-krypto` | Krypto-KESt Oesterreich (§ 27b EStG AT) | [endpoints/at-krypto.md](endpoints/at-krypto.md) |
| BAfoeG | POST | `/v1/bafoeg` | BAfoeG-Rechner (§§13, 13a, 23, 25, 29 BAfoeG) | [endpoints/bafoeg.md](endpoints/bafoeg.md) |
| Basiszinssatz | GET | `/v1/basiszins/current` | Aktuell gueltiger Basiszinssatz §247 BGB | [endpoints/basiszins-current.md](endpoints/basiszins-current.md) |
| Basiszinssatz | GET | `/v1/basiszins/series` | Komplette Basiszinssatz-Reihe seit 2002 | [endpoints/basiszins-series.md](endpoints/basiszins-series.md) |
| Basiszinssatz | GET | `/v1/basiszins/{stichtag}` | Basiszinssatz §247 BGB fuer einen Stichtag | [endpoints/basiszins-stichtag.md](endpoints/basiszins-stichtag.md) |
| Bauland | GET | `/v1/bauland/{ags}` | Bauland-Kaufwerte (Kreisebene) zu einer Gemeinde | [endpoints/bauland-ags.md](endpoints/bauland-ags.md) |
| Brutto-Netto | POST | `/v1/brutto-netto` | Brutto-Netto-Rechner | [endpoints/brutto-netto.md](endpoints/brutto-netto.md) |
| Brutto-Netto | POST | `/v1/brutto-netto/batch` | Brutto-Netto-Batch (max 1.000 Mitarbeiter) | [endpoints/brutto-netto-batch.md](endpoints/brutto-netto-batch.md) |
| Buergergeld | POST | `/v1/buergergeld` | Buergergeld-Rechner (SGB II) | [endpoints/buergergeld.md](endpoints/buergergeld.md) |
| CO2-Kostenaufteilung | POST | `/v1/co2-kostenaufteilung` | CO2-Kosten Mieter/Vermieter aufteilen | [endpoints/co2-kostenaufteilung.md](endpoints/co2-kostenaufteilung.md) |
| Duesseldorfer-Tabelle-Historie | GET | `/v1/duesseldorfer-tabelle/historie` | Duesseldorfer-Tabelle-Historie seit 2005 | [endpoints/duesseldorfer-tabelle-historie.md](endpoints/duesseldorfer-tabelle-historie.md) |
| EEG-Einspeiseverguetung | GET | `/v1/eeg-novellen` | Liste aller bekannten EEG-Novellen | [endpoints/eeg-novellen.md](endpoints/eeg-novellen.md) |
| EEG-Einspeiseverguetung | GET | `/v1/eeg-verguetung` | EEG-Einspeiseverguetung fuer PV-Anlage (anzulegender Wert + Restlaufzeit) | [endpoints/eeg-verguetung.md](endpoints/eeg-verguetung.md) |
| EEG-Einspeiseverguetung | GET | `/v1/eeg-verguetung/historie` | Time-Series der EEG-Verguetung fuer eine kWp-Klasse | [endpoints/eeg-verguetung-historie.md](endpoints/eeg-verguetung-historie.md) |
| Einkommensteuer | POST | `/v1/einkommensteuer` | Einkommensteuer-Tarif | [endpoints/einkommensteuer.md](endpoints/einkommensteuer.md) |
| Einkommensteuer | POST | `/v1/einkommensteuer/batch` | Einkommensteuer-Batch (max 1.000 zvE-Werte) | [endpoints/einkommensteuer-batch.md](endpoints/einkommensteuer-batch.md) |
| Elterngeld | POST | `/v1/elterngeld` | Elterngeld-Rechner (Basis + ElterngeldPlus) | [endpoints/elterngeld.md](endpoints/elterngeld.md) |
| Erbschaftsteuer | POST | `/v1/erbschaftsteuer` | Erbschaft- und Schenkungsteuer-Rechner | [endpoints/erbschaftsteuer.md](endpoints/erbschaftsteuer.md) |
| Finanzamt | GET | `/v1/finanzamt/{ags}` | Zustaendige Finanzaemter einer Gemeinde | [endpoints/finanzamt-ags.md](endpoints/finanzamt-ags.md) |
| Firmenwagen | POST | `/v1/firmenwagen` | Firmenwagen / Geldwerter Vorteil / Dienstwagen-Rechner | [endpoints/firmenwagen.md](endpoints/firmenwagen.md) |
| Firmenwagen | POST | `/v1/firmenwagen/batch` | Firmenwagen-Batch (max 200 Fahrzeuge) | [endpoints/firmenwagen-batch.md](endpoints/firmenwagen-batch.md) |
| Freelancer | POST | `/v1/freelancer` | Freelancer-Stundensatz-Rechner (§ 18 / § 15 EStG) | [endpoints/freelancer.md](endpoints/freelancer.md) |
| Fruehstartrente | POST | `/v1/fruehstartrente` | Frühstart-Rente – Kinderdepot (Referentenentwurf FrühStRG) | [endpoints/fruehstartrente.md](endpoints/fruehstartrente.md) |
| Gemeinde-Daten | GET | `/v1/einkommen/{ags}` | Einkommen je Gemeinde (Gesamtbetrag der Einkuenfte) | [endpoints/einkommen-ags.md](endpoints/einkommen-ags.md) |
| Gemeinde-Daten | GET | `/v1/mietstufe/{ags}` | Wohngeld-Mietenstufe einer Gemeinde | [endpoints/mietstufe-ags.md](endpoints/mietstufe-ags.md) |
| Gemeinde-Daten | GET | `/v1/schulden/{ags}` | Kommunale Schulden (Kreisebene) zu einer Gemeinde | [endpoints/schulden-ags.md](endpoints/schulden-ags.md) |
| Gewerbesteuer | POST | `/v1/gewerbesteuer` | Gewerbesteuer-Rechner | [endpoints/gewerbesteuer.md](endpoints/gewerbesteuer.md) |
| Gewerbesteuer | POST | `/v1/gewerbesteuer/batch` | Gewerbesteuer-Batch (max 1.000 Faelle) | [endpoints/gewerbesteuer-batch.md](endpoints/gewerbesteuer-batch.md) |
| GEZ-Befreiung | POST | `/v1/gez` | GEZ-Befreiungsrechner (§4 RBStV) | [endpoints/gez.md](endpoints/gez.md) |
| GKV-Umlagen | GET | `/v1/gkv/umlagen` | U1-/U2-Umlagesaetze aller Krankenkassen | [endpoints/gkv-umlagen.md](endpoints/gkv-umlagen.md) |
| GKV-Zusatzbeitrag | GET | `/v1/gkv-ik-verzeichnis` | BAS-IK-Verzeichnis Lookup (echte IK-Nummern, ~1083 Eintraege) | [endpoints/gkv-ik-verzeichnis.md](endpoints/gkv-ik-verzeichnis.md) |
| GKV-Zusatzbeitrag | GET | `/v1/gkv-kassen` | Liste aller aktiven gesetzlichen Krankenkassen | [endpoints/gkv-kassen.md](endpoints/gkv-kassen.md) |
| GKV-Zusatzbeitrag | GET | `/v1/gkv-zusatzbeitrag` | Zusatzbeitrag einer Krankenkasse (aktuell oder per Stichtag) | [endpoints/gkv-zusatzbeitrag.md](endpoints/gkv-zusatzbeitrag.md) |
| GKV-Zusatzbeitrag | GET | `/v1/gkv-zusatzbeitrag/aenderungen` | Aenderungs-Feed: Zusatzbeitrags-Wechsel aller Kassen seit einem Datum | [endpoints/gkv-zusatzbeitrag-aenderungen.md](endpoints/gkv-zusatzbeitrag-aenderungen.md) |
| GKV-Zusatzbeitrag | GET | `/v1/gkv-zusatzbeitrag/durchschnitt` | Ungewichteter Jahresdurchschnitt aller Zusatzbeitragssaetze | [endpoints/gkv-zusatzbeitrag-durchschnitt.md](endpoints/gkv-zusatzbeitrag-durchschnitt.md) |
| GKV-Zusatzbeitrag | GET | `/v1/gkv-zusatzbeitrag/historie` | Time-Series aller Zusatzbeitragsstaende einer Kasse | [endpoints/gkv-zusatzbeitrag-historie.md](endpoints/gkv-zusatzbeitrag-historie.md) |
| Grunderwerbsteuer | POST | `/v1/grunderwerbsteuer` | Grunderwerbsteuer-Rechner | [endpoints/grunderwerbsteuer.md](endpoints/grunderwerbsteuer.md) |
| Grunderwerbsteuer | POST | `/v1/grunderwerbsteuer/batch` | Grunderwerbsteuer-Batch (max 1.000 Objekte) | [endpoints/grunderwerbsteuer-batch.md](endpoints/grunderwerbsteuer-batch.md) |
| Grundsteuer | POST | `/v1/grundsteuer` | Grundsteuer-Rechner ab 2025 (Bundesmodell + 5 Landesmodelle) | [endpoints/grundsteuer.md](endpoints/grundsteuer.md) |
| Grundsteuer-Monitor | GET | `/v1/grundsteuer-monitor/{ags}` | Grundsteuerreform-Monitor 2025 einer Gemeinde (SH/NRW) | [endpoints/grundsteuer-monitor-ags.md](endpoints/grundsteuer-monitor-ags.md) |
| GWG | POST | `/v1/gwg` | GWG-Rechner – Sofort vs Sammelposten vs Linear (§ 6 Abs. 2 / 2a EStG) | [endpoints/gwg.md](endpoints/gwg.md) |
| Haushaltsnah | POST | `/v1/haushaltsnah` | Haushaltsnahe Leistungen (§ 35a EStG) | [endpoints/haushaltsnah.md](endpoints/haushaltsnah.md) |
| Hebesaetze | GET | `/v1/hebesaetze` | Hebesatz-Lookup nach AGS, PLZ oder Gemeindename | [endpoints/hebesaetze.md](endpoints/hebesaetze.md) |
| Hebesaetze | POST | `/v1/hebesaetze/bulk` | Bulk-Hebesatz-Lookup per AGS-Liste | [endpoints/hebesaetze-bulk.md](endpoints/hebesaetze-bulk.md) |
| Hebesaetze | GET | `/v1/hebesaetze/{ags}` | Hebesatz nach AGS (Path-Variante, Backward-Compat) | [endpoints/hebesaetze-ags.md](endpoints/hebesaetze-ags.md) |
| Hebesaetze-Historie | GET | `/v1/hebesaetze-aenderungen` | Aenderungs-Feed: geaenderte Hebesaetze seit einem Datum | [endpoints/hebesaetze-aenderungen.md](endpoints/hebesaetze-aenderungen.md) |
| Hebesaetze-Historie | GET | `/v1/hebesaetze-aggregat` | 10-Jahres-Reihe Hebesaetze-Aggregat per Bundesland (2016-2025) | [endpoints/hebesaetze-aggregat.md](endpoints/hebesaetze-aggregat.md) |
| Hebesaetze-Historie | GET | `/v1/hebesaetze-historie` | Hebesatz-Historie einer Gemeinde | [endpoints/hebesaetze-historie.md](endpoints/hebesaetze-historie.md) |
| Homeoffice | POST | `/v1/homeoffice` | Homeoffice-Pauschale-Rechner (§ 4 Abs. 5 Nr. 6c EStG) | [endpoints/homeoffice.md](endpoints/homeoffice.md) |
| IAB | POST | `/v1/iab` | Investitionsabzugsbetrag + Sonder-AfA (§ 7g EStG) | [endpoints/iab.md](endpoints/iab.md) |
| Kapitalertragsteuer | POST | `/v1/kapitalertragsteuer` | KapESt 25 % + Soli 5,5 % + KiSt mit §51a-Spezialformel | [endpoints/kapitalertragsteuer.md](endpoints/kapitalertragsteuer.md) |
| Kapitalertragsteuer | POST | `/v1/kapitalertragsteuer/batch` | Kapitalertragsteuer-Batch (max 1.000 Positionen) | [endpoints/kapitalertragsteuer-batch.md](endpoints/kapitalertragsteuer-batch.md) |
| Kfz-Steuer | POST | `/v1/kfz-steuer` | Kfz-Steuer | [endpoints/kfz-steuer.md](endpoints/kfz-steuer.md) |
| Kindergeld | POST | `/v1/kindergeld` | Kindergeldrechner (§ 66 EStG) | [endpoints/kindergeld.md](endpoints/kindergeld.md) |
| Kinderzuschlag | POST | `/v1/kinderzuschlag` | Kinderzuschlag-Rechner (§ 6a BKGG) | [endpoints/kinderzuschlag.md](endpoints/kinderzuschlag.md) |
| Kindesunterhalt | POST | `/v1/kindesunterhalt` | Kindesunterhalt-Rechner (Duesseldorfer Tabelle 2026) | [endpoints/kindesunterhalt.md](endpoints/kindesunterhalt.md) |
| Kindesunterhalt | POST | `/v1/kindesunterhalt/batch` | Kindesunterhalt-Batch (max 1.000 Faelle) | [endpoints/kindesunterhalt-batch.md](endpoints/kindesunterhalt-batch.md) |
| Kirchensteuer-Austritt | POST | `/v1/kirchensteuer-austritt` | Kirchensteuer-Austrittsrechner (KiStG + § 10 Abs. 1 Nr. 4 EStG) | [endpoints/kirchensteuer-austritt.md](endpoints/kirchensteuer-austritt.md) |
| Kleinunternehmer | POST | `/v1/kleinunternehmer` | Kleinunternehmer-Grenze-Rechner (§ 19 UStG, JStG 2024) | [endpoints/kleinunternehmer.md](endpoints/kleinunternehmer.md) |
| Koerperschaftsteuer | POST | `/v1/koerperschaftsteuer` | Koerperschaftsteuer / GmbH-Gesamtbelastung | [endpoints/koerperschaftsteuer.md](endpoints/koerperschaftsteuer.md) |
| Krankengeld | POST | `/v1/krankengeld` | Krankengeld-Rechner (gesetzliche KV) | [endpoints/krankengeld.md](endpoints/krankengeld.md) |
| Krankenkassenbeitrag | POST | `/v1/krankenkassenbeitrag` | Krankenkassenbeitrags-Rechner (KV + PV, §§ 241 ff. SGB V / § 55 SGB XI) | [endpoints/krankenkassenbeitrag.md](endpoints/krankenkassenbeitrag.md) |
| Krypto-Steuer | POST | `/v1/krypto` | Krypto-Steuer-Rechner (§ 23 EStG Spot + § 32d KapESt Futures) | [endpoints/krypto.md](endpoints/krypto.md) |
| Kuendigungsfrist | POST | `/v1/kuendigungsfrist` | Kuendigungsfrist-Rechner (§ 622 BGB) | [endpoints/kuendigungsfrist.md](endpoints/kuendigungsfrist.md) |
| Kurzarbeitergeld | POST | `/v1/kurzarbeitergeld` | Kurzarbeitergeld-Rechner (§§ 95 ff. SGB III) | [endpoints/kurzarbeitergeld.md](endpoints/kurzarbeitergeld.md) |
| Lohnkosten-Netto | POST | `/v1/lohnkosten-netto` | Lohnkosten-zu-Netto-Umkehrrechner | [endpoints/lohnkosten-netto.md](endpoints/lohnkosten-netto.md) |
| Lohnkosten-Netto | POST | `/v1/lohnkosten-netto/batch` | Lohnkosten-Netto-Batch (max 1.000 Mitarbeiter) | [endpoints/lohnkosten-netto-batch.md](endpoints/lohnkosten-netto-batch.md) |
| Midijob | POST | `/v1/midijob` | Midijob-Rechner (Uebergangsbereich) | [endpoints/midijob.md](endpoints/midijob.md) |
| Midijob | POST | `/v1/midijob/batch` | Midijob-Batch (max 1.000 Mitarbeiter) | [endpoints/midijob-batch.md](endpoints/midijob-batch.md) |
| Mieteinnahmen | POST | `/v1/mieteinnahmen` | Mieteinnahmen versteuern | [endpoints/mieteinnahmen.md](endpoints/mieteinnahmen.md) |
| Minijob | POST | `/v1/minijob` | Minijob / Midijob-Rechner | [endpoints/minijob.md](endpoints/minijob.md) |
| Minijob | POST | `/v1/minijob/batch` | Minijob-Batch (max 1.000 Mitarbeiter) | [endpoints/minijob-batch.md](endpoints/minijob-batch.md) |
| Mutterschaftsgeld | POST | `/v1/mutterschaftsgeld` | Mutterschaftsgeldrechner (§ 24i SGB V + § 20 MuSchG) | [endpoints/mutterschaftsgeld.md](endpoints/mutterschaftsgeld.md) |
| Nachtzuschlag | POST | `/v1/nachtzuschlag` | Nachtzuschlag-Rechner mit beiden Kappungsgrenzen (§ 3b EStG + § 1 SvEV) | [endpoints/nachtzuschlag.md](endpoints/nachtzuschlag.md) |
| Netto-Brutto | POST | `/v1/netto-brutto` | Netto-Brutto-Umkehrrechner | [endpoints/netto-brutto.md](endpoints/netto-brutto.md) |
| Netto-Brutto | POST | `/v1/netto-brutto/batch` | Netto-Brutto-Batch (max 200 Zielwerte) | [endpoints/netto-brutto-batch.md](endpoints/netto-brutto-batch.md) |
| Pendlerpauschale | POST | `/v1/pendlerpauschale` | Pendlerpauschale / Entfernungspauschale (§9 EStG) | [endpoints/pendlerpauschale.md](endpoints/pendlerpauschale.md) |
| Pfaendungsfreigrenzen | POST | `/v1/pfaendung` | Pfaendungsfreigrenzen-Rechner | [endpoints/pfaendung.md](endpoints/pfaendung.md) |
| Pfaendungsfreigrenzen-Historie | GET | `/v1/pfaendung/historie` | Historie der Pfaendungsfreigrenzen seit 2005 | [endpoints/pfaendung-historie.md](endpoints/pfaendung-historie.md) |
| Photovoltaik | POST | `/v1/photovoltaik` | Photovoltaik-Steuer-Rechner (§ 12 Abs. 3 UStG + § 3 Nr. 72 EStG) | [endpoints/photovoltaik.md](endpoints/photovoltaik.md) |
| Progressionsvorbehalt | POST | `/v1/progressionsvorbehalt` | Progressionsvorbehalt-Rechner (§32b EStG) | [endpoints/progressionsvorbehalt.md](endpoints/progressionsvorbehalt.md) |
| PV-Ertrag | GET | `/v1/pv-ertrag/{ags}` | PV-Ertrag einer Gemeinde (kWh je kWp, PVGIS) | [endpoints/pv-ertrag-ags.md](endpoints/pv-ertrag-ags.md) |
| Rente | POST | `/v1/rente` | Gesetzlicher Rentenrechner (§§ 63-68 SGB VI) | [endpoints/rente.md](endpoints/rente.md) |
| Rente | POST | `/v1/rentenluecke` | Rentenluecken-Rechner (Annahmen-Modell) | [endpoints/rentenluecke.md](endpoints/rentenluecke.md) |
| Rente | POST | `/v1/rentenpunkte` | Rentenpunkte-Rechner (§§ 63 ff. SGB VI) | [endpoints/rentenpunkte.md](endpoints/rentenpunkte.md) |
| Sanierung | POST | `/v1/sanierung` | Energetische Sanierung § 35c EStG (3-Jahres-Plan) | [endpoints/sanierung.md](endpoints/sanierung.md) |
| Schenkungsteuer | POST | `/v1/schenkungsteuer` | Schenkungsteuer-Rechner (ErbStG) | [endpoints/schenkungsteuer.md](endpoints/schenkungsteuer.md) |
| Sparplan | POST | `/v1/sparplan` | Sparplan- und Zinseszinsrechner | [endpoints/sparplan.md](endpoints/sparplan.md) |
| Spekulationssteuer | POST | `/v1/spekulationssteuer` | Spekulationssteuer Immobilien | [endpoints/spekulationssteuer.md](endpoints/spekulationssteuer.md) |
| Steuerklassen | POST | `/v1/steuerklassen` | Steuerklassen-Vergleich | [endpoints/steuerklassen.md](endpoints/steuerklassen.md) |
| Stundenlohn | POST | `/v1/stundenlohn` | Stundenlohn <-> Monatsgehalt + Netto-Berechnung | [endpoints/stundenlohn.md](endpoints/stundenlohn.md) |
| Szenario-Bundles | POST | `/v1/szenario/aktien-etf` | Bundle: Aktien & ETF Komplett-Steuer (VAP + 3-Topf + KapESt mit BL-KiSt) | [endpoints/szenario-aktien-etf.md](endpoints/szenario-aktien-etf.md) |
| Szenario-Bundles | POST | `/v1/szenario/familie` | Bundle: Familienplanung (Elterngeld + StKl + Kindergeld) | [endpoints/szenario-familie.md](endpoints/szenario-familie.md) |
| Szenario-Bundles | POST | `/v1/szenario/freelance-start` | Bundle: Freelance-Start EU vs GmbH | [endpoints/szenario-freelance-start.md](endpoints/szenario-freelance-start.md) |
| Szenario-Bundles | POST | `/v1/szenario/immobilie` | Bundle: Immobilienkauf (GrESt + Grundsteuer + Nebenkosten) | [endpoints/szenario-immobilie.md](endpoints/szenario-immobilie.md) |
| Szenario-Bundles | POST | `/v1/szenario/jobwechsel` | Bundle: Jobwechsel + Abfindung + Arbeitslosigkeit | [endpoints/szenario-jobwechsel.md](endpoints/szenario-jobwechsel.md) |
| Teilzeit | POST | `/v1/teilzeit` | Teilzeit-Rechner (Netto-Vergleich Vollzeit vs. Teilzeit) | [endpoints/teilzeit.md](endpoints/teilzeit.md) |
| Urlaubsanspruch | POST | `/v1/urlaubsanspruch` | Urlaubsanspruchsrechner (§§ 3-5 BUrlG) | [endpoints/urlaubsanspruch.md](endpoints/urlaubsanspruch.md) |
| Verlustverrechnung | POST | `/v1/verlustverrechnung` | 3-Topf-Verlustverrechnung (Aktien / Sonstige / §23 Krypto) | [endpoints/verlustverrechnung.md](endpoints/verlustverrechnung.md) |
| Verpflegungsmehraufwand | POST | `/v1/verpflegungsmehraufwand` | Verpflegungsmehraufwand-Rechner (§ 9 Abs. 4a EStG, Inland) | [endpoints/verpflegungsmehraufwand.md](endpoints/verpflegungsmehraufwand.md) |
| Verzugszinsen | POST | `/v1/verzugszins` | Verzugszinsen §288 BGB pro Halbjahres-Fenster | [endpoints/verzugszins.md](endpoints/verzugszins.md) |
| VL-Sparzulage | POST | `/v1/vl` | VL-Rechner – Arbeitnehmer-Sparzulage (§ 13 5. VermBG) | [endpoints/vl.md](endpoints/vl.md) |
| Vorabpauschale | POST | `/v1/vorabpauschale` | Vorabpauschale fuer thesaurierende ETF/Fonds (§18 InvStG) | [endpoints/vorabpauschale.md](endpoints/vorabpauschale.md) |
| Vorabpauschale | POST | `/v1/vorabpauschale/portfolio` | Vorabpauschale fuer ein Multi-Fonds-Portfolio (max 1.000 Fonds) | [endpoints/vorabpauschale-portfolio.md](endpoints/vorabpauschale-portfolio.md) |
| Vorfaelligkeitsentschaedigung | POST | `/v1/vorfaelligkeitsentschaedigung` | Vorfaelligkeitsentschaedigung (VFE) – BGH-Aktiv-Passiv-Methode | [endpoints/vorfaelligkeitsentschaedigung.md](endpoints/vorfaelligkeitsentschaedigung.md) |
| Waermepumpe | POST | `/v1/waermepumpe` | KfW 458 Waermepumpe-Foerderungs-Rechner (BEG EM) | [endpoints/waermepumpe.md](endpoints/waermepumpe.md) |
| Weihnachtsgeld | POST | `/v1/weihnachtsgeld` | Sonderzahlung / 13. Gehalt / Weihnachtsgeld – Netto-Rechner | [endpoints/weihnachtsgeld.md](endpoints/weihnachtsgeld.md) |
| Werte-Bundle | GET | `/v1/werte/current` | Werte-Bundle zum heutigen Tag | [endpoints/werte-current.md](endpoints/werte-current.md) |
| Werte-Bundle | GET | `/v1/werte/{stichtag}` | Werte-Bundle zu einem Stichtag | [endpoints/werte-stichtag.md](endpoints/werte-stichtag.md) |
| Wohngeld | POST | `/v1/wohngeld` | Wohngeld-Rechner nach WoGG (Wohngeld-Plus 2023+) | [endpoints/wohngeld.md](endpoints/wohngeld.md) |
| Zensus 2022 | GET | `/v1/zensus/wohnungen/{ags}` | Zensus-2022-Wohnungskennzahlen einer Gemeinde | [endpoints/zensus-wohnungen-ags.md](endpoints/zensus-wohnungen-ags.md) |
| Zinsen | GET | `/v1/zinsen` | Bundesbank-Referenzzinssaetze (Bauzins, Tagesgeld, Festgeld, Konsumkredit) | [endpoints/zinsen.md](endpoints/zinsen.md) |
