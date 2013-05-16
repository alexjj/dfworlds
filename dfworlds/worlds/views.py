from django.views.generic import ListView, DetailView
from worlds.models import World

class PublishedPostMixin(object):

    def get_queryset(self):
        return self.model.objects.live()


class WorldListView(PublishedPostMixin, ListView):

    model = World


class WorldDetailView(PublishedPostMixin, DetailView):

    model = World
