# Generated by Django 4.0.3 on 2022-11-23 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_movie_remove_hotel_lat_remove_hotel_lon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
    ]
