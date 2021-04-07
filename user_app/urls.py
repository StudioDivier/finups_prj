from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'personal'

urlpatterns = [
    path('login', views.LoginView.as_view(), name="login"),

    path('sign-in', views.RegisterView.as_view(), name='signin'),
    path('sign-in/second', views.Register2View.as_view(), name='signin2'),

    path('logout', views.log_out, name='logout'),

    path('administration', views.PersonalConfigView.as_view(), name='config'),
    path('applications', views.ProfilePage.as_view(), name='personal_application'),
    path('applications/accept', views.ApplicationAccept.as_view(), name='personal_application_accept'),
    path('applications/reject', views.ApplicationReject.as_view(), name='personal_application_reject'),
    path('applications/pending', views.ApplicationPending.as_view(), name='personal_application_pending'),
    path('create-application', views.CreateAppView.as_view(), name='create_application'),

    path('company', views.PersonalCompanyView.as_view(), name='personal_company'),
    path('company/<slug:slug>/', views.CompanyDetail.as_view(), name='company-detail'),
    path('add-company', views.AddCompanyView.as_view(), name='add_company'),

    path('create-partners/<int:id_app>', views.CreatePartView.as_view(), name='create_partners'),

    # change pass
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='personal/password_change.html',
        success_url='/personal/company'
    ), name='change_password'),

    # forgot pass
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='signin/reset/password_reset.html',
             subject_template_name='signin/reset/password_reset_subject.txt',
             email_template_name='signin/reset/password_reset_email.html',
             success_url='done'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='signin/reset/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='signin/reset/password_reset_confirm.html',
             success_url='password_reset_complete'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='signin/reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    # path("password_reset", views.PasswordReset.as_view(), name="password_reset"),

]
