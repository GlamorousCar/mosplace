import datetime

from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from places.models import Place
from profiles.serializers import *
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ProfileViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAdminUser | OwnProfilePermission,)
    # permission_classes = (OwnProfilePermission,)
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        user = self.request.query_params.get('id')
        return self.queryset.filter(user_id=user)

class ProfilePlacesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProfilePlacesSerializer
    queryset = ProfilePlaces.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        id = self.request.query_params.get('id')
        return self.queryset.filter(id=id)


class ProfilePlacesAddViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True)
    def add_place(self,request):
        profile_id = self.request.query_params.get('profile_id')
        place_id = self.request.query_params.get('place_id')
        status = 'OK'
        try:
            profile = Profile.objects.get(id=profile_id)
            place = Place.objects.get(id=place_id)
        except Profile.DoesNotExist:
            status = 'profile'
        except Place.DoesNotExist:
            status = 'Place.DoesNotExist'
        else:
            try:
                queryset = ProfilePlaces.objects.get(id=profile.visited_place.id)
                queryset.visited_places.add(place)
            except AttributeError:
                status = 'need to create'
                a1 = ProfilePlaces(date_of_visit=datetime.datetime.now())
                a1.save()
                a1.visited_places.add(place)
                a1.save()
                profile.visited_place = a1
                profile.save()
                # profile.visited_place.visited_places.add(place)
                status = 'all'
            except ProfilePlaces.DoesNotExist:
                status = 'profileplace'
        return Response({'status': status})


