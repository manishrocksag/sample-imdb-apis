from .models import Product, Review, Movie, Genre
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Review
        fields = ('id', 'title', 'review', 'rating', 'created_by')


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'reviews')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'popularity', 'director_name')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name')


