# Generated by Django 4.0.4 on 2023-03-04 10:12

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='Teksolutions/Articles/Images/default.png', max_length=255, verbose_name='Teksolutions/Articles/Images/')),
                ('headline', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('tags', models.CharField(max_length=200)),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
