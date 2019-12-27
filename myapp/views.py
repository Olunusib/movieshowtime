import requests
from django.shortcuts import render
import omdb
from omdbapi.movie_search import GetMovie
from dataclasses import dataclass
import requests
import sys, json
from .forms import MovieForm
from .findMovies import MoviesFinder
from . import models


# Create your views here.


def home(request):
    return render(request, 'index.html')


def results(request):
    finalposting = []
    finalMovies = []
    if request.method == 'POST':
        filled_form = MovieForm(request.POST)
        if filled_form.is_valid():
            genre = request.POST.get('choiceGenre')
            actors = request.POST.get('choiceActors')
            rating = request.POST.get('choiceRating')
            directors = request.POST.get('choiceDirectors')
            MovieName = request.POST.get('choiceMovieName')

            y = MoviesFinder()
            if len(MovieName) != 0:
                models.SearchByMovieName.objects.create(movieNames=MovieName)
                for movies in y.findByName(MovieName):
                    finalMovies.append(movies)

            if len(actors) != 0:
                models.SearchByActors.objects.create(actors=actors)
                for movies in y.findByActor(actors):
                    finalMovies.append(movies)
            if genre != ' ':
                models.SearchByGenre.objects.create(genre=genre)
                for movies in y.findByGenre(genre):
                    finalMovies.append(movies)

            if len(directors) != 0:
                models.SearchByDirectors.objects.create(directors=directors)
                for movies in y.findByDirector(directors):
                    finalMovies.append(movies)

            if len(rating) != 0:
                models.SearchByRating.objects.create(rating=rating)
                for movies in y.findByRating(rating):
                    finalMovies.append(movies)


            id = 0
            for movies in finalMovies:
                finalposting.append((id,y.getDetails(movies)))
                id+=1

            # finalMovies.append(((y.findByRating(rating)),(y.findByDirector(directors)),(y.findByActor(actors)),(y.findByGenre(genre)),(y.findByName(MovieName))))
            new_form = MovieForm()
            return render(request, 'myapp/results.html', {'MovieForm': new_form, 'finalposting': finalposting})
    else:
        form = MovieForm()
        return render(request, 'myapp/results.html', {'MovieForm': form})


def all(request):
    form = MovieForm()
    y = MoviesFinder()
    finalposting = []
    finalMovies = []
    rating = 0

    for movies in y.findByRating(rating):
        finalMovies.append(movies)
    id = 0
    for movies in finalMovies:
        finalposting.append((id,y.getDetails(movies)))
        id += 1

    return render(request, 'myapp/all.html', {'finalposting': finalposting})
