# Generated by Django 4.0.2 on 2022-02-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districts',
            name='title',
            field=models.CharField(max_length=64, unique=True, verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=64, unique=True, verbose_name='Округ'),
        ),
    ]
