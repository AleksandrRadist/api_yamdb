from rest_framework import serializers

from content.models import (Category, Comment, Genre,
                            Review, Title)

# Category, Genre and Title serializers 

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


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
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'

# Comments and Reviews serializers


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('id', 'pub_date')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    score = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('id', 'score', 'pub_date')

    def validate_score(self, value):
        if not 1 <= value <= 10:
            raise serializers.ValidationError(
                'Value of score field is out of range from 1 to 10')
        return value

    def validate(self, data):
        title_id = self.context.get('view').kwargs.get('title_id')
        user = self.context.get('request').user

        if self.context.get('request').method == 'POST':
            if ((not Title.objects.filter(id=title_id).exists()) or
                    not bool(data)):
                return serializers.ValidationError

            if Review.objects.filter(author=user, title__id=title_id).exists():
                raise serializers.ValidationError
        return data
