from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from places.serializers import *


class DistrictCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DistrictDetailSerializer


class DistrictsListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = DistrictsListSerializer
    queryset = Districts.objects.all()


class PlacesFilterListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = DistrictsFilterListSerializer

    def get_queryset(self):
        queryset = Place.objects.all()
        username = self.request.query_params.get('district_id')
        if username is not None:
            queryset = Place.objects.filter(district_id=username)
        return queryset


class DistrictDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DistrictsDetailView
    queryset = Districts.objects.all()


class ImageDetailView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ImageSerializer
    queryset = Place.objects.all()


class PlaceCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PlaceDetailSerializer


class PlaceListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PlaceListSerializer
    queryset = Place.objects.all()


class PlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PlaceDetailViewSerializer
    queryset = Place.objects.all()



