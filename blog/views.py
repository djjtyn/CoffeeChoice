from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm, CommentForm

"""A view to allow user to see all blog posts published previously rendered to the 'blogposts.html' template"""
def all_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blogposts.html', {'posts': posts })

"""A view that returns a single blog post based on the post ID. Rendered to the 'postdetail.html' template"""
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    comments = post.comments.filter()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()
    return render(request, 'postdetail.html', {'post': post, 'comments': comments, 'new_comment': new_comment,
                                               'comment_form': comment_form})

"""A view that allows a user to create or edit a post """
def create_or_edit_a_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render (request, 'blogpostform.html', {'form': form})

