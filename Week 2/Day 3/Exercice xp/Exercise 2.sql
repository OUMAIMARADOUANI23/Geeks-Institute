SELECT * FROM language;

UPDATE film
SET language_id = 3 
WHERE title ILIKE '%Love%';

SELECT conname, confrelid::regclass AS referenced_table
FROM pg_constraint
WHERE conrelid = 'customer'::regclass;

DROP TABLE customer_review;

SELECT COUNT(*) 
FROM rental
WHERE return_date IS NULL;

SELECT f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

SELECT f.title, f.description
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON a.actor_id = fa.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
  AND f.description ILIKE '%sumo%';

SELECT title, description, length, rating
FROM film
WHERE length < 60 AND rating = 'R';

SELECT DISTINCT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON p.rental_id = r.rental_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND p.amount > 4
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

SELECT DISTINCT f.title, f.replacement_cost, f.description
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC;

