from django.contrib import admin
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'createdDate', 'isPublished')
    list_display_links = ('name',)
    list_filter = ('createdDate',)
    list_editable = ('isPublished',)
    search_fields = ('name', 'description')

admin.site.register(Movie, MovieAdmin)