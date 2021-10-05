import psycopg2
from os import environ

# DATABASE_URL = environ['DATABASE_URL']
DATABASE_URL = 'dburl'

class DB_Conn:
    def __init__(self):
        self.app = None

    def init_app(self, app):
        self.app = app
        self.connect()

    def connect(self):
        self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        return self.conn

    def get_db(self):
        if not self.conn:
            return self.connect()
        return self.conn

    def close(self):
        self.conn.close()

db_conn = DB_Conn()