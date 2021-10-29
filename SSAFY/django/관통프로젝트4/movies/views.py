from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render, get_list_or_404, get_object_or_404

from .serializers import ActorListSerializer, MovieListSerializer, ReviewListSerializer, ActorSerializer, ReviewSerializer, MovieSerializer
from .models import movie_actor, movies_movie, movies_review
from movies import serializers


@api_view(['GET', 'POST'])
def actors_list(request):
    if request.method == 'GET':
        actors = get_list_or_404(movie_actor)
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def actors_detail(request, actors_pk):
    
    actor = get_object_or_404(movie_actor, pk=(actors_pk))

    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        actor.delete()
        data = {
            'delete': f'데이터 {actors_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(movies_movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def movies_detail(request, movies_pk):
    
    movie = get_object_or_404(movies_movie, pk=movies_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        movie.delete()
        data = {
            'delete': f'데이터 {movies_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@api_view(['GET'])
def reviews_list(request):
    reviews = get_list_or_404(movies_review)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def reviews_detail(request, reviews_pk):
    
    review = get_object_or_404(movies_review, pk=reviews_pk)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'message': f'댓글 {reviews_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def reviews_create(request, movies_pk):
    movie = get_object_or_404(movies_movie, pk=movies_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

