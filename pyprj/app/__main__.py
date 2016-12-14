import sys

if sys.version_info < (3, 0):
    print('This program require Python 3 or higher.')
    print('Current using version is {0}.{1}'.format(sys.version_info[0], sys.version_info[1]))
    print('Program is exiting...')
    sys.exit(1)

from hello import Hello
from util.movies import Movies

greeting = Hello()
greeting.say()
fav_movies = Movies()
fav_movies.print_movies()