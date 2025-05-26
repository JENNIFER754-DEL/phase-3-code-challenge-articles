from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_creation():
    author = Author.create("Article Author")
    magazine = Magazine.create("Article Mag", "Culture")
    article = Article.create("New Article", author.id, magazine.id)
    assert article.title == "New Article"
    assert article.author_id == author.id
    assert article.magazine_id == magazine.id
    assert article.id is not None

def test_find_methods():
    author = Author.create("Find Author")
    magazine = Magazine.create("Find Mag", "Health")
    article = Article.create("Find Article", author.id, magazine.id)

    found_by_id = Article.find_by_id(article.id)
    found_by_title = Article.find_by_title("Find Article")
    found_by_author = Article.find_by_author(author.id)
    found_by_magazine = Article.find_by_magazine(magazine.id)

    assert found_by_id.title == article.title
    assert any(a.title == "Find Article" for a in found_by_title)
    assert all(a.author_id == author.id for a in found_by_author)
    assert all(a.magazine_id == magazine.id for a in found_by_magazine)

if __name__ == "__main__":
    test_article_creation()
    test_find_methods()
    print("All Article tests passed.")
