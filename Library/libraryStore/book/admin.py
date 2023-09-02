from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Books)
admin.site.register(models.SubCategory)
admin.site.register(models.Category)