#!/usr/bin/env python


# from modules import cli
# from modules import model
from modules import storage


def main():
    a = [
        {"id": 1, "title": "mybook1", "author": "Basova1"},
        {"id": 2, "title": "mybook2", "author": "Basov41"},
        {"id": 3, "title": "mybook3", "author": "Basova51"},
    ]

    print(storage.save(a))


if __name__ == "__main__":
    main()
