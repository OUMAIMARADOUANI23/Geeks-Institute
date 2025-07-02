SELECT * FROM students

SELECT first_name, last_name FROM students 
ORDER BY last_name ASC
LIMIT 4

SELECT * FROM students
where birth_date=(SELECT MAX(birth_date) FROM students);

SELECT * FROM students 
ORDER BY last_name ASC
OFFSET 2
LIMIT 3;