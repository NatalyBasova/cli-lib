from dataclasses import dataclass
from typing import List


@dataclass
class Book:

    title: str
    author: str
    id: int = 0

    def serialize(self):
        return self.__dict__

    def deserialize(data):
        return Book(**data)


class Library:
    def __init__(self):
        self.books = []
        self.serial_id: int = 1

    def add_book(self, book: Book):

        if book.id == 0:
            book.id = self.serial_id
            self.serial_id = +1

        filtered = list(filter(lambda x: x.id == book.id, self.books))

        if len(filtered) == 0:

            if self.serial_id <= book.id:
                self.serial_id = book.id + 1

            self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_books(self):
        return self.books

    def serialize(self):
        return [book.serialize() for book in self.books]

    def deserialize(data):
        library = Library()

        for i in data:
            library.add_book(Book.deserialize(i))
        return library
