-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');


-- 1. Insert data into table
CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAT DATE NOT NULL
);

INSERT INTO
  articles (title, content, createdAT)
VALUES
  ('hello', 'world', '2000-01-01');

INSERT INTO
  articles (title, content, createdAT)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

INSERT INTO
  articles (title, content, createdAT)
VALUES
  ('mytitle', 'mycontent', DATE());

-- 2. Update data in table
UPDATE
  articles
SET
  title = 'update Title'
WHERE
  id = 1;

UPDATE
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;

-- 3. Delete data from table
DELETE FROM
  articles
WHERE
  id = 1;

DELETE FROM
  articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAT
  LIMIT 2
);