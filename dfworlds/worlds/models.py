from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class World(models.Model):
    DF_VERSION = (
        ('v34', '34.11'),
        ('v31', '31.25'),
        ('40d', '40d'),
        ('v23', '23a'),
    )
    HAS_RIVER = (
        ('river', 'River'),
        ('brook', 'Brook'),
        ('none', 'None'),
    )
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    df_version = models.CharField(max_length=3, choices=DF_VERSION)
    has_volcano = models.BooleanField()
    has_aquifer = models.BooleanField()
    has_river = models.CharField(max_length=5, choices=HAS_RIVER)
    embark_size = models.CharField(max_length=5)
    embark_loc_img = URLField(max_length=255)
    has_iron = models.BooleanField()
    has_candy = models.BooleanField()
    worldgen = models.TextField()
    prospect = models.TextField()
    slug = models.SlugField(max_length=255, blank=True, default='')
    author = models.ForeignKey(User, related_name="worlds")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "df_version", "embark_size", "prospect"]

    class Meta:
        ordering = ["-created_at", "df_version"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(World, self).save(*args, **kwargs)
