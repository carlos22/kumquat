# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cron', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjob',
            name='when',
            field=models.CharField(choices=[('0,5,10,15,20,25,30,35,40,45,50,55 * * * *', 'every 5 minutes'), ('0,30 * * * *', 'every 30 minutes'), ('0 * * * *', 'hourly'), ('0 0 * * *', 'daily'), ('0 0 * * 0', 'weekly'), ('0 0 1 * *', 'monthly')], max_length=255, verbose_name='When'),
        ),
    ]
