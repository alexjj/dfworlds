from django.contrib import admin
from .models import World, Dfversion, Stonetype, Soil_type, Surface_water


class WorldAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['title', 'created_at']
    list_display_links = ['title']
    list_filter = ['author']
    search_fields = ['title', 'df_version']

admin.site.register(World, WorldAdmin)
admin.site.register(Dfversion)
admin.site.register(Stonetype)
admin.site.register(Surface_water)
admin.site.register(Soil_type)
