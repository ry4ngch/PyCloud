from db_connect import DBConnect
from collections import deque

db = 'books-collections.db'

class Book:
    def __init__(self, db):
        self.db = db
        self.connect()

    def connect(self):
        with DBConnect(self.db) as con:
            con.execute(
                "CREATE TABLE IF NOT EXISTS books ("
                "id INTEGER PRIMARY KEY, "
                "title varchar(250) NOT NULL UNIQUE, "
                "author varchar(250) NOT NULL, "
                "rating FLOAT NOT NULL)"
            )

    def insert_book(self, title, author, rating):
        with DBConnect(self.db) as con:
            con.execute("INSERT INTO books VALUES (NULL, ?, ?, ?)", (title, author, rating))

    def get_books(self):
        with DBConnect(self.db) as con:
            res = con.execute("SELECT * from books")
            rows = res.fetchall()
            results = deque()
            headers = list(map(lambda x: x[0], con.cur.description))

            for row in rows:
                result = dict()
                for index, item in enumerate(row):
                    result[headers[index]] = item

                results.append(result)

            return results

    def update_book(self, index, title, author, rating):
        with DBConnect(self.db) as con:
            con.execute("UPDATE books SET title = ?, author = ?, rating = ? WHERE id = ?", (title, author, rating, index))

    def get_book(self, id):
        with DBConnect(self.db) as con:
            res = con.execute("SELECT * from books WHERE id = ?", id)
            row = res.fetchone()
            headers = list(map(lambda x: x[0], con.cur.description))
            return dict(zip(headers, row))

    def delete_book(self, id):
        with DBConnect(self.db) as con:
            con.execute("DELETE from books where id = ?", id)




books = Book(db)