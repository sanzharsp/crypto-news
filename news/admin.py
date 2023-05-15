from django.contrib import admin
from . import models

admin.site.register(models.Article)
admin.site.register(models.Journalist)
# Register your models here.
