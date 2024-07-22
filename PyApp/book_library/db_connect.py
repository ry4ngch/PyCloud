import sqlite3


class DBConnect:
    def __init__(self, db):
        self.db = db
        self.con = None
        self.cur = None

    def __enter__(self):
        try:
            self.con = sqlite3.connect(self.db)
            return self
        except sqlite3.OperationalError as err:
            print("Database does not exist")
            print(err)

    def execute(self, query, params=None):
        self.cur = self.con.cursor()
        try:
            result = self.cur.execute(query, params or ())
            self.con.commit()
        except Exception as e:
            result = e
        return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()