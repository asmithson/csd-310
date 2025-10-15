USE movies;

-- 1. Displaying all records from the studio table
SELECT * FROM studio;
-- 2. Displaying all records from the genre table
SELECT * FROM genre;

-- 3. Displaying film names with a runtime less than 2 hours
SELECT film_name
FROM film
WHERE film_runtime < 120;

-- 4. Displaying film names grouped by director with director names
SELECT film_director,
	GROUP_CONCAT(film_name ORDER BY film_name SEPARATOR ', ') AS films
FROM film
GROUP BY film_director
ORDER BY film_director;