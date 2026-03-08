import sqlite3

DB = "notionlite.db"

def connect():
    return sqlite3.connect(DB)

def init_db():
    conn = connect()
    cur = conn.cursor()

    # Pages table (Nested Notion-style structure)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        parent_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (parent_id) REFERENCES pages (id) ON DELETE CASCADE
    )
    """)

    # Tasks table (Missing in previous version)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        deadline TEXT,
        status TEXT DEFAULT 'todo',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Notes table (Missing in previous version)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Backlinks (Obsidian-style)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS links(
        source_id INTEGER,
        target_id INTEGER,
        PRIMARY KEY (source_id, target_id),
        FOREIGN KEY (source_id) REFERENCES pages (id) ON DELETE CASCADE,
        FOREIGN KEY (target_id) REFERENCES pages (id) ON DELETE CASCADE
    )
    """)

    # Full Text Search (FTS5) for instant global search
    cur.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS page_search 
    USING FTS5(page_id UNINDEXED, title, content)
    """)

    conn.commit()
    conn.close()

def sync_search_index():
    """Manually sync the FTS5 table with current pages."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM page_search")
    cur.execute("INSERT INTO page_search(page_id, title, content) SELECT id, title, content FROM pages")
    conn.commit()
    conn.close()