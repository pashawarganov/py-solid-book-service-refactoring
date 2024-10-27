from app.books.book import Book
from app.displays.book_display import BookDisplay


class ReverseDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
