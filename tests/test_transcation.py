def test_add_author_with_articles():
    import sqlite3
    from lib.transaction_handler import add_author_with_articles

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE articles (id INTEGER PRIMARY KEY, title TEXT, content TEXT, author_id INTEGER, magazine_id INTEGER)")

    author_id = add_author_with_articles(cursor, "Eve", [("T1", "Body1", 1), ("T2", "Body2", 1)])
    cursor.execute("SELECT name FROM authors WHERE id = ?", (author_id,))
    assert cursor.fetchone()[0] == "Eve"

    cursor.execute("SELECT COUNT(*) FROM articles WHERE author_id = ?", (author_id,))
    assert cursor.fetchone()[0] == 2
