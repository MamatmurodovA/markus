# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-17 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0048_auto_20180317_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('count_of_action', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('count_of_users', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='promotions/notifications/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='PromotionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(choices=[('click', 'Per click'), ('view', 'Per view')], max_length=12, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='companypromotion',
            name='promotion_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.PromotionType'),
        ),
    ]
