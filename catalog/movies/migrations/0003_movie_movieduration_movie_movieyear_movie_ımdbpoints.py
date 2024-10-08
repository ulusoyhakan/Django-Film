# Generated by Django 5.1.1 on 2024-09-30 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_ispublished_alter_movie_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movieDuration',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='Süre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='movieYear',
            field=models.SmallIntegerField(default=0, verbose_name='Yıl'),
        ),
        migrations.AddField(
            model_name='movie',
            name='ımdbPoints',
            field=models.SmallIntegerField(default=0, verbose_name='IMDB Puanı'),
        ),
    ]
