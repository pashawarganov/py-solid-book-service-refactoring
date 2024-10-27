from app.books.book import Book
from app.displays.book_display import BookDisplay


class ConsoleDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)
