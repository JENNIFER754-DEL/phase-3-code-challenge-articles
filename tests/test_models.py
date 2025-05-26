def test_author_create():
    import sqlite3
    from lib.models.author import Author

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT)")

    author = Author.create(cursor, "Jane Doe")
    assert author.name == "Jane Doe"