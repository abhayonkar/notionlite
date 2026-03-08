import sqlite3

DB = "notionlite.db"


def connect():
    return sqlite3.connect(DB)


def init_db():

    conn = connect()
    cur = conn.cursor()

    # Pages table (nested structure)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pages(
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT,
        parent_id INTEGER,
        created_at TEXT
    )
    """)

    # backlinks
    cur.execute("""
    CREATE TABLE IF NOT EXISTS links(
        source_id INTEGER,
        target_id INTEGER
    )
    """)

    # full text search
    cur.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS page_search
    USING FTS5(title,content)
    """)

    conn.commit()
    conn.close()