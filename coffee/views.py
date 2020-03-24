from django.shortcuts import render, get_object_or_404
from .models import Range, Intensity, Coffee

# Create your views here.
def all_coffee(request):
    all_coffee = get_object_or_404(Coffee)
    return render(request,'all_coffee.html', {'all_coffee':all_coffee})