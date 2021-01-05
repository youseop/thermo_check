from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('<int:thermal_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name='newblog'),
    path('login/', views.oauthlogin, name='oauthlogin'),
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view()),
]
