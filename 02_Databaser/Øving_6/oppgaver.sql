/*
 * Databaser
 * Leksjon 6: SQL-spørring mot flere tabeller (JOIN)
 * Øving 6 - Oppgaver 1.1-1.4
 * M. Bjørklund
 */
 

/*
 * Oppgavetekst:
 * Tabellene og data som dere skal bruke i oppgavene kan dere hente fra scriptet bok-script-mysql.txt.
 * For å få tabellene inn i MySQL kan du copy & paste scriptet inn i phpMyAdmin for kjøring.
 * Scriptet består av følgende tabeller hvor primærnøkler er understreket og fremmednøklene markert med en stjerne.
 * 
 * KONSULENT(kons_id, fornavn, etternavn, epost)
 * BOK(bok_id, tittel, utgitt_aar, forlag_id*)
 * FORLAG(forlag_id, forlag_navn, adresse, telefon)
 * FORFATTER(forfatter_id, fornavn, etternavn, fode_aar, dod_aar, nasjonalitet)
 * BOK_FORFATTER(bok_id*, forfatter_id*)
 * Lag SQL SELECT-spørringer (en spørring pr. deloppgave) som finner svar på følgende.
 * Alle spørringer i denne oppgaven er mot flere tabeller (dvs. en eller flere foreninger (joins), evt. sub-spørringer). Se kap. 5 i læreboka.
 */
 
## 1.1 Finn navn og adresse til forlaget som har gitt ut boka 'Generation X'
SELECT forlag.forlag_navn, forlag.adresse
FROM bok
	INNER JOIN forlag ON forlag.forlag_id = bok.forlag_id
WHERE bok.tittel = "Generation X";

## 1.2 Finn titlene på alle bøkene som Hamsun har skrevet 
SELECT bok.tittel
FROM forfatter
	INNER JOIN bok_forfatter ON forfatter.forfatter_id = bok_forfatter.forfatter_id
	INNER JOIN bok ON bok_forfatter.bok_id = bok.bok_id
WHERE forfatter.etternavn = "Hamsun";

## 1.3 Finn titlene på alle bøker og navnet på forlaget som har utgitt dem.
## Tilleggsoppgave: Også navnet på de forlag som ikke har gitt ut noen bøker skal skrives ut i resultattabellen.
SELECT bok.tittel, forlag.forlag_navn
FROM forlag
	LEFT JOIN bok ON forlag.forlag_id = bok.forlag_id
ORDER BY bok.tittel DESC;


## 1.4 Finn forfattere som har gitt ut minst én bok på forlaget Cappelen.
SELECT forfatter.etternavn
FROM forlag
	INNER JOIN bok ON bok.forlag_id = forlag.forlag_id
	INNER JOIN bok_forfatter ON bok_forfatter.bok_id = bok.bok_id
	INNER JOIN forfatter ON forfatter.forfatter_id = bok_forfatter.forfatter_id
WHERE forlag.forlag_navn = "Cappelen"
GROUP BY forfatter.forfatter_id
HAVING COUNT(*) >= 1; # Not strictly required for this specific query