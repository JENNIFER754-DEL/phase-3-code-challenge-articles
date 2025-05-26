from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

def test_author_creation():
    author = Author.create("Test Author")
    assert author.name == "Test Author"
    assert author.id is not None

def test_find_by_id_and_name():
    author = Author.create("Find Me")
    found_by_id = Author.find_by_id(author.id)
    found_by_name = Author.find_by_name("Find Me")
    assert found_by_id.id == author.id
    assert found_by_name[0].name == "Find Me"

def test_articles_and_magazines_relationship():
    author = Author.create("Rel Author")
    mag = Magazine.create("Rel Mag", "Science")
    author.add_article(mag, "Rel Article")
    
    articles = author.articles()
    magazines = author.magazines()
    topics = author.topic_areas()

    assert any(article.title == "Rel Article" for article in articles)
    assert any(mag.name == "Rel Mag" for mag in magazines)
    assert "Science" in topics

if __name__ == "__main__":
    test_author_creation()
    test_find_by_id_and_name()
    test_articles_and_magazines_relationship()
    print("All Author tests passed.")
