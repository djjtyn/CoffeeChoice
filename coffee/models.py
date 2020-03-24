from django.db import models

# Create your models here.

class Range(models.Model):
    name = models.CharField(max_length=35, blank=False)

    def __str__(self):
        return self.name


class Coffee(models.Model):
    name = models.CharField(max_length=40, blank=False)
    intensity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    coffee_range = models.ForeignKey(Range, default=1)
