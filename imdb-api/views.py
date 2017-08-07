from rest_framework import generics
from .models import Movie, Genre, GenreMapping
from .serializers import MovieSerializer, GenreSerializer


class MovieList(generics.ListCreateAPIView):
    # get the list of all the movies from movie table.
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'id'
    http_method_names = ['get']


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    # filter movie objects by id and perform operations on it.
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'id'
    http_method_names = ['get', 'post', 'put']


class GenreList(generics.ListCreateAPIView):
    # get the list of all the genres from the model.
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get']

