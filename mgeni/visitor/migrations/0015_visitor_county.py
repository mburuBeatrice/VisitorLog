# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0014_auto_20180426_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visitor.County'),
        ),
    ]
