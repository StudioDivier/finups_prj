from django.contrib import admin
from django.urls import path
from . import views

app_name = 'personal'

urlpatterns = [
    path('login', views.LoginView.as_view(), name="login"),

    path('sign-in', views.RegisterView.as_view(), name='signin'),
    path('sign-in/second', views.Register2View.as_view(), name='signin2'),

    path('logout', views.log_out, name='logout'),

    path('applications', views.ProfilePage.as_view(), name='personal_application'),
    path('create-application', views.CreateAppView.as_view(), name='create_application'),

    path('company', views.PersonalCompanyView.as_view(), name='personal_company'),
    path('add-company', views.AddCompanyView.as_view(), name='add_company'),

    path('create-partners/<int:id_app>', views.CreatePartView.as_view(), name='create_partners'),
]
