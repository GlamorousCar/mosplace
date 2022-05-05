from django.urls import path

from profiles.views import *

urlpatterns = [
    path('profile/', ProfileViewSet.as_view({'get': 'list'})),
    path('profile_places/',
         ProfilePlacesViewSet.as_view({'get': 'list'})),
    path('add_place_to_profile/',
         ProfilePlacesAddViewSet.as_view({'post': 'add_place'})),
]
