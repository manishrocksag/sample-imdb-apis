from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from . import views

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='Movies API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r'^', schema_view, name="docs"),
    url(
        r'^movies/$',
        views.MovieList.as_view()
    ),
    url(
        r'^genres/$',
        views.GenreList.as_view()
    ),
]
