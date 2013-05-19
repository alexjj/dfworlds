from django.views.generic import ListView, DetailView, CreateView
from .models import World


class WorldListView(ListView):

    model = World


class WorldDetailView(DetailView):

    model = World


class AddWorldView(CreateView):
    model = World