from django.contrib import admin
from django.contrib.auth.models import User
from . import models


# Register your models here.

class EntityAdmin(admin.StackedInline):
    model = models.ClientsEntity


class IndividualAdmin(admin.StackedInline):
    model = models.ClientsIndividual


class ApplicationsAdmin(admin.StackedInline):
    model = models.Applications


@admin.register(models.TypeUser)
class UserAdmin(admin.ModelAdmin):
    inlines = [ApplicationsAdmin, EntityAdmin, IndividualAdmin, ]
    list_display = ('user', 'type_user', )


admin.site.register(models.Banks)
admin.site.register(models.ClientsEntity)
admin.site.register(models.ClientsIndividual)
admin.site.register(models.Applications)
