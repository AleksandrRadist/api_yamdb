from django.db import models

from api_categories.models import Category
from api_genres.models import Genre


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='categories')
    genre = models.ManyToManyField(Genre, related_name='genres')
