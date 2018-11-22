from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('deleted/<int:pk>/', views.itemDelete, name="delete"),
    path('checkout/', views.checkout, name='checkout'),
    path('listDelete/', views.listDelete, name='listDelete'),
]