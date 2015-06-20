# coding: utf-8
from django.test import TestCase
from .models import Actor, Genre


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