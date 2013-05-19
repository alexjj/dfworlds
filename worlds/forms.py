from django.forms import ModelForm

from .models import World


class WorldForm(ModelForm):
    class Meta:
        model = World
