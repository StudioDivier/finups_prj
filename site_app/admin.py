from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.CallbackRequests)
class CRAdmin(admin.ModelAdmin):
    list_display = ('form_type', 'name', 'phone', 'email', 'date_request')
    search_fields = ('form_type', 'name', 'phone', 'email',)
    list_filter = ('form_type', 'date_request')\


class TypeServicesAdmin(admin.StackedInline):
    model = models.TypeService


@admin.register(models.ClassService)
class ClassServiceAdmin(admin.ModelAdmin):
    inlines = [TypeServicesAdmin, ]
    list_display = ('name_service',)
