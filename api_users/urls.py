from django.urls import path, include

from .views import (
    UsersViewSet,
    get_current_user,
    signup,
    activate
)

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
    path('v1/auth/email/', signup, name='signup'),
    path('v1/auth/token/(?P<uidb64>[0-9A-Za-z_\-]+)/'
         '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         activate, name='activate'),
]
