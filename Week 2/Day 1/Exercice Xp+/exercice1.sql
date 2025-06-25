CREATE TABLE students(
id SERIAL PRIMARY KEY,
last_name VARCHAR(100),
first_name VARCHAR(100),
birth_date DATE
);

INSERT INTO students (first_name, last_name, birth_date) VALUES
('marc', 'benichou', '1998-11-02'),
('yoan', 'cohen', '2010-12-03'),
('lea', 'benichou', '1987-07-27'),
('amelia', 'dux', '1996-04-07'),
('david', 'grez', '2003-06-14'),
('omer', 'simpson', '1980-10-03');

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('oumaima', 'radouani', '2002-02-23');

SELECT * FROM students;

SELECT first_name, last_name FROM students;

SELECT first_name, last_name FROM students
WHERE id = 2;

SELECT first_name, last_name FROM students
WHERE first_name = 'marc' AND last_name = 'benichou';

SELECT first_name, last_name FROM students
WHERE last_name = 'benichou' OR first_name = 'marc';

SELECT first_name, last_name FROM students
WHERE first_name LIKE '%a%';

SELECT first_name, last_name FROM students
WHERE first_name LIKE 'a%';

SELECT first_name, last_name FROM students
WHERE first_name LIKE '%a';

SELECT first_name, last_name FROM students
WHERE id IN (1, 3);

SELECT * FROM students
WHERE birth_date >= '2000-01-01';


