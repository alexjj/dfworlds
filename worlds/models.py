from django.db import models
from django.template.defaultfilters import slugify


class Dfversion(models.Model):
    version_number = models.CharField(max_length=255)

    def __unicode__(self):
        return self.version_number

class World(models.Model):
    NONE = 'NO'
    RIVER = 'RV'
    BROOK = 'BK'
    OCEAN = 'OC'
    LAKE = 'LK'
    PONDS = 'PD'
    WATERFALL = 'WF'

    WATER = (
        (NONE, 'None'),
        (RIVER, 'River'),
        (BROOK, 'Brook'),
        (OCEAN, 'Ocean'),
        (LAKE, 'Lake'),
        (PONDS, 'Ponds'),
        (WATERFALL, 'Waterfall')
    )

    FLAT = 'FT'
    REGULAR = 'RG'

    VOLCANO = (
        (NONE, 'None'),
        (FLAT, 'Flat'),
        (REGULAR, 'Regular'),
    )

    FLUX = 'FX'
    OBSIDIAN = 'OB'
    MAGMASAFE = 'MS'

    STONE = (
        (FLUX, 'Flux'),
        (OBSIDIAN, 'Obsidian'),
        (MAGMASAFE, 'Magma-Safe'),
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

    POCKET = 17
    SMALLER = 33
    SMALL = 65
    MEDIUM = 129
    LARGE = 257

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

    SAND = 'SD'
    SOIL = 'SL'
    CLAY = 'CY'

    HAS_SOIL = (
        (NONE, 'None'),
        (SAND, 'Sand'),
        (SOIL, 'Soil'),
        (CLAY, 'Clay'),
    )

    VSHORT = 5
    SHORT = 125
    MEDIUMH = 250
    LONG = 550
    VLONG = 1050

    HISTORY = (
        (VSHORT, 'Very Short'),
        (SHORT, 'Short'),
        (MEDIUMH, 'Medium'),
        (LONG, 'Long'),
        (VLONG, 'Very Long'),
    )
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    df_version = models.ForeignKey('Dfversion', default='0.34.11')
    has_volcano = models.CharField(max_length=2, choices=VOLCANO)
    has_aquifer = models.BooleanField(default=False)
    has_water = models.CharField(max_length=2, choices=WATER)
    embark_size = models.CharField(max_length=5)
    embark_loc_img = models.URLField(default='')
    download_word = models.URLField(default='')
    has_iron = models.BooleanField(default=False)
    has_copper = models.BooleanField(default=False)
    has_silver = models.BooleanField(default=False)
    has_gold = models.BooleanField(default=False)
    has_platinum = models.BooleanField(default=False)
    has_candy = models.BooleanField(default=False)
    has_soil = models.CharField(max_length=2, choices=HAS_SOIL)
    history = models.CharField(max_length=2, choices=HISTORY)
    climate = models.CharField(max_length=2, choices=CLIMATE)
    world_size = models.CharField(max_length=2, choices=WORLD_SIZE)
    surroundings = models.CharField(max_length=2, choices=SURROUNDINGS)
    terrain = models.CharField(max_length=2, choices=TERRAIN)
    stone = models.CharField(max_length=2, choices=STONE)
    worlddescription = models.TextField(default='')
    worldgen = models.TextField(default='')
    prospect = models.TextField(default='')
    slug = models.SlugField(max_length=255, blank=True, default='', editable=False)
    author = models.CharField(max_length=255, default='')

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
