#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from user.models import User
from .forms import LoginForm


def access(request):
    """View to process authentication user."""
    # verify if an open session exists
    id_server = request.session.session_key
    if id_server is not None:
        id_client = request.COOKIES['sessionid']
        id_user = request.session.get('id_user')
        if id_client == id_server and id_user:
            res = User.registry_user(id_user)
            if res['name']:
                return redirect('info')
    # from POST, data verification is required
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            res = User.verify_user(request.POST['username'],
                                   request.POST['passw'])
            if res['name']:
                request.session.create()
                if not ('remember' in request.POST):
                    request.session.set_expiry(300)
                request.session['id_user'] = res['id_user']
                request.session['name'] = res['name']
                return redirect('info')
            else:
                request.session['res'] = 'Err'
                messages.error(request, 'Wrong username or password')
                return redirect('home')
        else:
            request.session['res'] = 'Err'
            messages.error(request, form.errors)
            return redirect('home')
    else:
        msg = messages.get_messages(request)
        c = {}
        if msg:
            c['messages'] = messages.get_messages(request)
        return render(request, 'login.html', c)


def logout(request):
    """View for session close."""
    request.session.flush()
    return render(request, 'logout.html', {})