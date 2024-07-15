# operation_theatre/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_operation_theatre, name='list'),
    path('add/', views.add_operation_theatre, name='add'),
    path('edit/<int:pk>/', views.edit_operation_theatre, name='edit'),
    path('delete/<int:pk>/', views.delete_operation_theatre, name='delete'),
]
