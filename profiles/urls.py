from django.urls import path

from profiles.views import *
urlpatterns = [
path('profile/', ProfileViewSet.as_view({'get': 'list'}))

]