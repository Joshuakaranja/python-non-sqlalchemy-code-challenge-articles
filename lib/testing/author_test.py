# lib/author.py
class Author:
    all_authors = []
    
    def __init__(self, name):
        self._name = None  # Initialize to None first
        self.name = name   # Use the setter for validation
        self._articles = []
        Author.all_authors.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name') or self._name is None:
            if not isinstance(value, str) or len(value) <= 0:
                raise ValueError("Name must be a non-empty string")
            self._name = value
        else:
            raise AttributeError("Name cannot be changed after instantiation")
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article
    
    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))