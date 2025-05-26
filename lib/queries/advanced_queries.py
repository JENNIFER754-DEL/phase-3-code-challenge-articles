def get_magazines_with_multiple_authors(cursor):
    cursor.execute("""
        SELECT magazines.name FROM magazines
        JOIN articles ON articles.magazine_id = magazines.id
        GROUP BY magazines.id
        HAVING COUNT(DISTINCT articles.author_id) > 1
    """)
    return [row[0] for row in cursor.fetchall()]
