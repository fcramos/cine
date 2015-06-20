# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='nome')),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'G\xeanero',
                'verbose_name_plural': 'G\xeaneros',
            },
            bases=(models.Model,),
        ),
    ]
