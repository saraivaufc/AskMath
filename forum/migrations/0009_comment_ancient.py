# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20170207_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ancient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Comment', verbose_name='Ancient'),
        ),
    ]