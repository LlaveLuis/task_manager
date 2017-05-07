#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import date

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.safestring import mark_safe

from entry.decorators import logged
from calend.models import TaskCalendar

base_date = date.today()


@logged
def info(request, id_user=None):
    if id_user:
        cal = TaskCalendar().formatmonth(base_date.year, base_date.month)
        data = {'calendar': mark_safe(cal), }
        return render(request, 'info.html', data)
    else:
        request.session['res'] = 'Err'
        messages.error(request, 'Session has expired')
        return redirect('home')
