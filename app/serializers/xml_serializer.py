from xml.etree import ElementTree

from app.books.book import Book
from app.serializers.book_serializer import BookSerializer


class XMLSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
