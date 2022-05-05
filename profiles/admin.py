# Register your models here.
from django.contrib import admin

from profiles.models import *

admin.site.register(Profile)
admin.site.register(ProfilePlaces)
