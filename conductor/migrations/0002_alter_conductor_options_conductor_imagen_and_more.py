# Generated by Django 5.0.6 on 2024-06-14 21:23

import conductor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conductor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conductor',
            options={'verbose_name_plural': 'Conductores'},
        ),
        migrations.AddField(
            model_name='conductor',
            name='imagen',
            field=models.ImageField(blank=True, default='comunidad\\default-user.jpeg', null=True, upload_to=conductor.models.get_image_filename),
        ),
        migrations.AddField(
            model_name='conductor',
            name='modelo',
            field=models.PositiveIntegerField(default=0, verbose_name='Modelo'),
        ),
        migrations.AddField(
            model_name='conductor',
            name='moto_nombre',
            field=models.CharField(default='', max_length=50, verbose_name='Moto'),
        ),
        migrations.AddField(
            model_name='conductor',
            name='placa',
            field=models.CharField(default=False, max_length=6, unique=True, verbose_name='Placa'),
        ),
    ]