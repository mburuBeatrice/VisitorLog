# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0003_auto_20180411_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='departure',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
