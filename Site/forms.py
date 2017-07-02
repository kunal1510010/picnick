from django import forms


class UserRegister(forms.Form):
    first_name = forms.CharField(required=True, label="First name", max_length=20,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, label="Last name", max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, label="Email Id",
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(required=True, label="Password",
                               widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    contact_number = forms.IntegerField(required=True,
                                        widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}))
    address = forms.CharField(required="false", label="Address",
                              widget=forms.TextInput(attrs={'placeholder': 'Address'}))


class VendorRegister(forms.Form):
    restaurant_name = forms.CharField(required=True, label="Restaurant Name", max_length=20,
                                      widget=forms.TextInput(attrs={'placeholder': 'Restaurant Name'}))
    email = forms.EmailField(required=True, label="Email Id",
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(required=True, label="Password",
                               widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    contact_number = forms.IntegerField(required=True,
                                        widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}))
    address = forms.CharField(required="false", label="Address",
                              widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    widgets = {
        'password': forms.PasswordInput(),
    }


class LogInUser(forms.Form):
    email_id = forms.CharField(required=True, label="Email ID", max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': 'Email Id'}))
    password = forms.CharField(widget=forms.PasswordInput)

    widgets = {
        'password': forms.PasswordInput(),
    }


class OrderForm(forms.Form):
    delivery_address = forms.CharField(required=True, label="Delivery Address", max_length=20,
                                       widget=forms.TextInput(
                                           attrs={'placeholder': 'XYZ street, Sample Colony, Locality'}))
    pincode = forms.IntegerField(required=True,
                                 widget=forms.TextInput(attrs={'placeholder': '111111'}))
    coupon_code = forms.CharField(required=False, label="Coupon Code", max_length=20,
                                  widget=forms.TextInput(attrs={'placeholder': 'Coupon Code'}))

class SearchForm(forms.Form):
    query = forms.CharField(required=True, label="Search Using Location or Cousine",max_length=100)