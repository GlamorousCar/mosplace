from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('places.urls')),
    path('api/v1/', include('profiles.urls')),
    path('api/v1/', include('reviews.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls')),
    path('authl/', include('project_auth.urls')),
]
