# shop/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    
    path('plant/add/', views.plant_create, name='plant_create'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plant/<int:pk>/edit/', views.plant_update, name='plant_update'),
     path('plant/<int:pk>/delete/', views.plant_delete, name='plant_delete'),
    path('pots/', views.pots_list, name='pots_list'),
    path('pots/add/', views.add_pot, name='add_pot'),
    path('pots/edit/<int:pk>/', views.edit_pot, name='edit_pot'),
    path('pots/delete/<int:pk>/', views.delete_pot, name='delete_pot'),
]

