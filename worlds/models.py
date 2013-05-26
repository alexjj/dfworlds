from django.db import models
from django.template.defaultfilters import slugify


class Dfversion(models.Model):
    version_number = models.CharField(max_length=255)

    def __unicode__(self):
        return self.version_number


class Stonetype(models.Model):
    stone_type = models.CharField(max_length=255)

    def __unicode__(self):
        return self.stone_type

class Surface_water(models.Model):
    surface_water = models.CharField(max_length=255)

    def __unicode__(self):
        return self.surface_water

class Soil_type(models.Model):
    soil_types = models.CharField(max_length=255)

    def __unicode__(self):
        return self.soil_types


class Metal(models.Model):
    metal = models.CharField(max_length=255)

    def __unicode__(self):
        return self.metal

class World(models.Model):
    NONE = 'NO'
    FLAT = 'FT'
    REGULAR = 'RG'

    VOLCANO = (
        (NONE, 'None'),
        (FLAT, 'Flat'),
        (REGULAR, 'Regular'),
    )

    CFLAT = 'CF'
    MFLAT = 'MF'
    HILL = 'HL'
    VALLEY = 'VY'
    CLIFF = 'FF'

    TERRAIN = (
        (CFLAT, 'Completely Flat'),
        (MFLAT, 'Mostly Flat'),
        (HILL, 'Hill/Mountain Side'),
        (VALLEY, 'Valley'),
        (CLIFF, 'Shear Cliff'),
    )

    SERENE = 'SR'
    MIRTHFUL = 'MR'
    JOYOUS = 'JW'
    CALM = 'CA'
    WILDERNESS = 'WS'
    UNTAMED = 'UW'
    SINISTER = 'ST'
    HAUNTED = 'HD'
    TERRIFY = 'TG'

    SURROUNDINGS = (
        (SERENE, 'Serene'),
        (MIRTHFUL, 'Mirthful'),
        (JOYOUS, 'Joyous Wilds'),
        (CALM, 'Calm'),
        (WILDERNESS, 'Wilderness'),
        (UNTAMED, 'Untamed Wilds'),
        (SINISTER, 'Sinister'),
        (HAUNTED, 'Haunted'),
        (TERRIFY, 'Terrifying'),
    )

    POCKET = 'PK'
    SMALLER = 'SR'
    SMALL = 'LL'
    MEDIUM = 'MD'
    LARGE = 'LG'

    WORLD_SIZE = (
        (POCKET, 'Pocket'),
        (SMALLER, 'Smaller'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    )

    SCORCH = 'SG'
    HOT = 'HT'
    WARM = 'WM'
    TEMPERATE = 'TP'
    COLD = 'CD'
    FREEZE = 'FZ'

    CLIMATE = (
        (SCORCH, 'Scorching'),
        (HOT, 'Hot'),
        (WARM, 'Warm'),
        (TEMPERATE, 'Temperate'),
        (COLD, 'Cold'),
        (FREEZE, 'Freezing'),
    )

    VSHORT = 'VS'
    SHORT = 'ST'
    MEDIUMH = 'MH'
    LONG = 'LG'
    VLONG = 'VL'

    HISTORY = (
        (VSHORT, '5 Years'),
        (SHORT, '125 Years'),
        (MEDIUMH, '250 Years'),
        (LONG, '550 Years'),
        (VLONG, '1050 Years'),
    )
    title = models.CharField(max_length=255, help_text='Name of your world')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    df_version = models.ForeignKey(Dfversion, default=4, help_text='Version it generates on')
    has_volcano = models.CharField(max_length=2, choices=VOLCANO)
    has_aquifer = models.BooleanField(default=False)
    has_water = models.ManyToManyField(Surface_water, default='None')
    embark_size = models.CharField(max_length=5, help_text='e.g. 3x3')
    embark_loc_img = models.URLField(default='', help_text='Screenshot of embark location. Try imgur.com for hosting')
    download_world = models.URLField(default='', blank=True, help_text='A link to the zip of the generated world (optional)')
    metals = models.ManyToManyField(Metal)
    has_candy = models.BooleanField(default=False)
    has_soil = models.ManyToManyField(Soil_type, default='None')
    history = models.CharField(max_length=2, choices=HISTORY)
    climate = models.CharField(max_length=2, choices=CLIMATE)
    world_size = models.CharField(max_length=2, choices=WORLD_SIZE)
    surroundings = models.CharField(max_length=2, choices=SURROUNDINGS)
    terrain = models.CharField(max_length=2, choices=TERRAIN)
    stone = models.ManyToManyField(Stonetype, default='None')
    world_description = models.TextField(default='', help_text='Tell us about your world, and any other details not captured.')
    world_gen = models.TextField(default='', help_text='The parameters to create this world')
    prospect = models.TextField(default='', help_text='Output of prospect hell using dfhack. No dfhack? Just say so.')
    slug = models.SlugField(max_length=255, blank=True, default='', editable=False)
    author = models.CharField(max_length=255, default='', help_text='Name of world creator')

    class Meta:
        ordering = ["-created_at"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(World, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('worlds:detail', (), {'slug':self.slug})
