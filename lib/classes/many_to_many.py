class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value

    @staticmethod
    def get_all_articles():
        return Article.all


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return self._articles

    def add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        authors_count = {}
        for article in Article.all:
            if article.magazine == self:
                authors_count[article.author] = authors_count.get(article.author, 0) + 1


        contributing_authors = [author for author, count in authors_count.items() if count > 2]
        
        return contributing_authors if contributing_authors else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)
class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
        self._magazines = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        if hasattr(self, '_name'):
            raise ValueError("Name cannot be changed once set.")
        self._name = value

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        magazine.add_article(article)
        self._articles.append(article)
        if magazine not in self._magazines:
            self._magazines.append(magazine)
        return article

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))

    def topic_areas(self):
        return list(set(magazine.category for magazine in self._magazines)) or None