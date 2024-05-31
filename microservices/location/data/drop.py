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

    # Allow database operations
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Drop the database if it already exists
    cur.execute(f"DROP DATABASE IF EXISTS {os.getenv('DB_NAME')}")

    # Close the cursor and the connection
    cur.close()
    conn.close()
