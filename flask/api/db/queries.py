import os
import psycopg2
import json
from .connection import db_conn 

conn = db_conn.get_db()

def scaling(start, end):
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT info FROM scaling WHERE level >= %s AND level <= %s
            """,
            (start, end)
        )

        conn.commit()
    except:
        conn.rollback()

    rows = cursor.fetchall()
    cursor.close()

    query = {}
    i = 0
    while start <= end:
        try:
            query[start] = rows[i][0]
            start += 1
            i += 1
        except:
            return query

    return query