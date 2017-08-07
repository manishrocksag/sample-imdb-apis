from django.conf.urls import url
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='IMDB Movie APIs')

urlpatterns = [
    url(r'^$', schema_view, name="schema_view"),
    url(
        r'^movies$',
        views.MovieList.as_view()
    ),
    url(
        r'^genres$',
        views.GenreList.as_view()
    ),
]
