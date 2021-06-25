from django.contrib import admin
from .models import ColorToHexCodeMapping, GridColor

# Register your models here.
admin.site.register(ColorToHexCodeMapping)
admin.site.register(GridColor)
# admin.site.register(ColorsMapping)
