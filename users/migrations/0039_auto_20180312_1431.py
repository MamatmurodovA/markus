# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-12 14:31
from __future__ import unicode_literals

from django.db import migrations
import geosimple.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_auto_20180312_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='location',
            field=geosimple.fields.GeohashField(db_index=True, default={'latitude': 50.822482, 'longitude': -0.141449}, editable=False, max_length=12),
        ),
    ]
