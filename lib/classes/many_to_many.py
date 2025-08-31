class Article:
    all = []

    def __init__(self, author, magazine, title):
        # validate types
        if not isinstance(author, Author):
            raise TypeError("author must be an Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    # title should behave as immutable to outside changes: ignore attempts to set invalid value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Title is immutable: ignore all assignments
        pass


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) == 0:
            raise ValueError("name must be non-empty")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Name is immutable: ignore all assignments
        pass

    def articles(self):
        # return list of Article instances authored by this author
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        # unique magazines (Magazine instances) the author has written for
        mags = [a.magazine for a in self.articles()]
        # preserve order but unique
        seen = []
        for m in mags:
            if m not in seen:
                seen.append(m)
        return seen

    def add_article(self, magazine, title):
        # create and return a new Article with self as author
        return Article(self, magazine, title)

    def topic_areas(self):
        # return list of unique magazine categories for this author's articles
        cats = [m.category for m in self.magazines()]
        if not cats:
            return None
        seen = []
        for c in cats:
            if c not in seen:
                seen.append(c)
        return seen


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("name length must be between 2 and 16")
        if len(category) == 0:
            raise ValueError("category must be non-empty")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # mutable but validated: only change for valid values
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # else: ignore invalid assignments

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # mutable but validated: only change for valid values
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # else: ignore invalid assignments

    def articles(self):
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        authors = [a.author for a in self.articles()]
        # unique preserving order
        seen = []
        for auth in authors:
            if auth not in seen:
                seen.append(auth)
        return seen

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        # authors who have written more than 2 articles for this magazine
        authors = {}
        for a in self.articles():
            authors[a.author] = authors.get(a.author, 0) + 1
        contrib = [author for author, count in authors.items() if count > 2]
        if not contrib:
            return None
        return contrib
