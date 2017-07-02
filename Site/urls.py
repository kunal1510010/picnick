from django.conf.urls import url
from . import views

app_name = 'Site'

urlpatterns = [
    url(r'^register/user$', views.get_user, name='Register User'),
    url(r'^register/vendor$', views.get_vendor, name='Register Vendor'),
    url(r'^login/user$', views.login_user, name='Login User'),
    url(r'^login/vendor$', views.login_vendor, name='Login Vendor'),
    url(r'^order$', views.order_place, name='Place Order'),
    url(r'^logout$', views.logout, name='Logout'),
    url(r'^$', views.home, name='Home'),
    url(r'^vendor/profile$', views.vendor_profile, name='Vendor Profile'),

]
