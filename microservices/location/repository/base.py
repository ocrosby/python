from typing import Any, Dict
import psycopg2
import os


class BaseRepository:
    table_name: str
    conn: Any
    cursor: Any

    def __init__(self, table_name: str):
        self.table_name = table_name
        self.conn = psycopg2.connect(database=os.getenv("DB_NAME"),
                                           user=os.getenv("DB_USER"),
                                           password=os.getenv("DB_PASS"),
                                           host=os.getenv("DB_HOST"),
                                           port=os.getenv("DB_PORT"))

        self.cursor = self.conn.cursor()

    def create(self, data: Dict[str, Any]):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values})"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def find_all(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()

    def find_by_id(self, id: int):
        self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id = %s", (id,))
        return self.cursor.fetchone()

    def update(self, id: int, data: Dict[str, Any]):
        keys_and_values = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {self.table_name} SET {keys_and_values} WHERE id = %s"
        self.cursor.execute(query, tuple(data.values()) + (id,))
        self.conn.commit()

    def delete(self, id: int):
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = %s", (id,))
        self.conn.commit()