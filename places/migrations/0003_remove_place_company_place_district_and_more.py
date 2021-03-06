# Generated by Django 4.0.2 on 2022-02-13 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_districts_title_alter_place_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='company',
        ),
        migrations.AddField(
            model_name='place',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='places.districts', verbose_name='Округ'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=64, unique=True, verbose_name='Название места'),
        ),
    ]
