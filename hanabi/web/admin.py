from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Member)
admin.site.register(models.Language)
admin.site.register(models.Session)
admin.site.register(models.Exercise)
