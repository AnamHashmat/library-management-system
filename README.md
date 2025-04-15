class Book:
    def __init__(self, title, author, isbn, accession_number):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.accession_number = accession_number
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

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) < 5 and book.borrow():
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
        return overdue_days * 1.0


