from author import Author, Magazine, Article

# Sample Data
author1 = Author("Daniel")
author2 = Author("Abdi")
mag1 = Magazine("Tech Times", "Technology")
mag2 = Magazine("Health Hub", "Health")

article1 = author1.add_article(mag1, "Future of Moringa")
article2 = author1.add_article(mag2, "Health is Wealth")
article3 = author2.add_article(mag1, "Cloud Computing")
article4 = author1.add_article(mag1, "Respect and Ethics")

print(f"Author {author1.name} has written articles: {[a.title for a in author1.articles()]}")
print(f"Magazine {mag1.name} contributors: {[a.name for a in mag1.contributors()]}")
print(f"Top publisher: {Magazine.top_publisher().name}")
