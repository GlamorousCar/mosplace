from django.db import models


class Districts(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', filename])

    title = models.CharField(verbose_name='Округ',max_length=64, unique=True)
    abbreviation = models.CharField(verbose_name='Аббревиатура', max_length=10, default='')
    image = models.ImageField(upload_to=nameFile, default='')
    def __str__(self):
        return '%s' % (self.title)

class Place(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', filename])
    title = models.CharField(verbose_name='Название места', max_length=64,unique=True)
    district =  models.ForeignKey(Districts,verbose_name='Округ', on_delete = models.CASCADE)
    short_description = models.TextField(verbose_name='Краткое описание',default='')
    full_description = models.TextField(verbose_name='Полное писание',default='')
    PLACE_TYPE = (
        ('park','Парк'),
        ('unique_place','Особое место'),
        ('restaurant','Ресторан')
    )
    type = models.CharField(verbose_name='Тип места',max_length=30, choices=PLACE_TYPE)
class Gallery(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', filename])
    image = models.ImageField(upload_to=nameFile)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    def __str__(self):
        return self.image.name
