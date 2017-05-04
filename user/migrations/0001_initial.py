# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.IntegerField(serialize=False, db_column='id_role', primary_key=True)),
                ('description', models.CharField(max_length=64)),
                ('time_creation', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': False,
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('passw', models.CharField(max_length=256)),
                ('real_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('last_access', models.DateTimeField()),
                ('time_creation', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_registry', models.DateTimeField(auto_now_add=True)),
                ('id_register', models.ForeignKey(db_column='id_register', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='user.User')),
                ('id_role', models.ForeignKey(to='user.Role', db_column='id_role')),
                ('id_user', models.ForeignKey(to='user.User', db_column='id_user')),
            ],
            options={
                'db_table': 'user_role',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userrole',
            unique_together=set([('id_user', 'id_role')]),
        ),
    ]
