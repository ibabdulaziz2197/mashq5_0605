# 5
class Book:
    def __init__(self, title, author, pages, code):
        self.title = title
        self.author = author
        self._pages = pages          # protected
        self.__code = code           # private

    def read(self, pages):
        print(f"Reading {pages} pages")

    def bookmark(self, page):
        print(f"Bookmark at {page}")

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self._pages}")

book1 = Book("Python Basics", "Ali Valiyev", 200, "B001")

book1.read(10)
book1.bookmark(50)
