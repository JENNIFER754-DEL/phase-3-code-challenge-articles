from lib.transaction import run_transaction

def add_author_and_articles(author_name, articles_data):
    def operations(conn):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))
        author_id = cursor.lastrowid
        for title, magazine_id in articles_data:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (title, author_id, magazine_id)
            )
    run_transaction(operations)
