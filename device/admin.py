from django.contrib import admin

# Register your models here.
from .models import Device, Element

admin.site.register(Device)
admin.site.register(Element)