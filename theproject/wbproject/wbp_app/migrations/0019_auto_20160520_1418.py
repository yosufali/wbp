# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wbp_app', '0018_tutorial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutorials_end_time',
            new_name='tutorial_end_time',
        ),
    ]
