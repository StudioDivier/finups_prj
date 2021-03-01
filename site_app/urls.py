from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='main'),
    path('how-to-work', views.WorkView.as_view(), name='how'),
    path('services', views.ServicesView.as_view(), name='services'),
]
