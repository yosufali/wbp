# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbp_app', '0005_auto_20160420_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emergency_contact',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
    ]