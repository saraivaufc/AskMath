# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0002_auto_20170312_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['number'], 'verbose_name': 'Level', 'verbose_name_plural': 'Levels'},
        ),
        migrations.AlterField(
            model_name='levelmanager',
            name='level',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gamification.Level', verbose_name='Level'),
        ),
    ]