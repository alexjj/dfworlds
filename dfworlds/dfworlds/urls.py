from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
    url(r'^worlds/', include('worlds.urls', namespace="worlds")),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
