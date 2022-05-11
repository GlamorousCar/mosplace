from rest_framework.permissions import AllowAny

from reviews.serializers import *
from rest_framework import generics
from reviews.models import Comment
from rest_framework import viewsets


# Create your views here.


class CommentCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer


class CommentsListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentsViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Comment.objects.all()
        place_id = self.request.query_params.get('place_id')
        queryset = queryset.filter(place_id=place_id)
        return queryset

    serializer_class = CommentListSerializer
