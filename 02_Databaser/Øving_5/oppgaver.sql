/*
 * Databaser
 * Leksjon 5: SQL-spørring med funksjoner og gruppering
 * Øving 5 - Oppgaver 1.6-1.10
 * M. Bjørklund
 */
 

/*
 * Oppgavetekst:
 * Kopier inn world-tabellen i phpMyAdmin fra scriptet bbc-world-script-mysql.txt fra forrige øving (hvis du ikke har den fra tidligere).
 * Tabellen er hentet fra web-siden SQLZOO. Merk deg at innholdet i versjonen av tabellen som ligger i scriptet ikke er like oppdatert som den du finner på SQLZOO.
 * For en forklaring av world-tabellen: Gå inn på nettsiden SQLZOO på denne URL-en: http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial
 * Lag SQL SELECT-spørringer (en spørring pr. deloppgave) som finner svar på følgende:
 */
 
## 1.6 Finn totalt antall land i tabellen
SELECT COUNT(*) FROM world;

## 1.7 Finn antall land som har innbyggertall mellom 4000000 og 6000000
SELECT COUNT(*) FROM world WHERE population < 6000000 AND population > 4000000;

## 1.8 Finn gjennomsnitts innbyggertall pr. kvadratkilometer (area) for landene i 'Europe'
SELECT name, (population / area) AS pop_per_area FROM world WHERE continent = "Europe";

## 1.9 For hvert kontinent, finn antall land
SELECT continent, COUNT(*) AS ant_land FROM world GROUP BY continent;

## 1.10 Skriv ut de kontinentene som har flere enn 10 land
SELECT continent, COUNT(*) AS ant_land FROM world GROUP BY continent HAVING ant_land > 10;
