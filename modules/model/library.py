from dataclasses import dataclass
from typing import List


@dataclass
class Book:

    title: str
    author: str
    year: int
    id: int = 0

    def serialize(self):
        return self.__dict__

    def deserialize(data):
        return Book(**data)


class Library:
    def __init__(self):
        self.books: List[Book] = []
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

    def remove_book(self, id: int):
        book = None
        for b in self.books:
            if b.id == id:
                book: Book = b
                break

        # TODO: использовать какую-то ошибку
        if book:
            self.books.remove(book)

    def search_book_title(self, title: str) -> List[Book]:
        result = []
        for book in self.books:
            if book.title == title:
                result.append(book)
        return result

    # def search_book_author(self, author: str):
    #     result = []
    #     for book in self.books:
    #         if book.author == author:
    #             return result

    # def search_book_year(self, year: int):
    #     result = []
    #     for book in self.books:
    #         if book.year == year:
    #             return result

    def get_books(self):
        return self.books

    def serialize(self):
        return [book.serialize() for book in self.books]

    def deserialize(data):
        library = Library()

        for i in data:
            library.add_book(Book.deserialize(i))
        return library
