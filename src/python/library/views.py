import json

from pyramid.view import view_config

from library import books
from library.utils import get_template_path


@view_config(renderer=get_template_path('index.jinja2'))
def hello_view(request):
    return {}


@view_config(renderer="json", name='books', request_method='GET')
def all_books_view(request):
    return books.get_all_books()


@view_config(renderer="json", name='books', request_method='POST')
def add_book_view(request):
    return books.add_book({'name': request.json_body['name'],
                           'author': request.json_body['author'],
                           'release_date': request.json_body['release_date'],
                           'keywords': request.json_body['keywords']})


@view_config(renderer="json", route_name='modify_books', request_method='DELETE')
def remove_book_view(request):
    return books.remove_book(request.matchdict['_id'])


@view_config(renderer="json", route_name='modify_books', request_method='PUT')
def update_book_view(request):
    return books.update_book({'_id': request.matchdict['_id'],
                              'name': request.json_body.get('name'),
                              'author': request.json_body.get('author'),
                              'release_date': request.json_body.get('release_date'),
                              'keywords': request.json_body.get('keywords')})
