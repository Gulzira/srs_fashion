from django.contrib import admin
from .models import Guest, Brand, Dress, DressInstance

admin.site.register(Dress)
admin.site.register(Guest)
admin.site.register(Brand)
admin.site.register(DressInstance)