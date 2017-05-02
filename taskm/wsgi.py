#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskm.settings")

application = get_wsgi_application()
