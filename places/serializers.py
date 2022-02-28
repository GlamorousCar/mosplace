from rest_framework import serializers
from places.models import Districts, Place, Gallery
from django.contrib.auth.models import User


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class DistrictDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'


class DistrictsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'


class DistrictsFilterListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = '__all__'


class DistrictsDetailView(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'


class PlaceDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = '__all__'


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    images = ImageSerializer(many=True, read_only=True)


class PlaceDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Districts.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']
