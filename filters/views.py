from django.shortcuts import render
from coffee.models import Coffee

# Create your views here.


def filter_vertuo(request):
    coffee = Coffee.objects(coffee_range =='Vertuo')
    if coffee:
        return render(request, 'all_coffee.html', {'all_coffee': coffee})
    else:
        return render(request, 'no_results.html')

def filter_original(request):
    coffee = Coffee.objects.filter(coffee_range ='Original')
    if coffee:
        return render(request, 'all_coffee.html', {'all_coffee': coffee})
    else:
        return render(request, 'no_results.html')
