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
