from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from places.permissions import OwnProfilePermission
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


class ProfileViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAdminUser | OwnProfilePermission,)
    permission_classes = [AllowAny]
    # permission_classes = (OwnProfilePermission,)
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        user = self.request.query_params.get('id')
        return self.queryset.filter(user_id=user)
        # return self.queryset
    # def get_queryset(self,request):
    #     user = self.request.query_params.get('id')
    #
    #     return self.queryset.filter(id=user)
