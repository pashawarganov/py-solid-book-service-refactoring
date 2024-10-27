import json

from app.books.book import Book
from app.serializers.book_serializer import BookSerializer


class JSONSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})
