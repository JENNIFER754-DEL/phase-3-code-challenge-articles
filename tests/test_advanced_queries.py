def test_get_magazines_with_multiple_authors():
    import sqlite3
    from lib.models.magazine import Magazine
    from lib.models.author import Author
    from lib.models.article import Article
    from lib.queries.advanced_queries import get_magazines_with_multiple_authors

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE magazines (id INTEGER PRIMARY KEY, name TEXT, category TEXT)")
    cursor.execute("CREATE TABLE articles (id INTEGER PRIMARY KEY, title TEXT, content TEXT, author_id INTEGER, magazine_id INTEGER)")

    m1 = Magazine.create(cursor, "Science Weekly", "Science")
    a1 = Author.create(cursor, "Alice")
    a2 = Author.create(cursor, "Bob")

    Article.create(cursor, "A1", "C1", a1.id, m1.id)
    Article.create(cursor, "A2", "C2", a2.id, m1.id)

    result = get_magazines_with_multiple_authors(cursor)
    assert "Science Weekly" in result
