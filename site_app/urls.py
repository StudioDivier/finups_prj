from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='main'),
    path('how-to-work', views.how_to_work, name='how'),
]