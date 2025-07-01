SELECT * FROM customer;

SELECT first_name || ' ' || last_name AS full_name
FROM customer;

SELECT DISTINCT create_date
FROM customer;

SELECT * 
FROM customer
ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT address, phone
FROM address
WHERE district = 'Texas';

SELECT *
FROM film
WHERE film_id IN (15, 150);

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Academy Dinosaur';

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title ILIKE 'Ac%';

SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

SELECT film_id, title, rental_rate
FROM (SELECT film_id, title, rental_rate,ROW_NUMBER() OVER (ORDER BY rental_rate ASC) AS rank FROM film) AS ranked_films
WHERE rank > 10 AND rank <= 20;

SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

SELECT *
FROM film
WHERE film_id NOT IN (SELECT film_id FROM inventory);

SELECT city.city, country.country
FROM city
JOIN country ON city.country_id = country.country_id;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id;
