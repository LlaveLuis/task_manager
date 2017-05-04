#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'user', include('user.urls')),
    url(r'calend', include('calend.urls')),
    url(r'task', include('task.urls')),
    url(r'show', include('central_panel.urls')),
    url(r'', include('entry.urls')),
]
