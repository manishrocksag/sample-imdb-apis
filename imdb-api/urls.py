from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from . import views

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='Movies API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r'^', schema_view, name="docs"),
    url(r'^products/$', views.ProductList.as_view(), name='product-list'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.ProductDetail.as_view()),
    url(
        r'^products/(?P<product_id>[0-9]+)/reviews/$',
        views.ReviewList.as_view()
    ),
    url(
        r'^products/(?P<product_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/$',
        views.ReviewDetail.as_view()
    ),
    url(
        r'^movies/$',
        views.MovieList.as_view()
    ),
    url(
        r'^genres/$',
        views.GenreList.as_view()
    ),
]