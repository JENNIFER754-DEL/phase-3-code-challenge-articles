class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def create(cls, cursor, title, content, author_id, magazine_id):
        cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
                       (title, content, author_id, magazine_id))
        return cls(cursor.lastrowid, title, content, author_id, magazine_id)
