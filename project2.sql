-- CREATE TABLE IF NOT EXISTS nomnom (
  
--   name TEXT,
--   NEIGHBORHOOD TEXT,
--   CUISINE TEXT,
--   REVIEW REAL,
--   PRICE TEXT,
--   HEALTH TEXT
-- );
-- INSERT INTO nomnom (name, NEIGHBORHOOD, CUISINE, REVIEW, PRICE, HEALTH) VALUES
--   ('Pizza Palace', 'Downtown', 'Italian', 4.5, '$$', 'A'),
--   ('Sushi World', 'Uptown', 'Japanese', 4.7, '$$$', 'A'),
--   ('Burger Barn', 'Midtown', 'American', 4.2, '$', 'B'),
--   ('Curry Corner', 'Downtown', 'Indian', 4.6, '$$', 'A'),
--   ('Taco Town', 'Uptown', 'Mexican', 4.3, '$', 'B'),
--   ('Pasta Place', 'Midtown', 'Italian', 4.4, '$$', 'A');
  SELECT * FROM nomnom;
  SELECT name, CUISINE, REVIEW FROM nomnom WHERE NEIGHBORHOOD = 'Downtown' AND PRICE = '$$' AND HEALTH = 'A';
  SELECT name, NEIGHBORHOOD, PRICE FROM nomnom WHERE CUISINE =
    'Italian' AND REVIEW >= 4.4;    
    SELECT name, CUISINE, REVIEW FROM nomnom WHERE PRICE = '$' OR PRICE = '$$';
    SELECT* FROM nomnom ORDER BY REVIEW DESC LIMIT 3;
    SELECT* FROM nomnom WHERE CUISINE = 'Mexican' ORDER BY REVIEW DESC LIMIT 1;
    SELECT * FROM nomnom WHERE name LIKE '%Pasta%';
    SELECT * FROM nomnom WHERE NEIGHBORHOOD = 'Uptown' AND REVIEW >= 4.0 ORDER BY PRICE;
    SELECT*FROM nomnom ORDER BY REVIEW
    DRSC LIMIT 4;

    