# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 14:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wbp_app', '0019_auto_20160520_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
