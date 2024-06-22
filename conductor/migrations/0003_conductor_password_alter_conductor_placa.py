# Generated by Django 5.0.6 on 2024-06-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conductor', '0002_alter_conductor_options_conductor_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='  Password'),
        ),
        migrations.AlterField(
            model_name='conductor',
            name='placa',
            field=models.CharField(default='', max_length=6, unique=True, verbose_name='Placa'),
        ),
    ]
