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