def test_magazine_create():
    import sqlite3
    from lib.models.magazine import Magazine

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE magazines (id INTEGER PRIMARY KEY, name TEXT, category TEXT)")

    magazine = Magazine.create(cursor, "Tech Today", "Technology")
    assert magazine.name == "Tech Today"
    assert magazine.category == "Technology"