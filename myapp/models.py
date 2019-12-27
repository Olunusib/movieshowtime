from djongo import models
from django import forms


# Create your models here.
class SearchByActors(models.Model):
    actors = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.actors)

    class Meta:
        verbose_name_plural = 'Searches By Actors'

class SearchByGenre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.genre)

    class Meta:
        verbose_name_plural = 'Searches By Genres'

class SearchByMovieName(models.Model):
    movieNames = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.movieNames)

    class Meta:
        verbose_name_plural = 'Searches By Movie Names'

class SearchByRating(models.Model):
    rating = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.rating)

    class Meta:
        verbose_name_plural = 'Searches By Rating'

class SearchByDirectors(models.Model):
    directors = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.directors)

    class Meta:
        verbose_name_plural = 'Searches By Directors'


