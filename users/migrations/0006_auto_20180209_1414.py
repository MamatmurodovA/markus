# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 14:14
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('address', models.TextField()),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
                ('call_center', models.CharField(max_length=12)),
                ('opening_time', models.TimeField(null=True)),
                ('closing_time', models.TimeField(null=True)),
                ('website', models.URLField(null=True)),
                ('status', models.CharField(choices=[(0, 'Blocked'), (1, 'Active'), (2, 'Pending')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='is_top',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_category', to='users.Category'),
        ),
    ]
