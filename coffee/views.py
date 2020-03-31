from django.shortcuts import render, get_object_or_404, redirect
from .models import Range, Intensity, Coffee, Comment
from .forms import CommentForm

# Create your views here.
def all_coffee(request):
    all_coffee = Coffee.objects.all()
    return render(request,'all_coffee.html', {'all_coffee':all_coffee})

"""A view that returns a single coffee page based on the coffee ID rendered to the 'postdetail.html' template"""
def coffee_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'coffeedetail.html', {'coffee': coffee})

# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Coffee, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect(coffee_detail, post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'add_comment_to_post.html', {'form': form})
