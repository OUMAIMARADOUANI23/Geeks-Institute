CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50) ,
    age INT
);

INSERT INTO actors (first_name, last_name, age) VALUES
('Leonardo', 'DiCaprio', 49),
('Meryl', 'Streep', 74),
('Tom', 'Hanks', 67),
('Natalie', 'Portman', 43),
('Morgan', 'Freeman', 87);

SELECT COUNT(*) FROM actors;

INSERT INTO actors (first_name, last_name, age)
VALUES (NULL, NULL, NULL);

SELECT * FROM actors;
