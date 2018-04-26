# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0024_auto_20180426_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupancy', models.CharField(choices=[('V', 'Vacant'), ('O', 'Occupied')], default='V', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='occupancy',
        ),
        migrations.AddField(
            model_name='availability',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visitor.Room'),
        ),
    ]