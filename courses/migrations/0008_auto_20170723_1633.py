# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-23 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20170723_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Description'),
        ),
    ]