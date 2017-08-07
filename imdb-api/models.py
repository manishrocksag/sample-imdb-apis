from __future__ import unicode_literals
from django.db import models


class Movie(models.Model):
    """This class represents the movie model."""
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, blank=False)
    popularity = models.FloatField()
    director = models.CharField(max_length=255, blank=False)
    imdb_score = models.FloatField()


class Genre(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, blank=False)


class GenreMapping(models.Model):
    """
    This table maps the relationship between movie and their genres.
    One movie can have many genres.
    """
    id = models.IntegerField(primary_key=True, auto_created=True)
    genre_id = models.ForeignKey('Genre')
    movie_id = models.ForeignKey('Movie')
