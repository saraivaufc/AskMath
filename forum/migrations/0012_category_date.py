# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 01:38
from __future__ import unicode_literals

from django.db import migrations, models

import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_category_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now(), verbose_name='Date'),
            preserve_default=False,
        ),
    ]
