# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 23:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0009_auto_20170208_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='status',
        ),
    ]
