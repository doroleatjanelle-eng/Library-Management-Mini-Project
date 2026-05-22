class Member:
    def __init__(self, member_id: str, name: str, email: str):
        self._member_id = member_id
        self._name = name
        self._email = email
        self._borrowed_books = []

    @property
    def member_id(self):
        return self._member_id
    
    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def borrowed_books(self):
        return self._borrowed_books
    
    def borrow_book(self, book_id: str):
        if book_id not in self._borrowed_books:
            self._borrowed_books.append(book_id)
            return True
        return False
    
    def return_book(self, book_id: str):
        if book_id in self._borrowed_books:
            self._borrowed_books.remove(book_id)
            return True     
        return False
    
    def __str__ (self):
        return f"ID: {self._member_id}, \nName: {self._name}, \nEmail: {self._email}, \nBorrowed Books: {len(self._borrowed_books)}"