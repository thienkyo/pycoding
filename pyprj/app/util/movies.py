from abc import ABCMeta, abstractmethod


class Movies(metaclass=ABCMeta):
    def __init__(self):
        self.title = ''
        self.genre = ''

    def _make_a_movies(self):
        self.title = 'Titanic'
        self.genre = 'Drama'

    def print_movies(self):
        self._make_a_movies()
        print('Title: {0}. Genre: {1}'.format(self.title, self.genre))