# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-24 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0050_auto_20180321_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='weektime',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
