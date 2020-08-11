from django_filters.rest_framework import DjangoFilterBackend

from .filters import TitleFilter
from .models import Title
from .serializers import TitleSerializer

from .models import Genre
from .serializers import GenreSerializer
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsAdminOrReadOnly

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    pagination_class = PageNumberPagination


class GenreViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                   mixins.DestroyModelMixin, viewsets.GenericViewSet):
    lookup_field = 'slug'
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    pagination_class = PageNumberPagination


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    serializer_class = TitleSerializer
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination
