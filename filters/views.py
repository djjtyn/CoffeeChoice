from django.shortcuts import render
from coffee.models import Coffee
from django.core.paginator import Paginator

# Create your views here.


def filter_vertuo(request):
    coffee = Coffee.objects.filter(coffee_range__name ='Vertuo')
    paginator = Paginator(coffee, 9)
    page = request.GET.get('page', 1)
    coffee = paginator.page(page)
    if coffee:
        return render(request, 'all_coffee.html', {'all_coffee': coffee})
    else:
        return render(request, 'no_results.html')

def filter_original(request):
    coffee = Coffee.objects.filter(coffee_range__name ='Original')
    paginator = Paginator(coffee, 9)
    page = request.GET.get('page', 1)
    page = request.GET.get('page', 1)
    coffee = paginator.page(page)
    if coffee:
        return render(request, 'all_coffee.html', {'all_coffee': coffee})
    else:
        return render(request, 'no_results.html')
