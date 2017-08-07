from django.contrib import admin
from .models import Movie, Genre, GenreMapping

"""
Register movie, genre, genre models with the admin page giving him
the rights to perform CRUD operations on them.
"""
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(GenreMapping)