from django.contrib import admin
from .models import World, Dfversion


class WorldAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['published', 'title', 'created_at']
    list_display_links = ['title']
    list_editable = ['published']
    list_filter = ['published', 'author']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'df_version']

admin.site.register(World, WorldAdmin, Dfversion)
