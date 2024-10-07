from django.db import models
from datetime import timedelta

# Create your models here.

class Movie(models.Model):
    MOVIE_GENRE = [
        ('DRAMA', 'Drama'),
        ('KORKU', 'Korku'),
        ('AKSİYON', 'Aksiyon'),
        ('GERİLİM', 'Gerilim'),
        ('SAVAŞ', 'Savaş'),
        ('BİLİM_KURGU', 'Bilim Kurgu'),
        ('ROMANTİK', 'Romantik'),
        ('KOMEDİ', 'Komedi'),
        ('GİZEM', 'Gizem'),
        ('MACERA', 'Macera'),
        ('AİLE', 'Aile')
    ]

    name = models.CharField(max_length=100, verbose_name='Film Adı')
    description = models.TextField(verbose_name='Film Açıklaması')
    image = models.CharField(max_length=50, verbose_name= 'Film Afişi')
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    isPublished = models.BooleanField(default=True)
    ımdbPoints = models.FloatField(default=0 ,verbose_name='IMDB Puanı')
    movieDuration = models.DurationField(default=timedelta(hours=0,seconds=0,milliseconds=0), verbose_name='Süre')
    movieYear = models.SmallIntegerField(default=0000, verbose_name='Yıl')
    movieBanner = models.ImageField(default='posters/default.jpg', upload_to='posters/')

    def __str__(self) -> str:
        return self.name

