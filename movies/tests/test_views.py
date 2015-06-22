# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from movies.models import Movie, Actor, Genre


class MovieListTest(TestCase):
    def setUp(self):
        self.movie = Movie
        self.names = ['Aaa', 'Bbb', 'Ccc', 'Ddd', 'Eee', 'Fff', 'Ggg', 'Hhh', 'Iii', 'Jjj']
        for name in self.names:
            self.movie.objects.create(
                name=name,
                synopsis='synopsis',
            )
        self.response = self.client.get(r('movies:home'))

    def test_get(self):
        'GET may result in 200.'
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        'Template may be index.html.'
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        'May have html elements'
        self.assertContains(self.response, '<li class="fl"', 8)
        self.assertContains(self.response, '<li class="fl last"', 2)


class MovieDetailTest(TestCase):
    def setUp(self):
        a1 = Actor.objects.create(
            name='Tom Cruise'
        )

        a2 = Actor.objects.create(
            name='Jack Chan'
        )

        g1 = Genre.objects.create(
            name='Action'
        )

        g2 = Genre.objects.create(
            name='Shot'
        )

        self.movie = Movie.objects.create(
            name='The movie',
            slug='the-movie',
            synopsis='Synopsis on the movie.'
        )
        self.movie.actors.add(a1)
        self.movie.actors.add(a2)
        self.movie.genres.add(g1)
        self.movie.genres.add(g2)

        self.movies = []
        for x in range(20):
            self.movies.append(
                Movie.objects.create(
                    name='Any movie',
                    synopsis='Any synopsis from movie.'
                )
            )
            if x % 2 == 0:
                self.movies[x].actors.add(a1)
            else:
                self.movies[x].actors.add(a2)

            if x % 3 == 0:
                self.movies[x].genres.add(g1)
            else:
                self.movies[x].genres.add(g2)

        self.response = self.client.get(r('movies:detail', args=[self.movie.slug]))

    def test_get(self):
        'GET /filme/1 may result in 200.'
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        'Template may be interna.html.'
        self.assertTemplateUsed(self.response, 'interna.html')

    def test_html(self):
        'Check is a movie data was rendered.'
        self.assertContains(self.response, 'The movie')
        self.assertContains(self.response, 'Synopsis on the movie')

    def test_related_movies(self):
        'May have ten related movies.'
        self.assertContains(self.response, '<li class="fl"', 8)
        self.assertContains(self.response, '<li class="fl last"', 2)


class GenreMovieListTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(
            name='Action',
            slug='action'
        )

        self.movies = []
        names = ['Aaa', 'Bbb', 'Ccc', 'Ddd', 'Eee', 'Fff', 'Ggg', 'Hhh', 'Iii', 'Jjj']
        for x, name in enumerate(names):
            self.movies.append(
                Movie.objects.create(
                    name=name,
                    synopsis='Any synopsis from movie.'
                )
            )

            if x % 2 == 0:
                self.movies[x].genres.add(self.genre)

        self.response = self.client.get(r('movies:genre', args=[self.genre.slug]))

    def test_get(self):
        'GET /genre/1 may result in 200.'
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        'Check is a genre movies data was rendered.'
        self.assertContains(self.response, 'Action')
        self.assertContains(self.response, '<li class="fl"', 4)
        self.assertContains(self.response, '<li class="fl last"', 1)

    def test_filter(self):
        'Filter may order movies in alphabetical order.'
        self.response = self.client.get(r('movies:genre', args=[self.genre.slug]), {'order': 'name'})
        movies = self.response.context['movies']
        self.assertEqual(movies[0], self.movies[0])
        self.assertEqual(movies[4], self.movies[8])

    def test_filter_inverse(self):
        'Filter may order movies in inverse alphabetical order.'
        self.response = self.client.get(r('movies:genre', args=[self.genre.slug]), {'order': '-name'})
        movies = self.response.context['movies']
        self.assertEqual(movies[0], self.movies[8])
        self.assertEqual(movies[4], self.movies[0])


class ActorPageTest(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(
            name='Tom Cruise',
            slug='tom-cruise',
            country='EUA'
        )

        self.movies = []
        for x in range(10):
            self.movies.append(
                Movie.objects.create(
                    name='Any movie',
                    synopsis='Any synopsis from movie.'
                )
            )
            self.movies[x].actors.add(self.actor)

        self.response = self.client.get(r('movies:actor', args=[self.actor.slug]))

    def test_get(self):
        'GET /genre/1 may result in 200.'
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        'Check is a Actor page was rendered.'
        self.assertContains(self.response, 'Tom Cruise')
        self.assertContains(self.response, 'EUA')
        self.assertContains(self.response, '<li class="fl"', 8)
        self.assertContains(self.response, '<li class="fl last"', 2)