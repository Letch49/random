from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.AdminModel)
class AdminModel(admin.ModelAdmin):
    list_display = ('title',)
