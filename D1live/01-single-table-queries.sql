-- Active: 1728520754760@@127.0.0.1@3306
-- 01. Querying data
SELECT
  LastName
FROM
  employees;

SELECT
  LastName, FirstName
FROM
  employees;

SELECT
  *
FROM
  employees;

SELECT
  LastName AS '이름'
FROM
  employees;

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;


-- 02. Sorting data
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName;

SELECT
  Country,
  City
FROM
  customers
ORDER BY
  Country DESC,
  City;

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

-- NULL 정렬 예시
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;


-- 03. Filtering data
SELECT
  LastName,
  FirstName,
  City
FROM
  customers
WHERE
  City = 'Prague';

SELECT
  LastName,
  FirstName,
  City
FROM
  customers
WHERE
  City != 'Prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 AND 500000;
  -- 동일 코드
  -- Bytes >= 10000
  -- AND Bytes <= 500000;

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 AND 500000
ORDER BY
  Bytes;

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France');
  -- Country = 'Canada'
  -- OR Country = 'Germany'
  -- OR Country = 'France';

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France');

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';
  -- 언더바 개수 = 자리 수

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;

-- 04. Grouping data
SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

SELECT
  Composer,
  AVG(Bytes) AS avgOfBytes
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  avgOfBytes DESC;

SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
-- WHERE(에러 발생)
--   avgOFMinute < 10
GROUP BY
  Composer
HAVING
  avgOfMinute < 10;
  -- HAVING clause
  -- 주로 GROUP BY와 함께 사용하며 GROUP BY가 없다면 WHERE 처럼 동작