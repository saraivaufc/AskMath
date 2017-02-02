# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 11:30
from __future__ import unicode_literals

import ask.utils.colors
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0002_issue_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='color',
            field=models.CharField(blank=True, default=ask.utils.colors.get_color, max_length=20),
        ),
    ]
