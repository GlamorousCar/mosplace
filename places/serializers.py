from rest_framework import serializers
from places.models import Districts,Place,Gallery
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
        fields = ('id','title',)
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
class PlaceDetailView(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
