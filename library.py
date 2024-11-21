class Book:

    def __init__(self, ID, title, author, year,status):
        self.ID = ID
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def show(self):
        print(self.title, self.author, self.year)

    def get_attribute_string(self):
        print(str(self.title) + '_' + str(self.author) + '_' + str(self.year))

    def get_title(self):
        print(self.title)

    def get_author(self):
        print(self.author)

    def get_year(self):
        print(self.year)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, Book):
        self.books.append(Book)

    def remove_book(self, Book):
        self.books.remove(Book)

   
    def show_all(self):
        for Book in self.books:
            Book.show()



if __name__ == '__main__':
    lib = Library()
    book1 = Book(1, 'Bookname1', "$30")
    book2 = Book(2, 'Bookname2', "$10")
    book3 = Book(3, 'Bookname3', "$40")
    #1.show_id
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)
    lib.remove_book(book2)
    lib.show_all()