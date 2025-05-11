class PostgresConnection:
    def __init__(self):
        self.connection_params = psycopg2.connect(
            host="ep-old-tooth-a2vlt1z0-pooler.eu-central-1.aws.neon.tech",
            database="neondb",
            user="neondb_owner",
            password="npg_VXuMjw9Bhyd7"
        )
        self.cur = None
        self.conn = None


    def connect(self):
        self.conn = psycopg2.connect(**self.connection_params)
        self.cur = self.conn.cursor()


    def close(self):
        if self.cur: self.cur.close()
        if self.conn: self.conn.close()


    def execute_query(self, sql, params=None, fetch=False):
        self.connect() 
        self.cur.execute(sql, params)
        result = self.cur.fetchall() if fetch else None
        self.conn.commit() 
        self.close()
        return result