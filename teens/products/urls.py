from django.urls import path
from . import views

products_patterns = ([
    path('', views.products, name="products"),
    path('<int:pk>/<slug:slug>/', views.product, name="product"),
], 'products')
