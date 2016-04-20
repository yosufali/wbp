# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbp_app', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emergency_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='employable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='max_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phd_status',
            field=models.BooleanField(default=False),
        ),
    ]
