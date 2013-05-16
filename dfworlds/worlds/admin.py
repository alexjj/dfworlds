from django.contrib import admin
from world.models import World

class WorldAdmin(admin.ModelAdmin):
    

admin.site.register(World, WorldAdmin)
