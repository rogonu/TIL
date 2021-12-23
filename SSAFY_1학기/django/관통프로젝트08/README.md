B. Model

![](1.JPG)

![1](결과/1.PNG)

```python
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
```



C. URL

![1](결과/2.PNG)

```python
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # path('movie_1', views.movies_movie_1, name='movie_1'),
    # path('movie_2', views.movies_movie_2, name='movie_2'),
    # path('movie_3', views.movies_movie_3, name='movie_3'),

    path('actors/', views.actors_list),
    path('actors/<int:actors_pk>/', views.actors_detail),
    path('movies/', views.movies_list),
    path('movies/<int:movies_pk>/', views.movies_detail),
    path('reviews/', views.reviews_list),
    path('reviews/<int:reviews_pk>/', views.reviews_detail),
    path('movies/<int:movies_pk>/reviews/', views.reviews_create),
]
```



D. Admin

![1](결과/3.PNG)

```python
from django.contrib import admin
from .models import movie_actor, movie_actor_movies, movies_movie, movies_review
# Register your models here.

admin.site.register(movie_actor)
admin.site.register(movie_actor_movies)
admin.site.register(movies_movie)
admin.site.register(movies_review)
```



E. Serializer & View

![1](결과/4.PNG)

```python
from django.db.models import fields
from rest_framework import serializers
from .models import movie_actor, movies_movie, movies_review

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = movie_actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = movies_movie
        fields = ('title',)
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = movies_review
        fields = ('title',)

class ActorSerializer(serializers.ModelSerializer):
    class ActorMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = movie_actor
            fields = '__all__'
    actormovies = ActorMovieSerializer(many=True, read_only=True)

    class Meta:
        model = movies_movie
        fields = ('name','actormovies')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = movies_review
        fields = ('title',)

class MovieSerializer(serializers.ModelSerializer):
    
    review_set = ReviewSerializer(many=True, read_only=True)
    # review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = movies_movie
        fields = '__all__'
```

F. API test

![1](결과/pjt08_리뷰목록.PNG)

![1](결과/pjt08_리뷰상세정보.PNG)

![1](결과/pjt08_배우목록 불러오기.PNG)

![1](결과/pjt08_배우상세정보.PNG)

![1](결과/pjt08_영화목록.PNG)

![1](결과/pjt08_영화상세정보.PNG)



소감



최현준

* 페어로 진행한 장고 DB 프로젝트를 통해 혼자서 프로그래밍을 할 때는 빠르게 발견하지 못한 오타를 조기에 식별하고, 오류 발생시 같이 토의하여 문제를 해결하므로써 시간을 효율적으로 사용할 수 있었다. 페어 프로그램은 거듭할 수록 단점은 사라지고 장점이 더 부각되는 것이 느껴지며 앞으로도 많은 협업 경험을 통해 개발자들과 소통할 수 있는 역량을 갖추고 싶다.



노건우

* 처음 부터 끝까지 다 어려웠습니다. 항상 templates 를 이용해서 db를 관리했는데 rest api 형태로 관리 하려고 하니  처음부터 너무 헷갈리고 어떻게 해야 할지 감이 안잡혔습니다. 그래도 차근차근 할 수 있는 거 부터 따라 했는데 결국 모두 구현 하진 못했습니다. 그래도 함께 프로그래밍 하면서 서로 모르는 것이 있으면 의견을 나누면서 올바른 방향으로 진행할려고 노력했기 때문에 지금의 결과물이라도 나온 거 같습니다.

