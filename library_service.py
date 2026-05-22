from exceptions import (
    BookNotFoundError,
    BookUnavailableError,
    MemberNotFoundError,
    LoanNotFoundError,
    MemberAlreadyExistsError,
    BookAlreadyExistError  
)
from loan import Loan

class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = {}
        self._loan_counter = 0


    def add_book(self, book):
        if book.book_id in self._books:
            raise BookAlreadyExistError("Book with this ID already exists.")
        self._books[book.book_id] = book
        return f"Book '{book.title}' added successfully."
    
    def get_book(self, book_id: str):
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        return book

    def view_books(self):
        if not self._books:
            return "No books in the library."
        return list(self._books.values())
    
    def register_member(self, member):
        if member.member_id in self._members:   
            raise MemberAlreadyExistsError("Member with this ID already exists.")
        self._members[member.member_id] = member
        return f"Member '{member.name}' registered successfully."
    
    def get_member(self, member_id: str):
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        return member
    
    def view_members(self):
        if not self._members:
            return "No registered members."
        return list(self._members.values())

    def borrow_book(self, book_id: str, member_id: str):
        member = self.get_member(member_id)
        book = self.get_book(book_id)

        if not book.is_available:
            raise BookUnavailableError("Book is already borrowed.") 
        
        self._loan_counter += 1
        loan_id = f"LOAN{self._loan_counter:04d}"
        loan = Loan(loan_id, book_id, member_id)
        self._loans[loan_id] = loan
        book.set_available(False)
        member.borrow_book(book_id)
        return f" Member '{member.name}' borrowed '{book.title}' successfully.(Loan ID: {loan_id})"
    
    def return_book(self, book_id: str, member_id: str):
        member = self.get_member(member_id)
        book = self.get_book(book_id)   

        active_loan = None
        for loan in self._loans.values():
            if loan.book_id == book_id and loan.member_id == member_id and not loan.returned:
                active_loan = loan
                break   

        if active_loan is None:
            raise LoanNotFoundError("No active loan found for this book and member.")

        active_loan.mark_returned()
        book.set_available(True)
        member.return_book(book_id)
        return f" Member '{member.name}' returned '{book.title}' successfully."
    
    def view_loans(self):
        if not self._loans:
            return "No active loans."
        return list(self._loans.values())
    
    def view_active_loans(self):
        active_loans = [loan for loan in self._loans.values() if not loan.returned]
        if not active_loans:
            return "No active loans."
        return active_loans