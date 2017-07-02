# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorDetails',
            fields=[
                ('vendor_id', models.IntegerField(default=1000, primary_key=True, serialize=False)),
                ('restaurant_name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
