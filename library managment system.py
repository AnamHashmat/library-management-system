class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        return False

    def list_books(self):
        return [book for book in self.books if not book.is_borrowed]

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
            return False
    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
            return False
class Librarian:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def search_book(self, books, title):
        return [book for book in books if title.lower() in book.title.lower()]

    def calculate_fine(self, overdue_days):
        return overdue_days * 1.0 # Example: $1 fine per overdue day
    
    
    # Example usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
book2 = Book("1984", "George Orwell", "0987654321")
user = User("Alice", 1)
librarian = Librarian("Bob", 101)

books = [book1, book2]
# Borrow a book
if user.borrow_book(book1):
    print(f"{user.name} borrowed ’{book1.title}’")

 # Search for a book
results = librarian.search_book(books, "1984")
for book in results:
     print(f"Found: {book.title} by {book.author}")

 # Return a book
if user.return_book(book1):
    print(f"{user.name} returned ’{book1.title}’")

 # Fine calculation
print(f"Fine for 3 overdue days: ${librarian.calculate_fine(3)}")
