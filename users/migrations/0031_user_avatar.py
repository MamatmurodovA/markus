# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-10 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20180309_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(blank=True,  null=True, on_delete=django.db.models.deletion.CASCADE, to='users.File'),
        ),
    ]
