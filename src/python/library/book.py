class Book(object):

    def __init__(self, attributes):
        self._name = attributes['name']
        self._author = attributes['author']
        self._release_date = attributes['release_date']
        self._keywords = attributes['keywords']
        self._id = attributes.get('_id')

    def update(self, attributes):
        if attributes.get('name') is not None:
            self._name = attributes['name']
        if attributes.get('author') is not None:
            self._author = attributes['author']
        if attributes.get('release_date') is not None:
            self._release_date = attributes['release_date']
        if attributes.get('keywords') is not None:
            self._keywords = attributes['keywords']

    def set_id(self, _id):
        self._id = _id

    def get_id(self):
        return self._id

    def to_dict(self):
        result = {'name': self._name,
                  'author': self._author,
                  'release_date': self._release_date,
                  'keywords': self._keywords}
        if self._id:
            result['_id'] = self._id
        return result
