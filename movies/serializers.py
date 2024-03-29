from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'creator')



class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')


class MovieTitleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Movie
        fields = ('id', 'title')



class MovieIdSerializer(serializers.ModelSerializer):
     class Meta:
        model = Movie
        fields = '__all__'


class MovieGenreSerializer(serializers.ModelSerializer):
     class Meta:
        model = Movie
        fields = ('genre')


class MovieGenreSerializer(serializers.ModelSerializer):
     class Meta:
        model = Movie
        fields = ('genre')