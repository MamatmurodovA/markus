# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-20 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0054_notifications_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='call_center',
            field=models.CharField(max_length=13),
        ),
    ]
