from django.conf.urls import patterns, url

from .views import WorldListView, WorldDetailView, AddWorldView

urlpatterns = patterns(
    '',
    url(r'^$', WorldListView.as_view(), name="list"),
    url(r'^addworld$', AddWorldView.as_view(), name="addworld"),
    url(r"^(?P<slug>[\w-]+)$", WorldDetailView.as_view(), name="detail"),
)
