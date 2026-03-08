from core.database import connect


def get_graph():

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT source_id,target_id FROM links")

    edges = cur.fetchall()

    conn.close()

    return edges