# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0019_auto_20170301_2319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['creation'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
