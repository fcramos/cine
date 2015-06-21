# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from movies.models import Movie


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