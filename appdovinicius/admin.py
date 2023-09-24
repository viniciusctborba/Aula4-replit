from django.contrib import admin

from .models import Livros, Hobby, Pais

admin.site.register(Livros)
admin.site.register(Hobby)
admin.site.register(Pais)