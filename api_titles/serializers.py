from rest_framework import serializers

from api_categories.models import Category
from api_categories.serializers import CategorySerializer
from api_genres.models import Genre
from api_genres.serializers import GenreSerializer

from .models import Title


class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = CategorySerializer(value)
        return serializer.data


class GenreField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = GenreSerializer(value)
        return serializer.data


class TitleSerializer(serializers.ModelSerializer):
    category = CategoryField(slug_field='slug',
                             queryset=Category.objects.all(),
                             required=False)
    genre = GenreField(slug_field='slug',
                       queryset=Genre.objects.all(),
                       required=False,
                       many=True)

    class Meta:
        model = Title
        fields = '__all__'
