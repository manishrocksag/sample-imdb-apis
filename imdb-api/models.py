from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews')
    title = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    created_by = models.ForeignKey(User)


class Movie(models.Model):
    """This class represents the movie model."""
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, blank=False)
    popularity = models.FloatField()
    director_name = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class GenreMapping(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    genre_id = models.ForeignKey('Genre')
    movie_id = models.ForeignKey('Movie')