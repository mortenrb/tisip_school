/*
 * Databaser
 * Leksjon 7: Leksjon 7: Endre data (INSERT/DELETE/UPDATE)
 * Øving 7 - Oppgaver 1.1-1.2
 * M. Bjørklund
 */


/*
 * Oppgavetekst:
 * I begge oppgavene skriver du SQL -spørringer mot bokdatabasen (scriptet bok-script-mysql.txt) fra tidligere øvinger. 
 * I noen av oppgavene kan det være aktuelt å skrive flere spørringer etter hverandre som svar.
 */
 
## 1.1 SQL INSERT-spørringer mot bok-databasen 
## Du skal skrive INSERT-setninger for å legge inn ei ny bok med 2 (nye) forfattere.
## Boka som skal legges inn er boka med tittelen "Databaser" av Kjell Toft Hansen og Tore Mallaug. Boka kan registreres på forlaget Gyldendal.
## Skriv en eller flere INSERT-setninger mot tabellene bok, forfatter og bok_forfatter. PS! Rekkefølgen på INSERT-setningene er viktig pga. at referanseintegritet er satt i MySQL.
## For SQL-syntaks se eksempler i script og læreboka kap. 4. 
## Kopier INSERT-setningene inn her i riktig rekkefølge. 
INSERT INTO bok
	(tittel, utgitt_aar, forlag_id)
VALUES
(
	"Databaser",
	2008,
	(SELECT forlag_id FROM forlag WHERE forlag_navn="Gyldendal")
);

INSERT INTO forfatter 
	(fornavn, etternavn, fode_aar, dod_aar, nasjonalitet) 
VALUES 
	("Kjell Toft", "Hansen", NULL, NULL, "Norsk"),
	("Tore", "Mallaug", NULL, NULL, "Norsk");

INSERT INTO bok_forfatter 
	(bok_id, forfatter_id) 
VALUES
(
	(SELECT bok_id FROM bok WHERE tittel = "Databaser"),
	(SELECT forfatter_id FROM forfatter WHERE fornavn = "Kjell Toft" AND etternavn = "Hansen")
);

INSERT INTO bok_forfatter
	(bok_id, forfatter_id)
VALUES
(
	(SELECT bok_id FROM bok WHERE tittel = "Databaser"),
	(SELECT forfatter_id FROM forfatter WHERE fornavn = "Tore" AND etternavn = "Mallaug")
);

## 1.2 Rett opp mulige feil i eksempeldata i tabellene i bok-databasen
## Det kan finnes noen feil i data i tupler i eksempeldatabasen. Prøv å rette opp disse:
## • Fødselsåret til Hornby er feil
## • Tidligere var etternavnet til Hamsun stavet feil. Det var stavet 'Hamsund'. Skriv SQL-kode for å sjekke at denne feilen ikke eksisterer i databasen lenger
## • Evt. rett opp hvis du finner andre feil eller mangler i eksempeldataene. Kan f.eks. være forfattere som mangler dato for døde_år (hvis de er døde!)
## 
## Det finnes 2 mulige taktikker her:
## Løsn.1: Skriv UPDATE -setninger i SQL (se læreboka kap.4.3.1.2 Oppdatering av data)
## Løsn.2: Endre i selve scriptet (dvs. endre i tekstfila 'bok-script-mysql.txt')
UPDATE forfatter SET fode_aar = 1957 WHERE etternavn = "Hornby";
UPDATE forfatter SET fode_aar = 1949 WHERE etternavn = "Follet";
UPDATE forfatter SET fode_aar = 1958 WHERE etternavn = "Fielding";
UPDATE forfatter SET fode_aar = 1949 WHERE etternavn = "Sirowitz";
UPDATE forfatter SET fode_aar = 1953 WHERE etternavn = "Christensen";
UPDATE forfatter SET fode_aar = 1969 WHERE etternavn = "Loe";
UPDATE forfatter SET fode_aar = 1942, dod_aar = 2018 WHERE etternavn = "Hawking";
UPDATE forfatter SET fode_aar = 1922, dod_aar = 2010 WHERE etternavn = "Saramago";
UPDATE forfatter SET dod_aar = 2015 WHERE etternavn = "Mankell";
UPDATE forfatter SET etternavn = "Hamsund" WHERE etternavn = "Hamsun";
