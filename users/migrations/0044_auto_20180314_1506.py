# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-14 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_recentlyviewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
