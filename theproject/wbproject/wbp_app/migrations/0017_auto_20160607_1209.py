# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 12:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wbp_app', '0016_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_date', models.DateField()),
                ('lecture_start_time', models.TimeField()),
                ('lecture_end_time', models.TimeField()),
                ('lecture_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_date', models.DateField()),
                ('tutorial_start_time', models.TimeField()),
                ('tutorial_end_time', models.TimeField()),
                ('tutorial_group', models.CharField(max_length=2)),
                ('tutorial_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tutorial',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wbp_app.Module'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lecture',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wbp_app.Module'),
        ),
    ]
