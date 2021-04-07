from django.contrib import admin
from django.contrib.auth.models import User
from . import models


# Register your models here.

class EntityAdmin(admin.StackedInline):
    model = models.ClientsEntity


class IndividualAdmin(admin.StackedInline):
    model = models.ClientsIndividual


class ApplicationsBankAdmin(admin.StackedInline):
    model = models.ApplicationsBank


@admin.register(models.Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    inlines = [ApplicationsBankAdmin, ]


@admin.register(models.TypeUser)
class UserAdmin(admin.ModelAdmin):
    inlines = [EntityAdmin, IndividualAdmin, ]
    list_display = ('user', 'type_user', )


admin.site.register(models.Banks)
admin.site.register(models.ClientsEntity)
admin.site.register(models.ClientsIndividual)
# admin.site.register(models.Applications)
admin.site.register(models.ApplicationsBank)
