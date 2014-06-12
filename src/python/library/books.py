from library import api_db
from library.book import Book


_books = None


def _fill_books():
    global _books
    _books = []
    for book in api_db.get_books():
        _books.append(Book(book))


def get_books():
    if _books is None:
        _fill_books()
    return _books


def find_book(_id):
    for book in get_books():
        if book.get_id() == _id:
            return book


def get_all_books():
    return [book.to_dict() for book in get_books()]


def add_book(book):
    new_book = Book(book)
    _id = api_db.add_book(book)
    new_book.set_id(_id)
    get_books().append(new_book)
    return new_book.to_dict()


def remove_book(_id):
    api_db.remove_book(_id)
    books = get_books()
    books.remove(find_book(_id))
    return 'Removed'


def update_book(book):
    for key in book.keys():
        if book[key] is None:
            del(book[key])
    updated_book = find_book(book['_id'])
    updated_book.update(book)
    api_db.update_book(updated_book.to_dict())
    return 'Updated'
