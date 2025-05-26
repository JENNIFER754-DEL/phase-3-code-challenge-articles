import sqlite3
from lib.models.article import Article

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, cursor, name):
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        return cls(cursor.lastrowid, name)

    @classmethod
    def all(cls, cursor):
        cursor.execute("SELECT id, name FROM authors")
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    def articles(self, cursor):
        cursor.execute("SELECT id, title, content, magazine_id FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        return [Article(row[0], row[1], row[2], self.id, row[3]) for row in rows]

    def magazines(self, cursor):
        cursor.execute("SELECT DISTINCT magazines.id, magazines.name, magazines.category FROM magazines \n                        JOIN articles ON articles.magazine_id = magazines.id\n                        WHERE articles.author_id = ?", (self.id,))
        return cursor.fetchall()
