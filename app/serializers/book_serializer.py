from app.books.book import Book


class BookSerializer:
    def serialize(self, book: Book) -> str:
        ...
