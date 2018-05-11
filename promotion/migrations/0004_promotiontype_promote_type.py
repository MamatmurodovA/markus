# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-01 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0003_auto_20180331_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotiontype',
            name='promote_type',
            field=models.CharField(choices=[('click', 'Per click'), ('view', 'Per view'), ('notification', 'Per notification')], default='show_in_search', max_length=40),
            preserve_default=False,
        ),
    ]
