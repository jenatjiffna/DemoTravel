from django.contrib import admin

# Register your models here.
from .models import place, pics

admin.site.register(place)
admin.site.register(pics)