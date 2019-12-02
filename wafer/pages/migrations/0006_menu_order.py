# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-30 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_page_cache_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='menu_order',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Ordering in the menu (smaller numbers come first)', null=True),
        ),
    ]