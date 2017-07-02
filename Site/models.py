# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class UserDetail(models.Model):
    user_id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    phone_number = models.IntegerField(null=True)
    address = models.CharField(null=True, max_length=100)

    def __str__(self):
        return str(self.user_id)


class VendorDetail(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    phone_number = models.IntegerField(null=True)
    address = models.CharField(null=True, max_length=100)
    cod_availabitity = models.BooleanField(default=False)
    home_delivery = models.BooleanField(default=False)

    def __str__(self):
        return str(self.vendor_id)


class MenuItem(models.Model):
    vendor_id = models.ForeignKey(VendorDetail)
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField(null=False)
    order_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.item_id)


class CouponCode(models.Model):
    vendor_id = models.ForeignKey(VendorDetail)
    coupon_code = models.CharField(max_length=20)
    discount_offered = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.coupon_code


class OrderDetail(models.Model):
    item_id = models.ForeignKey(MenuItem)
    user_id = models.ForeignKey(UserDetail)
    delivery_id = models.AutoField(primary_key=True)
    delivery_address = models.CharField(max_length=100)
    pincode = models.IntegerField(null=False)
    coupon_code = models.CharField(max_length=20, null=True)
    order_amount = models.IntegerField(null=False, default=0)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.delivery_id)