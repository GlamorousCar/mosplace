from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets
from places.serializers import *
from places.models import Districts
from django.http.multipartparser import MultiPartParser
from rest_framework.parsers import MultiPartParser, FormParser

class DistrictCreateView(generics.CreateAPIView):
    serializer_class = DistrictDetailSerializer
class DistrictsListView(generics.ListAPIView):
    serializer_class = DistrictsListSerializer
    queryset = Districts.objects.all()
class DistrictsFilterListView(generics.ListAPIView):
    serializer_class = DistrictsFilterListSerializer
    def get_queryset(self):
        queryset = Place.objects.all()
        username = self.request.query_params.get('district_id')
        if username is not None:
            queryset = Place.objects.filter(district_id=username)
        return queryset
class DistrictDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DistrictsDetailView
    queryset = Districts.objects.all()

class ImageDetailView(generics.CreateAPIView):
    serializer_class = ImageSerializer
    queryset = Place.objects.all()
class PlaceCreateView(generics.CreateAPIView):
    serializer_class = PlaceDetailSerializer
class PlaceListView(generics.ListAPIView):
    serializer_class = PlaceListSerializer
    queryset = Place.objects.all()
class PlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceDetailView
    queryset = Place.objects.all()
