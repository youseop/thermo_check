from django.contrib import admin
from django.urls import path, include
import accounts.views

urlpatterns = [
    path('login/', accounts.views.oauthlogin, name='oauthlogin'),
    path('accounts/', include('allauth.urls')),
]