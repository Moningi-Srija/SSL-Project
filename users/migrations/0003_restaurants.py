# Generated by Django 3.2.9 on 2022-11-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=500)),
                ('location', models.CharField(default='hyderabad', max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('rating', models.CharField(max_length=100)),
                ('lat', models.CharField(blank=True, max_length=20, null=True)),
                ('lon', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]