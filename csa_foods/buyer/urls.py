from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.buyer_login, name='buyer_login'),
    path('dash/', views.buyer_dash, name='buyer_dashboard'),
    path('view_food_items/<int:restaurant_id>/', views.view_food_items, name='view_food_items'),
    path('register/', views.buyer_register, name='buyer_register'),
]
