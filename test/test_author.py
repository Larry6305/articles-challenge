from lib.models.author import Author
from lib.models.magazine import Magazine

def test_author_can_add_article():
    author = Author("Test Author")
    author.save()
    mag = Magazine("Test Mag", "Science")
    mag.save()
    article = author.add_article(mag, "Cool Article")
    assert article.title == "Cool Article"
