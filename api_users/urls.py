from django.urls import path, include

from .views import UsersViewSet, EmailViewSet

from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('v1/users/me/', UsersViewSet.get_current_user)
    ]

router = DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns += [
    path('v1/', include(router.urls)),
    path('v1/auth/email/', EmailViewSet, name='email'),
]
