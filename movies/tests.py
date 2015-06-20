# coding: utf-8
from django.test import TestCase
from .models import Actor, Genre, Movie


class ActorTest(TestCase):
    def setUp(self):
        self.actor = Actor(
            name='Fulano',
            country='Brasil',
        )
        self.actor.save()

    def test_create(self):
        'Actor instance may be saved'
        self.assertEqual(1, self.actor.pk)

    def test_unicode(self):
        'Actor string representation may be the name.'
        self.assertEqual(u'Fulano', unicode(self.actor))


class GenreTest(TestCase):
    def setUp(self):
        self.genre = Genre(
            name='Action'
        )
        self.genre.save()

    def test_create(self):
        'Genre instance may be saved'
        self.assertEqual(1, self.genre.pk)

    def test_unicode(self):
        'Genre string representation may be the name.'
        self.assertEqual(u'Action', unicode(self.genre))


class MovieTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            name='007',
            synopsis='Lorem ypsum',
        )

    def test_create(self):
        self.assertEqual(1, self.movie.pk)

    def test_unicode(self):
        self.assertEqual('007', unicode(self.movie))

    def test_actors(self):
        'Movie has many actors'
        self.movie.actors.create(
            name='Daniel Craig',
            country='England'
        )
        self.assertEqual(1, self.movie.actors.count())

    def test_genres(self):
        'Movie has many genres'
        self.movie.genres.create(
            name='Espionage',
        )
        self.assertEqual(1, self.movie.genres.count())