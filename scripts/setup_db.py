import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../lib/db/articles.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), '../lib/db/schema.sql')

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    with open(SCHEMA_PATH, 'r') as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")

if __name__ == "__main__":
    setup_database()
