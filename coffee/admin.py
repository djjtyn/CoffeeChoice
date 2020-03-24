from django.contrib import admin
from .models import Range, Coffee, Intensity

# Register your models here.
admin.site.register(Range)
admin.site.register(Coffee)
admin.site.register(Intensity)