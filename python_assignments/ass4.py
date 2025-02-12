class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn==isbn:
                self.books.remove(book)
                return
        print(f"Book not found.")

    def find_book(self,isbn):
        for book in self.books:
            if book.isbn==isbn:
                return book
        return None

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(f"Title:{book.title},Author:{book.author},ISBN:{book.isbn},Copies:{book.copies}")

class Book:
    def __init__(self,title,author,isbn,copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.copies=copies

lib = Library()

book1=Book("Emerald", "Arthur", "123456", 10)
book2=Book("dune", "Harold", "654321", 40)
lib.add_book(book1)
lib.add_book(book2)

print("All books in the library:")
lib.display_books()

isbn_to_find="123456"
found_book=lib.find_book(isbn_to_find)
if found_book:
    print(f"\nFound book: Title: {found_book.title}, Author: {found_book.author}, ISBN: {found_book.isbn}, Copies: {found_book.copies}")
else:
    print(f"\nBook not found.")

isbn_to_remove="654321"
lib.remove_book(isbn_to_remove)
lib.display_books()
