# Generated by Django 5.1.1 on 2024-09-30 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_movieduration_movie_movieyear_movie_ımdbpoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='ımdbPoints',
            field=models.FloatField(default=0, verbose_name='IMDB Puanı'),
        ),
    ]
