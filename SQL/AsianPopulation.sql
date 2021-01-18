SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE IN (SELECT CODE FROM COUNTRY WHERE CONTINENT = 'Asia');
/*--------------USING JOIN--------------
SELECT SUM(CI.POPULATION)
FROM CITY CI
INNER JOIN COUNTRY CO ON CI.COUNTRYCODE = CO.CODE
WHERE CONTINENT = 'Asia'
*/

/* -------------WRONG SOLUTION----------
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = (SELECT CODE FROM COUNTRY WHERE CONTINENT = 'Asia');
*/ 

/* -----------------SONUÇ---------------
altsorgunun çıktısı tek değer ise "=" kullan
birden fazla çıktı varsa recursive gerekli ve "IN" kullan 
*/
