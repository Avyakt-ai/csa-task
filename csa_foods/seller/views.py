from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Restaurant
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from .forms import SellerRegistrationForm
from django.contrib.auth import logout
import os
from django.conf import settings


def is_seller(user):
    return user.groups.filter(name='sellers').exists()


def not_authorized(request):
    return render(request, 'seller/not_authorized.html')


def seller_registration(request):
    # Below two lines if for when user is logged in and they clicks back button so that he will be logged out automatically.
    # Otherwise he can roam around login, and other pages while logged in but we don't want that so we do this.
    if request.user.is_authenticated:
        messages.success(request, f'You have been logged out of your account. Login In Again!')
        logout(request)
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            restaurant_name = form.cleaned_data['restaurant_name']
            opening_time = form.cleaned_data['opening_time']
            closing_time = form.cleaned_data['closing_time']
            address = form.cleaned_data['address']
            non_veg_available = form.cleaned_data['non_veg_available']
            contact_number = form.cleaned_data['contact_number']
            image = form.cleaned_data['image']
            # if not image:
            #     default_image_path = os.path.join(settings.MEDIA_ROOT, 'default_image.png')
            #     with open(default_image_path, 'rb') as img_file:
            #         image = img_file

            user = User.objects.create_user(username=username, email=email, password=password)

            # Below code is for including the seller to the "sellers" group.
            sellers_group, created = Group.objects.get_or_create(name='sellers')
            user.groups.add(sellers_group)

            restaurant = Restaurant.objects.create(
                seller=user,
                restaurant_name=restaurant_name,
                opening_time=opening_time,
                closing_time=closing_time,
                address=address,
                non_veg_available=non_veg_available,
                contact_number=contact_number,
                image=image,
            )
            restaurant.save()
            messages.success(request, f'Your account has been created! You can now login')

            return redirect('seller_login')
    else:
        form = SellerRegistrationForm()
    return render(request, 'seller/seller_registration.html', {'form': form})


def seller_login(request):
    if request.user.is_authenticated:
        messages.success(request, f'You have been logged out of your account. Login In Again!')
        logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('seller_dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'seller/seller_login.html')


@user_passes_test(is_seller, login_url='not_authorized')
def seller_dash(request):
    return render(request, 'seller/seller_dash.html')