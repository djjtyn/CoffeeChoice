from django.contrib import admin
from .models import Range, Coffee, Intensity, Comment

# Register your models here.
admin.site.register(Range)
admin.site.register(Coffee)
admin.site.register(Intensity)
admin.site.register(Comment)