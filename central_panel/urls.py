#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import url

urlpatterns = [
    url(r'^info', 'central_panel.views.info', name='info'),
]
