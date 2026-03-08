import sqlite3
from database import DB_NAME

def add_note(title, content):

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "INSERT INTO notes(title, content) VALUES (?,?)",
        (title, content)
    )

    conn.commit()
    conn.close()


def get_notes():

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM notes")

    notes = c.fetchall()

    conn.close()
    return notes