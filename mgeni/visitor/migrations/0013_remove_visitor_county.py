# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 06:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0012_auto_20180426_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='county',
        ),
    ]
