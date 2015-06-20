# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Actor(models.Model):
    """
    The purpose of this model is manage actors
    """
    name = models.CharField(_('nome'), max_length=200, )
    slug = models.SlugField()
    photo = models.ImageField(_('foto'), upload_to='actors', )
    country = models.CharField(_(u'país'), max_length=200, )

    class Meta:
        ordering = ['name']
        verbose_name = _('Ator')
        verbose_name_plural = _('Atores')

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    """
    The purpose of this model is manage movie genres
    """
    name = models.CharField(_('nome'), max_length=200, )
    slug = models.SlugField()

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Gênero')
        verbose_name_plural = _(u'Gêneros')

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    """
    The purpose of this model is manage movies
    """
    name = models.CharField(_('nome'), max_length=200, )
    slug = models.SlugField()
    synopsis = models.TextField(_('sinopse'), )
    genres = models.ManyToManyField('Genre', verbose_name=_(u'Gêneros'), )
    actors = models.ManyToManyField('Actor', verbose_name=_('Atores'), )
    cover = models.ImageField(_('capa'), upload_to='covers', )

    class Meta:
        ordering = ['name']
        verbose_name = _('Filme')
        verbose_name_plural = _('Filmes')

    def __unicode__(self):
        return self.name