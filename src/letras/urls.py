# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',
    url(r'resultado/$', ResultadoView.as_view(), name='resultado'),
    url(r'^$', HomeView.as_view(), name='home'),
)
