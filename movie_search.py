import django
from omdbapi.movie_search import GetMovie
movie = GetMovie(title='Passengers', api_key='38e42f62')


print(django.get_version())