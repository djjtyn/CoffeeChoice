from django.shortcuts import render
from checkout.models import Order
from django.contrib.auth.models import User

# Create your views here.
def orderHistory(request):
    order_history = Order.objects.filter(full_name = request.user)
    return render(request, 'orderhistory.html', {'order_history': order_history,})