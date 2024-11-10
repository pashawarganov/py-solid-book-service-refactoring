from app.book import Book


class BookDisplay:
    def display(self, book: Book) -> None:
        ...


class ConsoleDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
