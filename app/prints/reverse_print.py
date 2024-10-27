from app.books.book import Book
from app.prints.book_print import BookPrint


class ReversePrint(BookPrint):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
