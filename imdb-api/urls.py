from django.conf.urls import url
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='IMDB Movie APIs')

"""
/admin ~ reference to the admin site page where CRUD operations 
    can be performed on models.
    
/movie ~ Returns the list of all the movies.

/movie?id={0} ~ Returns the movie with the given id

/genre ~ Returns the list of all the genres.

# todo 

/movie/{id}?genre={name} ~ Returns the genre list of the given movie.

/movie/{id}?director={name} ~ Returns the director name of the given movie.

/movie/popularity?score={number} ~ Returns the list of the movies which has a popularity
    greater than or equal to the given score.
    
/movie/rating?rating={number} ~ Returns the list of the movies which has a ratings
    greater than or equal to the given score.

movie/genre?{name} ~ Returns the movie list which belongs to the given genre.    

# todo adding permission and authentication.
"""

urlpatterns = [
    url(r'^$', schema_view, name="schema_view"),
    url(
        r'^movies$',
        views.MovieList.as_view(), name='movie-list'
    ),
    url(r'^movies/(?P<id>[0-9]+)/$', views.MovieDetail.as_view()),
    url(
        r'^genres$',
        views.GenreList.as_view()
    )
]
