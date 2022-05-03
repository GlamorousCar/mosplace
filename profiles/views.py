from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from profiles.models import Profile
from profiles.serializers import ProfileSerializer


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