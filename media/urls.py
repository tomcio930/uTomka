'''
Created on 06-03-2013

@author: Comarch
'''
from django.conf.urls import patterns, url

from media import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)