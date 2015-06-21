from django.shortcuts import render, get_object_or_404
from itertools import chain
from models import Movie


def home(request):
    if request.GET:
        movies = Movie.objects.all().order_by(request.GET['order'])
    else:
        movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)