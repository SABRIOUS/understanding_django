from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Author)
admin.site.register(models.Language)
admin.site.register(models.Snippet)
admin.site.register(models.Tag)
