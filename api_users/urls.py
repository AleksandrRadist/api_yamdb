from django.urls import path, include

from .views import UsersViewSet, get_current_user

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )


urlpatterns = [
    path('v1/users/me/', get_current_user),
    ]

router = DefaultRouter()
router.register(r'users', UsersViewSet)


urlpatterns += [
    path('v1/', include(router.urls)),
    path(
        'v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

]
