from django.contrib import admin
from .models import World


class WorldAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['title', 'created_at']
    list_display_links = ['title']
    list_filter = ['author']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'df_version']

admin.site.register(World, WorldAdmin)