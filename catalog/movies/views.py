from django.shortcuts import render
from .models import Movie
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/movies_list.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    context = {
        'movieDetail': movie
    }
    return render(request, 'movies/detail.html', context)

def search(request):
    return render(request, 'movies/search.html')