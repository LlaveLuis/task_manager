#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.forms import ModelForm

from user.models import User


class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'passw']
