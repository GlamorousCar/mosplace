from rest_framework import serializers
from profiles.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Districts.objects.all())

    class Meta:
        model = Profile
        fields = ['id', 'name','image']

