from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewsSet,
                    GenreViewSet, ReviewViewsSet,
                    TitleViewSet)

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet, basename='title')
router.register(r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewsSet, basename='review')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewsSet, basename='comment')

urlpatterns = [
    path('v1/', include(router.urls)),
]
