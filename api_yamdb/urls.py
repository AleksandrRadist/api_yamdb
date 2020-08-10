from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('api/', include('api_comments_reviews.urls')),
    path('api/', include('api_titles.urls')),
    path('api/', include('api_categories.urls')),
    path('api/', include('api_genres.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api_users.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
