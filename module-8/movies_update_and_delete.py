# movies_update_and_delete.py
# Author: Asher Smithson
# Date: October 23, 2025
# M8.2 Assignment- Movies: Update & Deletes

import mysql.connector
from mysql.connector import errorcode

# Connection to the movies database
config = {
    "user": "root",
    "password": "TakaisBae25!",
    "host": "localhost",
    "database": "movies"
}

def show_films(cursor, title):
    """Display film name, director, genre, and studio via INNER JOINs."""
    query = (
        "SELECT film_name AS Name, film_director AS director, "
        "genre_name AS Genre, studio_name AS Studio "
        "FROM film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id "
        "ORDER BY film_name"
    )
    
    cursor.execute(query)
    rows = cursor.fetchall()

    print(f"\n-- {title} --")
    for film in rows:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre: {film[2]}\nStudio: {film[3]}\n")

try:
    db = mysql.connector.connect(**config) # Establish database connection
    cursor = db.cursor()
    show_films(cursor, "DISPLAYING FILMS") # Display all films
    
    # Placed to delete duplicate lines of inserted film (The Signal)
    # cursor.execute("DELETE FROM film WHERE film_name = 'The Signal';")
        
    # Insert a new film record (The Signal) --- tested and works ---
    #cursor.execute("""
    #    INSERT INTO film (film_name, film_director, film_releaseDate, film_runtime, genre_id, studio_id)
    #    VALUES ('The Signal', 'William Eubank', '2014', 97, 2, 1);
    #""")
    
    #db.commit() # Commiting the inserted film ← cannot forget this step!

    # Display films after insert
    #show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
    
    # Updating the film Alien into the Horror genre
    cursor. execute("""
        UPDATE film
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
        WHERE film_name = 'Alien';
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")
    
    # Delete the film Gladiator from the DB
    cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator';
    """)
    db.commit()
    
    # Display films after deletion
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Handle connection or DB errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print(err)

# Close the connection here
finally:
    cursor.close()
    db.close()