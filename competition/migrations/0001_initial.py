# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-21 17:28
from __future__ import unicode_literals

import base.utils.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', base.utils.models.AutoSlugField(blank=True, db_index=False, populate_from='title', unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'ordering': ['-creation'],
                'verbose_name': 'Challenge',
                'verbose_name_plural': 'Challenges',
            },
        ),
    ]
