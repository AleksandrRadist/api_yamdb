from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from django.db.models import Avg
from django.shortcuts import get_object_or_404

from .filters import TitleFilter
from .permissions import IsAdminOrReadOnly, IsAuthorOrStaff
from .serializers import (CategorySerializer, 
                        CommentSerializer, GenreSerializer,
                        ReviewSerializer, TitleSerializer)
from content.models import (Category, Comment, Genre,
                            Review, Title)


class CategoryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                      mixins.DestroyModelMixin, GenericViewSet):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    pagination_class = PageNumberPagination


class GenreViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                   mixins.DestroyModelMixin, GenericViewSet):
    lookup_field = 'slug'
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    pagination_class = PageNumberPagination


class TitleViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    serializer_class = TitleSerializer
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination

    def get_queryset(self):
        titles = Title.objects.annotate(rating=Avg('reviews__score'))
        return titles

class ReviewViewsSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthorOrStaff,
        IsAuthenticatedOrReadOnly
    )

    def get_title(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())

    def get_queryset(self):
        title = self.get_title()
        return title.reviews.all()


class CommentViewsSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthorOrStaff,
        IsAuthenticatedOrReadOnly
    )

    def get_review(self):
        review_id = self.kwargs.get('review_id')
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Review, pk=review_id, title__id=title_id)

    def perform_create(self, serializer):
        review = self.get_review()
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = self.get_review()
        return review.comments.all()

