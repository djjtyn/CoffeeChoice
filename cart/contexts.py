from django.shortcuts import get_object_or_404
from coffee.models import Coffee

def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        coffee = get_object_or_404(Coffee, pk=id)
        total += quantity * coffee.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'coffee': coffee})
    return { 'cart_items':cart_items, 'total': total, 'product_count': product_count}