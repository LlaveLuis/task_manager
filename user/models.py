#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models


class Role(models.Model):
    """Represents the available roles for users."""
    id = models.IntegerField(db_column='id_role', primary_key=True)
    description = models.CharField(max_length=64)
    id_creator = models.ForeignKey('User', db_column='id_creator',
                                   on_delete=models.PROTECT)
    time_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'role'


class User(models.Model):
    """Represents a system user."""
    username = models.CharField(max_length=32)
    passw = models.CharField(max_length=256)
    real_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    last_access = models.DateTimeField()
    id_creator = models.ForeignKey('User', db_column='id_creator',
                                   related_name='+', on_delete=models.PROTECT)
    id_updater = models.ForeignKey('User', db_column='id_updater',
                                   related_name='+', on_delete=models.PROTECT,
                                   blank=True, null=True)
    time_creation = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserRole(models.Model):
    """Store roles assigned to users."""
    id_user = models.ForeignKey(User, db_column='id_user',
                                on_delete=models.CASCADE)
    id_role = models.ForeignKey(Role, db_column='id_role',
                                on_delete=models.CASCADE)
    id_register = models.ForeignKey(User, db_column='id_register',
                                    related_name='+', on_delete=models.PROTECT)
    time_registry = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_user', 'id_role')
        db_table = 'user_role'
