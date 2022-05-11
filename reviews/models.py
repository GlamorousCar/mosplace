from django.db import models
from places.models import Place
from profiles.models import Profile
# Create your models here.
from django.utils import timezone
from django.core.validators import MaxValueValidator, \
    MinValueValidator


class Comment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(default=None, blank=True)
    stars = models.IntegerField(default=None, blank=True,
                                validators=[MaxValueValidator(5),
                                            MinValueValidator(0)])

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_date']

    def __str__(self):
        return self.text[:50]
