# Create your models here.
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    name = models.CharField("name", max_length=500)
    image = models.ImageField(default='default.png')

    def __str__(self):
        return f"{self.name} "
