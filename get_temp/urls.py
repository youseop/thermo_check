from django.urls import path
from . import views

urlpatterns = [
    path('<int:thermal_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name='newblog'),
]
