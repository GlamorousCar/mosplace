# Generated by Django 4.0.2 on 2022-02-15 09:26

from django.db import migrations, models
import places.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_remove_place_company_place_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(null=True, upload_to=places.models.Place.nameFile),
        ),
    ]
