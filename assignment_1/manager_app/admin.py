from django.contrib import admin
from manager_app import models
# Register your models here.

admin.site.register(models.Manager)
admin.site.register(models.Employee)
