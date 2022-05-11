from reviews.views import *
from django.urls import path

urlpatterns = [
    path('comment_add', CommentCreateView.as_view()),
    path('comment_by_article_id',
         CommentsViewSet.as_view({'get': 'list'})),

]
