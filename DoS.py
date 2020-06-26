from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.utils import timezone

# An example django view to handle user request
def addItemToCart(request):
	user = User.objects.get(id=request.POST['userID'])
	cart = Cart.objects.get(user=user)
	cartItem = CartItem.objects.create(text=request.POST['itemID'], cart=cart)
	# A malicious user can send this request a million time 
	# to exhaust your disk space and memory with adding millions of items to the cart


# More secured way 
CART_ITEM_LIMIT = 4000
def addItemToCart(request):
	user = User.objects.get(id=request.POST['userID'])
	cart = Cart.objects.get(user=user)
	cartItemCount = CartItem.objects.filter(cart=cart).count()
	if cartItemCount < MAX_CART_LIMIT:
		cartItem = CartItem.objects.create(text=request.POST['itemID'], cart=cart)
		# This way, users can't exhaust your resources