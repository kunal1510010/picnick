# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0005_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site.MenuItem')),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site.VendorDetail')),
            ],
        ),
    ]
