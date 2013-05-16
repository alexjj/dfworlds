from django.conf.urls import patterns, url

from worlds.views import WorldListView, WorldDetailView

urlpatterns = patterns('',
    url(r'^$', WorldListView.as_view(), name="list"),
    url(r"^(?P<slug>[\w-]+)$", WorldDetailView.as_view(), name="detail"),
)
