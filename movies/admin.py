from django.contrib import admin
from .models import Actor, Genre, Movie


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', )
    search_fields = ('name', )
    list_filter = ['name', 'country']
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Actor, ActorAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ['name', ]
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'genre', 'actors', )
    list_filter = ['name', 'actors', ]
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Movie, MovieAdmin)
