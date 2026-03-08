from core.database import connect
import datetime


def add_task(title, deadline):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tasks(title,deadline,status,created_at) VALUES(?,?,?,?)",
        (title,deadline,"todo",str(datetime.datetime.now()))
    )

    conn.commit()
    conn.close()


def get_tasks():

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM tasks")

    tasks = cur.fetchall()

    conn.close()

    return tasks