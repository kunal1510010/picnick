# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0009_auto_20170630_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponcode',
            name='discount_offered',
            field=models.IntegerField(default=0),
        ),
    ]