from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=30, blank=False)
    original_range = models.BooleanField(default=False)
    vertuo_range = models.BooleanField(default=False)
    intensity = models.IntegerField(max_value=10)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
