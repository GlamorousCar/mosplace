# Generated by Django 4.0.2 on 2022-02-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_place_short_description_alter_place_full_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='districts',
            name='abbreviation',
            field=models.CharField(default='', max_length=10, verbose_name='Аббревиатура'),
        ),
    ]
