from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .filters import TitleFilter
from .models import Title
from .permissions import IsAdminOrReadOnly
from .serializers import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    serializer_class = TitleSerializer
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination
