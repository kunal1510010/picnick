# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserRegister, VendorRegister, LogInUser, OrderForm, SearchForm
from passlib.hash import pbkdf2_sha256
from .models import UserDetail, VendorDetail, OrderDetail, MenuItem
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def get_user(request):
    if 'email' in request.session:
        return HttpResponseRedirect('/Site/')
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        print(form.is_valid())
        if form.is_valid():
            first_name_temp = form.cleaned_data["first_name"]
            last_name_temp = form.cleaned_data["last_name"]
            email_temp = form.cleaned_data["email"]
            password_temp = form.cleaned_data["password"]
            enc_password = pbkdf2_sha256.encrypt(password_temp)
            contact_temp = form.cleaned_data["contact_number"]
            address_temp = form.cleaned_data["address"]
            user_object = UserDetail.objects.create(first_name=first_name_temp,
                                                    last_name=last_name_temp,
                                                    email_id=email_temp, password=enc_password,
                                                    phone_number=contact_temp, address=address_temp)
            request.session['email'] = email_temp
            user_object.save()
            try:
                subject = "Registration Notice"
                message = "Thanks for Your Registration with Picnick"
                from_email = settings.EMAIL_HOST_USER
                send_mail(subject, message, from_email, [email_temp], fail_silently=False)
            except:
                messages.error(request, 'Not Connected to internet or invalid email id provided ')
                return HttpResponseRedirect('/Site/login/user/')
    return render(request, 'register.html', {'form': form})


def get_vendor(request):
    if 'email' in request.session:
        return render(request, 'index.html')
    form = VendorRegister()
    if request.method == 'POST':
        form = VendorRegister(request.POST)
        print(form.is_valid())
        if form.is_valid():
            restaurant_name_temp = form.cleaned_data["restaurant_name"]
            email_temp = form.cleaned_data["email"]
            password_temp = form.cleaned_data["password"]
            enc_password = pbkdf2_sha256.encrypt(password_temp)
            contact_temp = form.cleaned_data["contact_number"]
            address_temp = form.cleaned_data["address"]
            vendor_object = VendorDetail.objects.create(restaurant_name=restaurant_name_temp,
                                                        email_id=email_temp, password=enc_password,
                                                        phone_number=contact_temp, address=address_temp)
            request.session['email'] = email_temp
            vendor_object.save()
            return HttpResponseRedirect('/Site/login/vendor/')
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if 'email' in request.session:
        return HttpResponseRedirect('/Site/')
    form = LogInUser()
    if request.method == 'POST':
        form = LogInUser(request.POST)
        if form.is_valid():
            email_tmp = form.cleaned_data["email_id"]
            password_tmp = form.cleaned_data["password"]
            try:
                user_check = UserDetail.objects.get(email_id=email_tmp)
                if pbkdf2_sha256.verify(password_tmp, user_check.password):
                    request.session['email'] = email_tmp
                    return HttpResponseRedirect('/Site/')
                else:
                    messages.error(request, "Password Incorrect")
            except ObjectDoesNotExist:
                messages.error(request, "SignUp First")

    return render(request, 'login.html', {'form': form})


def login_vendor(request):
    if 'email' in request.session:
        return render(request, 'index.html')
    form = LogInUser()
    if request.method == 'POST':
        form = LogInUser(request.POST)
        if form.is_valid():
            email_tmp = form.cleaned_data["email_id"]
            password_tmp = form.cleaned_data["password"]
            try:
                vendor_check = VendorDetail.objects.get(email_id=email_tmp)
                if pbkdf2_sha256.verify(password_tmp, vendor_check.password):
                    request.session['email'] = email_tmp
                    return HttpResponseRedirect('/Site/login/vendor')
                else:
                    messages.error(request, "Password Incorrect")
            except ObjectDoesNotExist:
                messages.error(request, "SignUp First")

    return render(request, 'register.html', {'form': form})


def order_place(request):
    form = LogInUser()
    if 'email' in request.session:
        if request.method == 'POST':
            form = OrderForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                delivery_address_temp = form.cleaned_data["delivery_address"]
                pincode_temp = form.cleaned_data["pincode"]
                coupon_code_temp = form.cleaned_data["coupon_code"]
                delivery_object = OrderDetail.objects.create(vendor_id=1001, user_id=1001,
                                                             delivery_address=delivery_address_temp,
                                                             pincode=pincode_temp, coupon_code=coupon_code_temp,
                                                             order_amount=100)
                delivery_object.save()
                return HttpResponseRedirect('/Site/')
        return HttpResponseRedirect('/Site/order/')
    else:
        return HttpResponseRedirect('/Site/login/user/')


def logout(request):
    form = LogInUser()
    if 'email' in request.session:
        del request.session['email']
        return HttpResponseRedirect('/Site/login/user')
    else:
        messages.error(request, "You are already Logged out")
        return HttpResponseRedirect('/Site/')


def home(request):
    form = SearchForm()
    if request.method =='POST':
        print("true")
        form = SearchForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            key = form.cleaned_data["query"]
            return HttpResponseRedirect('/Site/search')
    return render(request,"index.html",{'form': form})


def vendor_profile(request, vendor_id):
    vendor = VendorDetail.objects.get(vendor_id=vendor_id)
    menu = MenuItem.objects.filter(vendor_id=vendor_id)
    return render(request,"resto new.html",{'vendor': vendor , 'menu': menu})


def search(request):
    form = SearchForm()
    if request.method == 'POST':
                form = SearchForm(request.POST)
                if form.is_valid():
                    search_tmp = form.cleaned_data["query"]
                    list_item = VendorDetail.objects.filter(restaurant_name__contains=search_tmp)
                    return render(request, 'search-rest.html', {'form': form,'list': list_item })
                else :
                    return HttpResponseRedirect('/Site/')

    list_item = VendorDetail.objects.all()
    return render(request, 'search-rest.html', {'form': form, 'list':list_item })
