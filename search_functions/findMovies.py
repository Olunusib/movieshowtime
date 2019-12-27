import json
import sys

# testing set for methods
def testing():

    finder = MoviesFinder('moviesDict.json')
    
    print("by rating:\n")
    print(finder.findByRating(7))
    print('\n')
    print("by genre:\n")
    print(finder.findByGenre(['action','Fantasy']))
    print('\n')
    print("by director:\n")
    print(finder.findByDirector('J.J. Abrams'))
    print('\n')
    print("by actor:\n")
    print(finder.findByActor('Adam Driver'))
    print('\n')
    print('all movies:\n')
    print(finder.showAll())



class MoviesFinder():

    def __init__(self, filepath):
        with open(filepath) as movies:
            moviesDict = json.load(movies)
        self.moviesDict = moviesDict

    def showAll(self):
        movies = []
        for title in self.moviesDict.keys():
            movies.append(title)
        return movies

    def findByRating(self, rating):
        matchedMovies = []
        for title, metaData in self.moviesDict.items():
            if metaData['rating']:   
                if metaData['rating'] >= rating:
                    matchedMovies.append(title)
        return matchedMovies
    # takes a list of genres as argument 
    def findByGenre(self,genres):
        if type(genres) != list:
            list(genres)
        genres = [genre.casefold() for genre in genres]
        matchedMovies = []
        for title, metaData in self.moviesDict.items():
            if metaData['genre']:
                titleGenres = [genre.casefold() for genre in metaData['genre']]
                for genre in titleGenres:
                    if genre in genres:
                        matchedMovies.append(title)
        return matchedMovies

    # takes name(s) of director(s) as a list as argument  
    def findByDirector(self,directors):
        if type(directors) != list:
            directors = [directors]
        directors = [director.casefold() for director in directors]
        matchedMovies = []
        for title, metaData in self.moviesDict.items():
            movieDirectors = [director.casefold() for director in metaData['directors'] if metaData['directors'][0] != 'None']
            for director in movieDirectors:
                if director.casefold() in directors:
                    matchedMovies.append(title)
        return matchedMovies

    # takes name(s) of actor(s) as a list as argument
    def findByActor(self, actors):
        if type(actors) != list:
            actors = [actors]
        actors = [actor.casefold() for actor in actors]
        matchedMovies = []
        for title, metaData in self.moviesDict.items():
            cast = [actor.casefold() for actor in metaData['cast'] if metaData['cast'][0] != 'None']
            for actor in cast:
                if actor.casefold() in actors:
                    matchedMovies.append(title)
        return matchedMovies



# running the test
testing()



# make a loop asking for user input how he wants to find movie suggestion from the given methoods


