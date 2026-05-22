from datetime import datetime

class Loan:
    def __init__(self, loan_id: str, member_id: str, book_id: str):
        self._loan_id = loan_id
        self._member_id = member_id 
        self._book_id = book_id
        self._borrow_date = datetime.now()
        self._return_date = None
        self._is_returned = False

    @property
    def loan_id(self):
        return self._loan_id
    
    @property
    def member_id(self):
        return self._member_id
    
    @property
    def book_id(self):
        return self._book_id
    
    @property
    def borrow_date(self):
        return self._borrow_date
    
    @property
    def return_date(self):
        return self._return_date

    @property
    def is_returned(self):
        return self._is_returned
    
    def mark_as_returned(self):
        self._is_returned = True
        self._return_date = datetime.now()

    def __str__(self):
        status = "Returned" if self._is_returned else "Borrowed"
        return f"Loan ID: {self._loan_id}, \nMember ID: {self._member_id}, \nBook ID: {self._book_id}, \nBorrow Date: {self._borrow_date}, \nReturn Date: {self._return_date}, \nStatus: {status}"