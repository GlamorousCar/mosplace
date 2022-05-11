from rest_framework import serializers
from reviews.models import Comment
from profiles.serializers import ProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
