import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Define your initial data
countries = [('USA', 'US'), ('Canada', 'CA'), ('Mexico', 'MX')]
states = [('California', 1), ('New York', 1), ('Ontario', 2), ('Quebec', 2), ('Jalisco', 3), ('Nuevo Leon', 3)]
cities = [('Los Angeles', 1), ('New York City', 2), ('Toronto', 3), ('Montreal', 4), ('Guadalajara', 5), ('Monterrey', 6)]
postal_codes = [('90001',), ('10001',), ('M1B 1B5',), ('H1A 0A1',), ('44100',), ('64000',)]
locations = [('123 Main St', 1, 1), ('456 Broadway', 2, 2), ('789 Yonge St', 3, 3), ('321 Saint Laurent Blvd', 4, 4), ('654 Lopez Mateos Ave', 5, 5), ('987 Garza Sada Ave', 6, 6)]

if __name__ == "__main__":
    # Connect to the database
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Insert data into the tables
    cur.executemany("INSERT INTO countries (name, code) VALUES (%s, %s)", countries)
    cur.executemany("INSERT INTO states (name, country_id) VALUES (%s, %s)", states)
    cur.executemany("INSERT INTO cities (name, state_id) VALUES (%s, %s)", cities)
    cur.executemany("INSERT INTO postal_codes (code) VALUES (%s)", postal_codes)
    cur.executemany("INSERT INTO locations (address, postal_code_id, city_id) VALUES (%s, %s, %s)", locations)

    # Commit the transaction
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()