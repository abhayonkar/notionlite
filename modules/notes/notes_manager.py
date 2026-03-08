from core.database import connect
import datetime


def add_note(title, content):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO notes(title,content,created_at) VALUES(?,?,?)",
        (title,content,str(datetime.datetime.now()))
    )

    conn.commit()
    conn.close()


def get_notes():

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM notes")

    data = cur.fetchall()

    conn.close()

    return data