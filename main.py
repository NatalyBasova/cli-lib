#!/usr/bin/env python


from modules import cli
from modules import model
from modules import storage


def main():
    args = cli.parse_args()

    library = model.Library.deserialize(storage.read_data(args.storage_path))

    if args.cmds == "add":
        book = model.Book(title=args.title, author=args.author, year=int(args.year))
        library.add_book(book=book)

    if args.cmds == "del":
        library.remove_book(id=int(args.id))

    if args.cmds == "search":
        if args.title:
            result = library.search_book_title(title=str(args.title))
        if args.author:
            result = library.search_book_author(author=str(args.author))
        if args.year:
            result = library.search_book_year(year=int(args.year))

        model.print_books(result)

    if args.cmds == "show":
        model.print_books(library.books)

    storage.save(data=library.serialize(), path=args.storage_path)


if __name__ == "__main__":
    main()
