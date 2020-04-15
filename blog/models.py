from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
"""Class below for a single blog post"""
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, related_name='comment')
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


