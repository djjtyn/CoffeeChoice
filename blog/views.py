from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import BlogPostForm, CommentForm
from django.core.paginator import Paginator


"""A view to allow user to see all blog posts published previously rendered to the 'blogposts.html' template"""
def all_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 9)
    page = request.GET.get('page', 1)
    posts = paginator.page(page)
    return render(request, 'blogposts.html', {'posts': posts })

"""A view that returns a single blog post based on the post ID. Rendered to the 'postdetail.html' template"""
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post = post, published_date__lte=timezone.now()).order_by('-published_date')
    post.views += 1
    post.save()
    return render(request, 'postdetail.html', {'post': post, 'comments': comments})

"""A view that allows a user to comment on individual blog posts. Login required for this"""
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(post_detail, post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


