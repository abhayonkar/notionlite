import re
from core.database import connect

pattern = r"\[\[(.*?)\]\]"


def extract_links(page_id, text):

    conn = connect()
    cur = conn.cursor()

    links = re.findall(pattern, text)

    for link in links:

        cur.execute(
            "SELECT id FROM pages WHERE title=?",
            (link,)
        )

        res = cur.fetchone()

        if res:
            cur.execute(
                "INSERT INTO links VALUES (?,?)",
                (page_id,res[0])
            )

    conn.commit()
    conn.close()