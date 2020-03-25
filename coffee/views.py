from django.shortcuts import render, get_object_or_404
from .models import Range, Intensity, Coffee

# Create your views here.
def all_coffee(request):
    return render(request,'all_coffee.html', {'all_coffee':all_coffee})

"""A view that returns a single coffee page based on the coffee ID rendered to the 'postdetail.html' template"""
def coffee_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'coffeedetail.html', {'coffee': coffee})