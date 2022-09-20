/*
 * Databaser
 * Leksjon 4: SQL-spørring mot en tabell
 * Øving 4 - Oppgaver 1.1-1.5
 * M. Bjørklund
 */
 

/*
 * Oppgavetekst:
 * Kopier inn world-tabellen i phpMyAdmin fra scriptet bbc-world-script-mysql.txt. 
 * Tabellen er hentet fra web-siden SQLZOO. Merk deg at innholdet i versjonen av tabellen som ligger i scriptet ikke er like oppdatert som den du finner på SQLZOO.
 * For en forklaring av world-tabellen: Gå inn på nettsiden SQLZOO på denne URL-en: http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial
 * Lag SQL SELECT-spørringer (en spørring pr. deloppgave) som finner svar på følgende:
 */

## 1.1 Skriv ut navnet på alle land i 'Europe', sortert stigende alfabetisk
SELECT name FROM world WHERE continent = "Europe" ORDER BY name ASC;

## 1.2 Skriv ut navnet på alle land som IKKE er i 'Europe'
SELECT name FROM world WHERE continent != "Europe";

## 1.3 Skriv ut innbyggertallet til alle land som er i alle delene av Asia
SELECT name, population FROM world WHERE continent LIKE "%Asia%";
# Eventuelt hvis man ønsker summen av populasjonen til Asia:
SELECT SUM(population) FROM world WHERE continent LIKE "%Asia%";

## 1.4 Skriv ut landnavn som begynner på bokstavene 'Ne' eller 'No'
SELECT name FROM world WHERE name LIKE "Ne%" OR name LIKE "No%";

## 1.5 Skriv ut alle land som har innbyggertall mellom 4000000 og 6000000
SELECT name FROM world WHERE population < 6000000 AND population > 4000000;
