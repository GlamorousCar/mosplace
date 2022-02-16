from django.contrib import admin
from django.urls import path,re_path, include
from places.views import *

app_name = 'places'
urlpatterns = [
    path('district/',DistrictCreateView.as_view()),
    path('districts/', DistrictsListView.as_view()),
    re_path('^district/(?P<username>.+)/$', DistrictsFilterListView.as_view()),
    path('district_edit/<int:pk>', DistrictDetailView.as_view()),
    path('place/',PlaceCreateView.as_view()),
    path('places/', PlaceListView.as_view()),
    path('place/<int:pk>', PlaceDetailView.as_view()),
    path('img', ImageDetailView.as_view())

]
