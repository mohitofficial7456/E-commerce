from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login',handlelogin),
    path('logout',handlelogout),
    path('signup',signup),
]
