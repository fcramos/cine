# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='nome')),
                ('slug', models.SlugField()),
                ('synopsis', models.TextField(verbose_name='sinopse')),
                ('cover', models.ImageField(upload_to=b'covers', verbose_name='capa')),
                ('actors', models.ManyToManyField(to='movies.Actor', verbose_name='Atores')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='G\xeaneros')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
            bases=(models.Model,),
        ),
    ]
