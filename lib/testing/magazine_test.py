# lib/magazine.py
class Magazine:
    all_magazines = []
    
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # Use setters for validation
        self.category = category
        self._articles = []
        Magazine.all_magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) <= 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value
    
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles))
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        
        magazines_with_articles = [mag for mag in cls.all_magazines if mag.articles()]
        if not magazines_with_articles:
            return None
        
        return max(magazines_with_articles, 
                  key=lambda magazine: len(magazine.articles()))