from django.urls import path

from . import views

urlpatterns = [
    path('add-to-cart/<int:product_id>/',views.addToCart, name='addToCart'),
    path('cart/',views.cart, name='cart'),
    
       
]
