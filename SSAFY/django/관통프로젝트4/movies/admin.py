from django.contrib import admin
from .models import movie_actor, movies_movie, movies_review, movie_actor_movies
# Register your models here.

admin.site.register(movie_actor)
admin.site.register(movie_actor_movies)
admin.site.register(movies_movie)
admin.site.register(movies_review)
