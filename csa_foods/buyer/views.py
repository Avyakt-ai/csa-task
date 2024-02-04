from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from seller.models import Restaurant, FoodItem

def type_of_user(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'buyer/type_of_user.html')


def buyer_register(request):
    # When we create a form it is sent as a POST request.
    if request.user.is_authenticated:
        messages.success(request, f'You have been logged out of your account. Login In Again!')
        logout(request)
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login')
            form.save()
            return redirect('buyer_login')
    else:
        form = UserRegisterForm()
    return render(request, 'buyer/register.html', {'form': form})


def buyer_login(request):
    if request.user.is_authenticated:
        messages.success(request, f'You have been logged out of your account. Login In Again!')
        logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('buyer_dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'buyer/buyer_login.html')


@login_required
def buyer_dash(request):
    user_name = request.user.username
    restaurants = Restaurant.objects.all()

    return render(request, 'buyer/buyer_dash.html', {
        'user_name': user_name,
        'restaurants': restaurants,
    })

def view_food_items(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    food_items = FoodItem.objects.filter(restaurant=restaurant)
    return render(request, 'buyer/view_food_items.html', {'restaurant': restaurant, 'food_items': food_items})