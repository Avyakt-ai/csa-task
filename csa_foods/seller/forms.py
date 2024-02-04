from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Restaurant

class SellerRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    restaurant_name = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)
    opening_time = forms.TimeField()
    closing_time = forms.TimeField()
    non_veg_available = forms.BooleanField(required=False)
    address = forms.CharField(required=False)
    contact_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'restaurant_name', 'address', 'contact_number', 'opening_time', 'closing_time', 'non_veg_available', 'image']