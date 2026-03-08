import sqlite3
from database import DB_NAME

def add_task(title, deadline):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "INSERT INTO tasks(title, deadline) VALUES (?,?)",
        (title, deadline)
    )

    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM tasks")

    tasks = c.fetchall()

    conn.close()
    return tasks