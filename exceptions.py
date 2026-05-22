class LibraryError(Exception):
    """Base class for all library-related errors."""
    pass

class BookUnavailableError(LibraryError):
    """Raised when a book is already borrowed."""
    pass

class BookNotFoundError(LibraryError):
    """Raised when a book does not exist."""
    pass

class MemberNotFoundError(LibraryError):
    """Raised when a member does not exist."""
    pass

class LoanNotFoundError(LibraryError):
    """Raised when there is no active loan for the book."""
    pass

class MemberAlreadyExistsError(LibraryError):
    """Raised when trying to register a member with an existing ID."""
    pass

class BookAlreadyExistError(LibraryError):
    """Raised when trying to add a book with an existing ID."""
    pass