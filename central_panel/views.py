#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages

from entry.decorators import logged


@logged
def info(request, id_user=None):
    if id_user:
        return render(request, 'info.html')
    else:
        request.session['res'] = 'Err'
        messages.error(request, 'Session has expired')
        return redirect('home')
