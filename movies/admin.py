from django.contrib import admin
from .models import Actor


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', )
    search_fields = ('name', )
    list_filter = ['name', 'country']
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Actor, ActorAdmin)