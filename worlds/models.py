from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Dfversion(models.Model):
    version_number = models.CharField()

class World(models.Model):
    DF_VERSION = (
        ('v34', '34.11'),
        ('v31', '31.25'),
        ('40d', '40d'),
        ('v23', '23a'),
    )
    HAS_RIVER = (
        ('River', 'River'),
        ('Brook', 'Brook'),
        ('None', 'None'),
    )
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    df_version = models.ForeignKey('Dfversion')
    #df_version = models.CharField(max_length=3, choices=DF_VERSION)
    has_volcano = models.BooleanField(default=False)
    has_aquifer = models.BooleanField(default=False)
    has_river = models.CharField(max_length=5, choices=HAS_RIVER)
    embark_size = models.CharField(max_length=5)
    embark_loc_img = models.URLField(default='')
    has_iron = models.BooleanField(default=False)
    has_candy = models.BooleanField(default=False)
    worldgen = models.TextField(default='')
    prospect = models.TextField(default='')
    slug = models.SlugField(max_length=255, blank=True, default='', editable=False)
    author = models.CharField(max_length=255, default='')
    published = models.BooleanField(default=True, editable=False)

    class Meta:
        ordering = ["-created_at", "df_version"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(World, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('worlds:detail', (), {'slug':self.slug})
