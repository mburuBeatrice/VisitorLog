# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_auto_20180412_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='occupancy',
            field=models.CharField(choices=[('V', 'Vacant'), ('O', 'Occupied')], max_length=1),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('LR', 'Laundry'), ('RM', 'Rooms'), ('WF', 'Wifi')], max_length=10),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]
