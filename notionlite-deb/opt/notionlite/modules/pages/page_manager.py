from core.database import connect
import datetime


def create_page(title, parent=None):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO pages(title,parent_id,created_at) VALUES(?,?,?)",
        (title,parent,str(datetime.datetime.now()))
    )

    conn.commit()
    conn.close()


def get_children(parent):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM pages WHERE parent_id=?",
        (parent,)
    )

    pages = cur.fetchall()

    conn.close()

    return pages