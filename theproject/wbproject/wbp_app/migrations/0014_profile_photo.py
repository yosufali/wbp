# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbp_app', '0013_remove_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='test.jpg', upload_to='media'),
            preserve_default=False,
        ),
    ]
