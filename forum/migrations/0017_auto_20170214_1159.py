# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 14:59
from __future__ import unicode_literals

from django.db import migrations
import forum.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0016_auto_20170210_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=forum.utils.models.AutoSlugField(blank=True, db_index=False, populate_from=b'name', unique=True),
        ),
    ]
