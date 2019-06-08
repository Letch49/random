from django.contrib import admin
from . import models
# Register your models here.
class UsersInCompanyAdmin(admin.TabularInline):
  model = models.UsersInCompanies

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
  inlines=[UsersInCompanyAdmin]