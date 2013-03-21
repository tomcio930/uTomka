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
    url(r'^image/(?P<image_id>\d+)/$', views.image, name='image'),
    url(r'^go_to_page/$', views.go_to_page, name='go_to_page'),
    url(r'^media/images/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT, 'show_indexes': True})
)