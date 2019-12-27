from django.contrib import admin
from .models import SearchByActors,SearchByGenre,SearchByRating,SearchByDirectors,SearchByMovieName

# Register your models here.
admin.site.register([SearchByActors,SearchByGenre,SearchByRating,SearchByDirectors,SearchByMovieName])
# Register your models her
