# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 02:20
from __future__ import unicode_literals

import base.utils.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0004_auto_20170204_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Title')),
                ('slug', base.utils.models.AutoSlugField(blank=True, db_index=False, populate_from=b'title', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('status', models.CharField(choices=[(b'd', 'Draft'), (b'p', 'Published'), (b'w', 'Removed')], max_length=1)),
                ('is_closed', models.BooleanField(default=False, verbose_name='Closed')),
                ('is_removed', models.BooleanField(default=False)),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='Views count')),
                ('comment_count', models.PositiveIntegerField(default=0, verbose_name='Comment count')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Category', verbose_name='Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
    ]
