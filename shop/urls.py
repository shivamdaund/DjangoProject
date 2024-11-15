# shop/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plant/new/', views.plant_create, name='plant_create'),
    path('plant/<int:pk>/edit/', views.plant_update, name='plant_update'),
    path('plant/<int:pk>/delete/', views.plant_delete, name='plant_delete'),
]



