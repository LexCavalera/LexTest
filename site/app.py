import os

from wsgiref.simple_server import make_server

from pyramid.config import Configurator



def create_views(config):
    config.add_route('modify_books', '/books/{_id}')
    config.scan('library.views')
    config.add_static_view(name='js', path='js')
    config.add_static_view(name='css', path='css')
    config.add_static_view(name='img', path='img')


def main():
    config = Configurator()
    config.include('pyramid_jinja2')
    create_views(config)
    app = config.make_wsgi_app()
    return app


if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
