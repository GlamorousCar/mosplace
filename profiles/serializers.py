from rest_framework import serializers
from profiles.models import Profile
from profiles.models import ProfilePlaces


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfilePlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePlaces
        fields = ['visited_places']
