from django import forms
from .models import Post, Comment

"""Form to be used for site owner to post blogs with"""
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')

"""Form to be used for site users to post blog comments with"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
        'text':(''),
        }