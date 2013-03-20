'''
Created on 06-03-2013

@author: Comarch
'''
from django.conf.urls import patterns, url
from uTomka.settings import MEDIA_ROOT
from media import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page>\d+)/$', views.index, name='index'),
    url(r'^media/images/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT, 'show_indexes': True})
)