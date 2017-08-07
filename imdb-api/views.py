from rest_framework import generics
from .models import Movie, Genre, GenreMapping
from .serializers import MovieSerializer, GenreSerializer


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'id'
    http_method_names = ['get']


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'id'
    http_method_names = ['get', 'post', 'put']


class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get']

