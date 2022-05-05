# Create your models here.
from django.db import models
from django.conf import settings
from places.models import Place


class ProfilePlaces(models.Model):
    visited_places = models.ManyToManyField(Place,
                                            verbose_name='Посещенные места',
                                            blank=True)
    date_of_visit = models.DateTimeField('date of visit',
                                         auto_now_add=True)

    class Meta:
        verbose_name = 'Посещенные места профиля'
        verbose_name_plural = 'Посещенные места профиля'


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    name = models.CharField("name", max_length=500,
                            default='default.')
    image = models.ImageField(default='default.png')
    visited_place = models.OneToOneField(ProfilePlaces,
                                         on_delete=models.CASCADE,
                                         blank=True, null=True)

    def __str__(self):
        return f"{self.name} "

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
