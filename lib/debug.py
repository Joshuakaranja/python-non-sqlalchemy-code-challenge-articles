#!/usr/bin/env python3
import ipdb

# Import from the correct location (classes/many_to_many.py)
from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create some sample data for testing
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    article1 = Article(author1, magazine1, "The Future of AI")
    article2 = Article(author1, magazine2, "Healthy Eating Habits")
    article3 = Article(author2, magazine1, "Python Programming Tips")
    article4 = Article(author2, magazine1, "Web Development Trends")
    article5 = Article(author2, magazine1, "Data Science Fundamentals")

    # Make Article.all available as the tests expect
    # (Assuming the Article class has an all_articles class variable)
    Article.all = Article.all_articles

    # don't remove this line, it's for debugging!
    ipdb.set_trace()