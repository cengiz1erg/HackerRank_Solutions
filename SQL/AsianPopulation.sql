SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE IN (SELECT CODE FROM COUNTRY WHERE CONTINENT = 'Asia');

/* ----- HATALI İLK HAL -----
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = (SELECT CODE FROM COUNTRY WHERE CONTINENT = 'Asia');
*/ 
/* ----- SONUÇ -----
altsorgunun çıktısı tek değer ise "=" kullan
birden fazla çıktı varsa recursive gerekli ve "IN" kullan 
*/
