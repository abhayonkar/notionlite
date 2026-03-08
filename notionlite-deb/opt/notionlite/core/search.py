from core.database import connect


def search(query):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT title FROM page_search WHERE page_search MATCH ?",
        (query,)
    )

    results = cur.fetchall()

    conn.close()

    return results