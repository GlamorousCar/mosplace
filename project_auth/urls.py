from django.urls import path
from django.urls import include, re_path
from project_auth.views import ActivateUser

app_name = 'auth'
urlpatterns = [
    path('accounts/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),

]
