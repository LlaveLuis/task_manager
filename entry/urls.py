#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^logout', 'entry.views.logout', name='logout'),
    url(r'^', 'entry.views.access', name='home'),
]
