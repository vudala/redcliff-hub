import os
import psycopg2
import json

DATABASE_URL = 'dburl'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

filepath = '../resources/scale.json'
with open(filepath, 'r') as f:
    data = json.loads(f.read())

for k in data:
    try:
        cursor.execute(
            """
            INSERT INTO scaling (level, info)
            VALUES (%s,%s)
            """,
            (
                k,
                json.dumps(data[k])
            )
        )

        print('success')

        conn.commit()
    except Exception as e:
        print('fail: {}'.format(e))
        conn.rollback()

cursor.close()
conn.close()