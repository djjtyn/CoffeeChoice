from django.shortcuts import render

# Create your views here.

#Return the index.html page
def index(request):
    return render(request, 'index.html')