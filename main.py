from book import Book
from member import Member
from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    BookUnavailableError,
    MemberNotFoundError,
    LoanNotFoundError,
    LibraryError
)

def display_menu():
    print("\n==== Library Management System ====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("===================================")

def add_book(service):
    try:
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Title: ").strip()
        author = input("Enter Author: ").strip()
        book = Book(book_id, title, author)
        result = service.add_book(book)
        print(result)
    except LibraryError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def register_member(service):
    try:
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        member = Member(member_id, name, email)
        result = service.register_member(member)
        print(result)
    except LibraryError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def borrow_book(service):
    try:        
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        result = service.borrow_book(book_id, member_id)
        print(result)
    except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def return_book(service):
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        result = service.return_book(book_id, member_id)
        print(result)

    except (LoanNotFoundError, BookNotFoundError, MemberNotFoundError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def view_books(service):
    try:
        books = service.view_books()
        if not books:
            print("No books in the library.")
        else:
            print("\n--- Books ---")
            for book in books:
                print(book)
    except Exception as e:
        print(f"Unexpected error: {e}")

def view_members(service):
    try:
        members = service.view_members()
        if not members:
            print("No registered members.")
        else:
            print("\n--- Members ---")
            for member in members:
                print(member)
    except Exception as e:
        print(f"Unexpected error: {e}")

def view_loans(service):
    try:
        loans = service.view_loans()
        if not loans:
            print("No active loans.")
        else:
            print("\n--- Active Loans ---")
            for loan in loans:
                print(loan)
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    service = LibraryService()
    try:
        service.add_book(Book("B001", "Python Basics", "John Doe"))
        service.add_book(Book("B002", "Data Structures", "Enielle Elly"))
        service.add_book(Book("B003", "Clean Code", "Cheng Yue"))

        service.register_member(Member("M101", "Olivia Rodrigo", "Livie@example.com"))
        service.register_member(Member("M102", "Yan HaoXiang", "Haoer@example.com"))

    except LibraryError as e:
        print(f"Error during setup: {e}")

    while True:
        display_menu()
        choice = input("Choose an option (1-8): ").strip()
        if choice == "1":
            add_book(service)
        elif choice == "2":
            register_member(service)
        elif choice == "3":
            borrow_book(service)
        elif choice == "4":
            return_book(service)
        elif choice == "5":
            view_books(service)
        elif choice == "6":
            view_members(service)
        elif choice == "7":
            view_loans(service)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()