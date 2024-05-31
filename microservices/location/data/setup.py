import os
import psycopg2

from dotenv import load_dotenv
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

load_dotenv()

if __name__ == "__main__":
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(
        dbname="postgres",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    # Allow database creation
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Create a new database
    cur.execute(f"CREATE DATABASE {os.getenv('DB_NAME')}")

    # Close the cursor and the connection
    cur.close()
    conn.close()

    # Connect to the new database
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Create tables
    cur.execute("""
        CREATE TABLE countries (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            code VARCHAR(255)
        )
    """)

    cur.execute("""
        CREATE TABLE states (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            country_id INTEGER REFERENCES countries(id)
        )
    """)

    cur.execute("""
        CREATE TABLE cities (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            state_id INTEGER REFERENCES states(id)
        )
    """)

    cur.execute("""
        CREATE TABLE postal_codes (
            id SERIAL PRIMARY KEY,
            code CHAR(10) UNIQUE NOT NULL
        )
    """)


    cur.execute("""
        CREATE TABLE locations (
            id SERIAL PRIMARY KEY,
            address TEXT NOT NULL,
            postal_code_id INTEGER REFERENCES postal_codes(id) NOT NULL,
            city_id INTEGER REFERENCES cities(id)
        );
        
        CREATE INDEX idx_locations_postal_code_id ON locations(postal_code_id);
    """)

    # Commit the transaction
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()
