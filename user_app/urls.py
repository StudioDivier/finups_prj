from django.contrib import admin
from django.urls import path
from . import views

app_name = 'personal'

urlpatterns = [
    path('log-in', views.login, name='login'),
    path('sign-in', views.signin, name='signin'),
    path('sign-in/second', views.signin2, name='signin2'),
    path('applications', views.personal_application, name='personal_application'),
    path('company', views.personal_company, name='personal_company'),
    path('git', views.create_create_app, name='create_application'),
]
