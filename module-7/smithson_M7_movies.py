# smithson_m7_movies.py
# This script connects to MySQL DB using credentials from the .env file
# 1. Display all studio records; 2. Display all genre tables.
# 3. Display movie names with runtime less than 2 hours (< 120 minutes).
# 4. Display film names grouped by director.

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Loading credentials from .env file
secrets = dotenv_values(".env")

# Database config
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    # Try connecting to the database
    db = mysql.connector.connect(**config)
    print(
        f"\n\n2713 Database user {config['user']} connected to MySQL "
        f"on host {config['host']} with database {config['database']}"
    )

    # Creating a cursor object
    cursor = db.cursor()

    # ----- Query 1: Display all studio records -----
    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio;")
    studios = cursor.fetchall()
    for studio in studios:
        print(
            f"Studio ID: {studio[0]}\n"
            f"Studio Name: {studio[1]}\n"
        )

    # ----- Query 2: Display all genre records -----
    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre;")
    genres = cursor.fetchall()
    for genre in genres:
        print(
            f"Genre ID: {genre[0]}\n"
            f"Genre Name: {genre[1]}\n"
        )

    # ----- Query 3: Display movie names with runtime < 120 minutes -----
    print("\n-- DISPLAYING Short Film RECORDS --")
    cursor.execute("""
        SELECT film_name, film_runtime
        FROM film
        WHERE film_runtime < 120
        ORDER BY film_name;
    """)
    short_films = cursor.fetchall()
    for name, runtime in short_films:
        print(f"Film Name: {name}\nRuntime: {runtime}\n")

    # ----- Query 4: Display film names grouped by director -----
    print("\n-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("""
        SELECT film_name, film_director
        FROM film
        ORDER BY film_director;
    """)
    director_records = cursor.fetchall()
    for film_name, director_name in director_records:
        print(f"Film Name: {film_name}\nDirector: {director_name}\n")

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n274C The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n274C The specified database does not exist")
    else:
        print(f"\n274C Database error: {err}")

finally:
    try:
        cursor.close()
        db.close()
        print("Database connection closed.")
    except:
        pass
