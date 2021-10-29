from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class movie_actor(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class movies_movie(models.Model):

    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    poster_path = TextField()
    
    def __str__(self):
        return self.title

class movie_actor_movies(models.Model):
    actor_id = models.ForeignKey(movie_actor, on_delete=models.CASCADE) 
    movie_id = models.ForeignKey(movies_movie, on_delete=models.CASCADE)


class movies_review(models.Model):
    movie_id = models.ForeignKey(movies_movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
    
    def __str__(self):
        return self.title