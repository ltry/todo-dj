# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 21:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('publish_date',)},
        ),
    ]
