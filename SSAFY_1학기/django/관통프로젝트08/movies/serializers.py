from django.db.models import fields
from rest_framework import serializers
from .models import movie_actor, movies_movie, movies_review

# class MoviesactorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = movie_actor
#         fields = '__all__'

# class MoviesmovieSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = movies_movie
#         fields = '__all__'

# class MoviesreviewSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = movies_review
        # fields = '__all__'
# 
# 
# 
# 
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
            model = movies_movie
            fields = ('title',)
    actormovies = ActorMovieSerializer(many=True, read_only=True)

    class Meta:
        model = movie_actor
        fields = ('name','actormovies',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = movies_review
        fields = '__all__'




class MovieSerializer(serializers.ModelSerializer):
    
    review_set = ReviewSerializer(many=True, read_only=True)
    # review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = movies_movie
        fields = '__all__'
