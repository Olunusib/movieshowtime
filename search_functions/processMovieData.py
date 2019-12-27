from imdb import IMDb
import json
import sys

# a dict storing dicts of movies titles as keys with a nested dict for the movie's metadata
movies = {}

# intilising an instance of IMDb api
mdb = IMDb()


# takes an argument of a file path in a sting format
# build a dict with movie title as key and movie metadata nested dict (keys: rating, genre, plot, cast, directors, runtime )
def ProcessData(filePath):
    with open(filePath, 'r') as movieList:
        moviesList = json.load(movieList)
        for movie in moviesList:
            for key, value in movie.items():
                if IDgetter(key) == None:
                    continue
                rating, genre, plot, cast, directors, runtime = getMetaData(key)
                movies[key] = value
                movie[key]['rating'] = rating
                movie[key]['genre'] = genre
                movie[key]['plot'] = plot
                movie[key]['cast'] = [str(actor) for actor in cast]
                movie[key]['directors'] = [str(director) for director in directors]
                movie[key]['runtime'] = runtime
    with open('moviesDict.json', 'w') as moviesDict:
        json.dump(movies, moviesDict)


# get movie meta data
def getMetaData(title):
    movie_ID = IDgetter(title)
    movie = mdb.get_movie(movie_ID)

    if movie.get('rating'):
        rating = movie.get('rating')
    else:
        rating = None
    if movie.get('genre'):
        genre = movie.get('genre')
    else:
        genre = None
    if movie.get('plot'):
        plot = movie.get('plot')
    else:
        plot = None
    if movie.get('cast'):
        cast = movie.get('cast')[:5]
    else:
        cast = [None]
    if movie.get('director'):
        directors = movie.get('director')[:4]
    else:
        directors = [None]
    if movie.get('runtime'):
        runtime = movie.get('runtime')
    else:
        runtime = None

    return rating, genre, plot, cast, directors, runtime


def IDgetter(title):
    mbd = IMDb()
    search_results = mbd.search_movie(title)
    if search_results:
        movie_ID = search_results[0].movieID
    else:
        return None
    return movie_ID


ProcessData('movies.json')
