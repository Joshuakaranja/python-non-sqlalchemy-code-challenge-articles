# lib/article.py
class Article:
    all_articles = []
    
    def __init__(self, author, magazine, title):
        self._title = None
        self._author = None
        self._magazine = None
        
        # Use setters for validation
        self.title = title
        self.author = author
        self.magazine = magazine
        
        Article.all_articles.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not hasattr(self, '_title') or self._title is None:
            if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
                raise ValueError("Title must be a string between 5 and 50 characters")
            self._title = value
        else:
            raise AttributeError("Title cannot be changed after instantiation")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        
        # Remove from old author's list if changing
        if hasattr(self, '_author') and self._author:
            self._author._articles.remove(self)
        
        self._author = value
        value._articles.append(self)
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        
        # Remove from old magazine's list if changing
        if hasattr(self, '_magazine') and self._magazine:
            self._magazine._articles.remove(self)
        
        self._magazine = value
        value._articles.append(self)