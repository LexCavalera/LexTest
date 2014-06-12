from pymongo import MongoClient
from bson.objectid import ObjectId


_client = None


def get_client(host='localhost', port=27017):
    global _client
    if _client is None:
        _client = MongoClient(host, port)
    return _client


def get_db(db='library'):
    return get_client()[db]


def get_collection(collection='books'):
    return get_db()['books']


def get_books():
    book_list = list(get_collection().find())
    for book in book_list:
        book['_id'] = str(book['_id'])
    return book_list


def add_book(book):
    collection = get_collection()
    _id = collection.insert(book)
    return str(_id)
    

def remove_book(_id):
    collection = get_collection()
    collection.remove(ObjectId(_id))


def update_book(book,
                update_fields=['name', 'author', 'release_date', 'keywords']):
    collection = get_collection()
    _id = ObjectId(book['_id'])
    update_values = dict([(field, book[field]) for field in update_fields])
    collection.update({'_id': _id}, {'$set': update_values})
    

'''
from book import Book

new_book = Book({'name': 'Book1',
                 'author': 'Author1',
                 'release_date': 'Date1',
                 'keywords': 'Keywords1'})
_id = add_book(new_book.to_dict())
new_book.set_id(_id)
books = get_books()
print books
first_book = books[0]
first_book['name'] = 'Super book'
update_book(first_book, ['name'])
books = get_books()
print books'''

