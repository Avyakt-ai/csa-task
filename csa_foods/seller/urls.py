from django.contrib import admin
from django.urls import path, include
from . import views
from buyer import views as buyer_views

urlpatterns = [
    path('login/', views.seller_login, name='seller_login'),
    path('dash/', views.seller_dash, name='seller_dashboard'),
    path('seller-registration/', views.seller_registration, name='seller_registration'),
    path('not_authorized/', views.not_authorized, name='not_authorized'),
]
