from django.shortcuts import render
from checkout.models import OrderLineItem
from django.contrib.auth.models import User

# Create your views here.
def orderHistory(request):
    order_history = OrderLineItem.objects.filter(customer__exact = request.user)
    return render(request, 'orderhistory.html', {'order_history': order_history,})