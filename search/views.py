from django.shortcuts import render
from coffee.models import Coffee

# Create your views here.
def do_search(request):
    coffee = Coffee.objects.filter(name__icontains = request.GET['query'])
    if coffee:
        return render(request, 'all_coffee.html', {'all_coffee': coffee})
    else:
        return render(request, 'no_results.html')