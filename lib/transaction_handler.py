def add_author_with_articles(cursor, author_name, articles_data):
    cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))
    author_id = cursor.lastrowid

    for article in articles_data:
        title, content, magazine_id = article
        cursor.execute(
            "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
            (title, content, author_id, magazine_id)
        )
    return author_id