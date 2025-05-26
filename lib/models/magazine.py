class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, cursor, name, category):
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
