# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-01 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0004_promotiontype_promote_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotiontype',
            name='promote_type',
            field=models.CharField(choices=[('show_in_search', 'Show in search'), ('show_in_related', 'Show in related')], max_length=40),
        ),
    ]
