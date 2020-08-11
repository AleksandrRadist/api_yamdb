from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TitleViewSet

from .views import GenreViewSet

from .views import CategoryViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(router.urls)),
    path('v1/', include(router.urls)),
]