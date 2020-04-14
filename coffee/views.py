from django.shortcuts import render, get_object_or_404, redirect
from .models import Range, Intensity, Coffee, Comment
from .forms import CommentForm
from django.utils import timezone

# Create your views here.
def all_coffee(request):
    all_coffee = Coffee.objects.all()
    range = Range.objects.all()
    intensity = Intensity.objects.all()
    return render(request,'all_coffee.html', {'all_coffee':all_coffee, 'ranges': range, 'intensity': intensity})

"""A view that returns a single coffee page based on the coffee ID rendered to the 'postdetail.html' template"""
def coffee_review(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    comments = Comment.objects.filter(coffee =coffee, created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'coffeereview.html', {'coffee': coffee, 'comments': comments})

def add_comment_to_coffee(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.coffee = coffee
            comment.author = request.user
            comment.save()
            return redirect(coffee_review, coffee.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_coffee.html', {'form': form})
