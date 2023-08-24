from django.shortcuts import render, get_object_or_404
from ecomm.models import Product
from django.contrib.auth.models import User
from .models import Cart, CartItem
# Create your views here.

def addToCart(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    #itemId = request.GET['']
    print("ItemId:",product_id)
    print("Product Name:",product.name)
    return render(request,"index.html")



def cart(request):
    cart = Cart.objects.filter(user=request.user)
    print(f"user {request.user} : {cart}")
    user_cart = CartItem.objects.filter(cart__user=request.user)
    print(request.user)
    return render(request, 'cart.html', {'user_cart': user_cart})