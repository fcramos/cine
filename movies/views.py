from django.shortcuts import render, get_object_or_404
from itertools import chain
from models import Movie, Genre, Actor


def home(request):
    if request.GET:
        movies = Movie.objects.all().order_by(request.GET['order'])
    else:
        movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)


def detail(request, slug):
    # Getting requested movie
    movie = get_object_or_404(Movie, slug=slug)

    # Getting actors from current movie
    actors = movie.actors.values_list('pk', flat=True)
    # Getting genres from current movie
    genres = movie.genres.values_list('pk', flat=True)

    # Getting movies with same actors and genres from current movie
    mixed_movies = Movie.objects.filter(genres__in=genres, actors__in=actors).exclude(slug=slug).distinct().order_by()[:10]

    # If possible, may have ten results
    if mixed_movies.count() < 10:
        # Getting movies with same actors from current movie
        actors_movies = Movie.objects.filter(actors__in=actors).distinct().exclude(slug=slug)\
            .exclude(pk__in=mixed_movies.values_list('pk', flat=True))

        # Getting movies with same genres from current movie
        genres_movies = Movie.objects.filter(actors__in=actors).distinct().exclude(slug=slug)\
            .exclude(pk__in=mixed_movies.values_list('pk', flat=True))\
            .exclude(pk__in=actors_movies.values_list('pk', flat=True))

        # Joining results
        related_movies = chain(mixed_movies[:5], actors_movies[:3], genres_movies[:2])
    else:
        related_movies = mixed_movies

    context = {
        'movie': movie,
        'movies': related_movies
    }
    return render(request, 'interna.html', context)


def genre(request, slug):
    this_genre = Genre.objects.get(slug=slug)
    movies = Movie.objects.filter(genres=this_genre.pk)
    if request.GET:
        movies = movies.order_by(request.GET['order'])

    context = {
        'genre': this_genre,
        'movies': movies
    }
    return render(request, 'genero.html', context)


def actor(request, slug):
    this_actor = Actor.objects.get(slug=slug)
    movies = Movie.objects.filter(actors=this_actor.pk)

    context = {
        'actor': this_actor,
        'movies': movies
    }
    return render(request, 'artista.html', context)