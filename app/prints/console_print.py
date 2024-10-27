from app.books.book import Book
from app.prints.book_print import BookPrint


class ConsolePrint(BookPrint):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)
