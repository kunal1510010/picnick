# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserDetail, VendorDetail, MenuItem, CouponCode, OrderDetail
from django.contrib import admin

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(VendorDetail)
admin.site.register(MenuItem)
admin.site.register(CouponCode)
admin.site.register(OrderDetail)