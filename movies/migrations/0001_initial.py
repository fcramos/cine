# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='nome')),
                ('slug', models.SlugField()),
                ('photo', models.ImageField(upload_to=b'actors', verbose_name='foto')),
                ('country', models.CharField(max_length=200, verbose_name='pa\xeds')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
            bases=(models.Model,),
        ),
    ]
