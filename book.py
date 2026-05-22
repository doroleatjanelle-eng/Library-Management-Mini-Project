class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._is_available = True

    @property
    def book_id(self):
        return self._book_id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def is_available(self):
        return self._is_available

    def set_available(self, available: bool):
        self._is_available = available

    def __str__(self):
        status = "Available"  if self._is_available else "Borrowed"
        return f"ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Status: {status}"