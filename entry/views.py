#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render


def access(request):
    return render(request, 'login.html', {})


def logout(request):
    return render(request, 'logout.html', {})