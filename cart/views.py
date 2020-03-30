from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

def view_cart(request):
    return render(request, 'cart.html')

@login_required
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart',{})
    cart[id] = cart.get(id, 0) + quantity
    request.session['cart'] = cart
  
    return redirect(reverse('all_coffee'))

def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))  
    cart = request.session.get('cart',{})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))