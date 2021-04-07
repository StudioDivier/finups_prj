from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.views.generic import TemplateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.contrib.auth.models import User
from . import forms
from . import models
from datetime import datetime
from site_app import models as site_models


def log_out(request):
    logout(request)
    return redirect('personal:login')


class LoginView(TemplateView):
    template_name = "signin/login-page.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        print(request)
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("personal:personal_application")
            else:
                context['error'] = "Логин или пароль неправильные"

        return render(request, self.template_name, context)


class RegisterView(TemplateView):
    template_name = "signin/signin-page.html"

    def dispatch(self, request, *args, **kwargs):
        form = forms.SignStageOne()
        if request.method == 'POST':
            username = request.POST.get('email')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                user = User.objects.create_user(username, email, password)
                login(request, user)
                return redirect(reverse('personal:signin2'))
        return render(request, self.template_name, {'form': form})


class Register2View(TemplateView):
    template_name = 'signin/signin-page2.html'

    def dispatch(self, request, *args, **kwargs):
        if '/personal/sign-in' not in str(self.request.META.get('HTTP_REFERER')):
            return redirect('personal:signin')
        if request.method == 'POST':
            type_user = request.POST['choice']
            base_user = User.objects.get(email=str(self.request.user))
            obj = models.TypeUser(type_user=type_user, user_id=base_user.id)
            obj.save()

            return redirect("personal:personal_application")

        return render(request, self.template_name, )


class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = "personal/personal_application.html"

    login_url = '/personal/login'
    redirect_field_name = 'personal_application'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if self.request.user:
            person = User.objects.get(username=self.request.user)
            if person.is_superuser or person.is_staff:
                return redirect('admin:index')
        try:
            base_user = User.objects.get(email=str(self.request.user))
            main_user = models.TypeUser.objects.get(user_id=base_user.id)
            data = models.Applications.objects.all().filter(owner_id=main_user.id)
            context['apps'] = data
            context['status'] = models.Applications.STATUS_TYPE
        except Exception:
            context['error'] = 'Список Ваших заявок пуст, но вы можете это исправить.'

        return render(request, self.template_name, context)


class ApplicationAccept(LoginRequiredMixin, TemplateView):
    template_name = "personal/personal_application.html"

    login_url = '/personal/login'
    redirect_field_name = 'personal_application'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if self.request.user:
            person = User.objects.get(username=self.request.user)
            if person.is_superuser or person.is_staff:
                return redirect('admin:index')
        try:
            base_user = User.objects.get(email=str(self.request.user))
            main_user = models.TypeUser.objects.get(user_id=base_user.id)
            data = models.Applications.objects.all().filter(owner_id=main_user.id).filter(status=models.Applications.accept)
            context['apps'] = data
            context['status'] = models.Applications.STATUS_TYPE
            context['now_status'] = models.Applications.accept
        except Exception:
            context['error'] = 'Список Ваших заявок пуст, но вы можете это исправить.'

        return render(request, self.template_name, context)


class ApplicationReject(LoginRequiredMixin, TemplateView):
    template_name = "personal/personal_application.html"

    login_url = '/personal/login'
    redirect_field_name = 'personal_application'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if self.request.user:
            person = User.objects.get(username=self.request.user)
            if person.is_superuser or person.is_staff:
                return redirect('admin:index')
        try:
            base_user = User.objects.get(email=str(self.request.user))
            main_user = models.TypeUser.objects.get(user_id=base_user.id)
            data = models.Applications.objects.all().filter(owner_id=main_user.id).filter(status=models.Applications.reject)
            context['apps'] = data
            context['status'] = models.Applications.STATUS_TYPE
            context['now_status'] = models.Applications.reject
        except Exception:
            context['error'] = 'Список Ваших заявок пуст, но вы можете это исправить.'

        return render(request, self.template_name, context)


class ApplicationPending(LoginRequiredMixin, TemplateView):
    template_name = "personal/personal_application.html"

    login_url = '/personal/login'
    redirect_field_name = 'personal_application'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if self.request.user:
            person = User.objects.get(username=self.request.user)
            if person.is_superuser or person.is_staff:
                return redirect('admin:index')
        try:
            base_user = User.objects.get(email=str(self.request.user))
            main_user = models.TypeUser.objects.get(user_id=base_user.id)
            data = models.Applications.objects.all().filter(owner_id=main_user.id).filter(status=models.Applications.pending)
            context['apps'] = data
            context['status'] = models.Applications.STATUS_TYPE
            context['now_status'] = models.Applications.pending
        except Exception:
            context['error'] = 'Список Ваших заявок пуст, но вы можете это исправить.'

        return render(request, self.template_name, context)


class PersonalCompanyView(LoginRequiredMixin, TemplateView):
    template_name = 'personal/personal_company.html'

    login_url = '/personal/login'
    redirect_field_name = '/personal/company/'

    def get(self, request, *args, **kwargs):
        context = {}
        try:
            base_user = User.objects.get(email=str(self.request.user))
            main_user = models.TypeUser.objects.get(user_id=base_user.id)
            entity = models.ClientsEntity.objects.all().filter(owner_id=main_user.id)
            context['entity_list'] = entity
        except Exception:
            context['error'] = 'Список Ваших команий пуст, но вы можете это исправить.'

        return render(request, self.template_name, context)


class CreateAppView(LoginRequiredMixin, TemplateView):
    template_name = 'personal/create_application.html'

    login_url = '/personal/login'
    redirect_field_name = '/personal/create_application/'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        # load services
        try:
            context['serv_list'] = site_models.ClassService.objects.all()
            context['serv'] = site_models.TypeService.objects.all()

            # load companies
            base_user = User.objects.get(email=str(self.request.user))
            main_user = models.TypeUser.objects.get(user_id=base_user.id)
            entity = models.ClientsEntity.objects.all().filter(owner_id=main_user.id)
            context['companies'] = entity

            if request.method == 'POST':
                data = {}

                cmp = request.POST['company']
                data['company'] = models.ClientsEntity.objects.get(org_name=cmp.split()[1])

                data['type_service'] = request.POST['type_service']
                data['service'] = request.POST['service']
                data['zakon'] = request.POST['zakon']
                data['purchase_number'] = request.POST['purchase_number']
                data['summ'] = request.POST['summ']
                data['contract_price'] = request.POST['contract_price']
                data['subj_contract'] = request.POST['subj_contract']
                data['text_contract'] = request.POST['text_contract']
                if 'prepaid_expense' in request.POST:
                    data['prepaid_expense'] = True
                else:
                    data['prepaid_expense'] = False
                if 'indisputable_write_off' in request.POST:
                    data['indisputable_write_off'] = True
                else:
                    data['indisputable_write_off'] = False
                data['date_start'] = request.POST['date_start']
                data['date_end'] = request.POST['date_end']
                data['owner_id_id'] = main_user.id

                obj = models.Applications(**data)
                obj.save()

                return redirect('personal:create_partners', id_app=obj.id)
        except Exception:
            context['error'] = 'К сожалению, вы не можете создать заявку.'

        return render(request, self.template_name, context)


class CreatePartView(LoginRequiredMixin, TemplateView):
    template_name = 'personal/create_partners.html'

    login_url = '/personal/login'
    redirect_field_name = '/personal/applications/'

    def dispatch(self, request, id_app, *args, **kwargs):
        context = {}
        if '/personal/create-application' not in str(self.request.META.get('HTTP_REFERER')):
            return redirect('personal:personal_application')

        banks = models.Banks.objects.all()
        banks_list = banks.values()
        context['banks'] = banks
        if request.POST:
            for i in range(len(banks_list)):
                print(banks_list[i])
                if banks_list[i]['name'] in request.POST:
                    data = {}
                    base_user = User.objects.get(email=str(self.request.user))

                    data['user_id'] = models.TypeUser.objects.get(user_id=base_user.id)
                    data['app_id'] = models.Applications.objects.get(id=id_app)
                    data['bank_id'] = models.Banks.objects.get(name=banks_list[i]['name'])

                    obj = models.ApplicationsBank(**data)
                    obj.save()
                    data.clear()

            return redirect('personal:personal_application')

        return render(request, self.template_name, context)


class AddCompanyView(LoginRequiredMixin, TemplateView):
    template_name = 'personal/add_face.html'

    login_url = '/personal/login'
    redirect_field_name = '/personal/add_face/'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        try:
            base_user = User.objects.get(email=str(self.request.user))
            main_user = models.TypeUser.objects.get(user_id=base_user.id)
            if request.method == 'POST':
                if 'inn' in request.POST:
                    # text data entity
                    context['org_inn'] = request.POST['inn']
                    context['org_form'] = request.POST['form-org']
                    context['org_name'] = request.POST['name']
                    context['org_kpp'] = request.POST['kpp']
                    context['org_ogrn'] = request.POST['ogrn']
                    context['org_r_account'] = request.POST['rs']
                    context['org_bank_bic'] = request.POST['bic']
                    context['org_bank_name'] = request.POST['bank']
                    context['org_bank_cor_acc'] = request.POST['kr']
                    context['org_gen'] = request.POST['gen']
                    context['org_buh'] = request.POST['buh']
                    context['owner_id'] = main_user

                    # file data entity not required
                    context['charter'] = request.FILES['charter']
                    context['charter'] = request.FILES['egru']
                    context['charter'] = request.FILES['certificate']
                    context['charter'] = request.FILES['gen-doc']
                    context['charter'] = request.FILES['buh-doc']
                    context['charter'] = request.FILES['bal19']
                    context['charter'] = request.FILES['bal20']

                    obj = models.ClientsEntity(**context)
                    obj.save()
                if 'second__name' in request.POST:
                    context['second_name'] = request.POST['second__name']
                    context['name'] = request.POST['fist__name']
                    context['last_name'] = request.POST['last__name']
                    context['city'] = request.POST['city']
                    context['phone'] = request.POST['number']
                    context['email'] = request.POST['email']
                    context['owner_id'] = main_user

                    obj = models.ClientsIndividual(**context)
                    obj.save()

                return redirect("personal:personal_application")

        except Exception as e:
            context['error'] = 'К сожалению, вы не можете добавить компанию.'
            print(e)

        return render(request, self.template_name, context)


class PersonalConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'personal/personal_config.html'

    login_url = '/personal/login'
    redirect_field_name = '/personal/add_face/'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        base_user = User.objects.get(email=str(self.request.user))
        main_user = models.TypeUser.objects.get(user_id=base_user.id)
        context['base_user'] = base_user
        context['main_user'] = main_user

        if request.method == 'POST':
            if 'username' in request.POST:
                base_user.username = request.POST['username']

            if 'first_name' in request.POST:
                base_user.first_name = request.POST['first_name']

            if 'last_name' in request.POST:
                base_user.last_name = request.POST['last_name']

            if 'email' in request.POST:
                base_user.email = request.POST['email']

            if 'choice' in request.POST:
                main_user.type_user = request.POST['choice']

            base_user.save()
            main_user.save()
            return redirect('personal:config')

        return render(request, self.template_name, context)


class CompanyDetail(TemplateView):

    template_name = 'personal/company_detail.html'

    def dispatch(self, request, slug, *args, **kwargs):
        obj = models.ClientsEntity.objects.get(slug=slug)
        if request.method == 'POST':
            # text post
            if 'inn' in request.POST:
                obj.org_gen = request.POST['inn']
            if 'form-org' in request.POST:
                obj.org_gen = request.POST['form-org']
            if 'name' in request.POST:
                obj.org_gen = request.POST['name']
            if 'kpp' in request.POST:
                obj.org_gen = request.POST['kpp']
            if 'ogrn' in request.POST:
                obj.org_gen = request.POST['ogrn']
            if 'rs' in request.POST:
                obj.org_gen = request.POST['rs']
            if 'bic' in request.POST:
                obj.org_gen = request.POST['bic']
            if 'bank' in request.POST:
                obj.org_gen = request.POST['bank']
            if 'kr' in request.POST:
                obj.org_gen = request.POST['kr']
            if 'gen' in request.POST:
                obj.org_gen = request.POST['gen']
            if 'buh' in request.POST:
                obj.org_gen = request.POST['buh']

            # docu post
            if 'charter' in request.FILES:
                obj.charter = request.FILES['charter']
            if 'egru' in request.FILES:
                obj.charter = request.FILES['egru']
            if 'certificate' in request.FILES:
                obj.charter = request.FILES['certificate']
            if 'gen-doc' in request.FILES:
                obj.charter = request.FILES['gen-doc']
            if 'buh-doc' in request.FILES:
                obj.charter = request.FILES['buh-doc']
            if 'bal19' in request.FILES:
                obj.charter = request.FILES['bal19']
            if 'bal20' in request.FILES:
                obj.charter = request.FILES['bal20']

            obj.save()

            return redirect('personal:personal_company')
        return render(request, self.template_name, context={'company': obj})


# class PasswordReset(TemplateView):
#     """
#     Class based view сброса пароля
#     """
#
#     template_name = 'signin/reset/password_reset.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         """
#         Функция сброса пароля
#         ЛогикаЖ
#             1. принимаем и валидируем форму\
#             2. находим пользователя по email из формы
#             3. генерируем письмо со сслыкой для сброса пароля
#             4. отправляем письмо
#         :param request:
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         if request.method == "POST":
#             password_reset_form = PasswordResetForm(request.POST)
#             if password_reset_form.is_valid():
#                 data = password_reset_form.cleaned_data['email']
#                 associated_users = User.objects.filter(Q(email=data))
#                 if associated_users.exists():
#                     for user in associated_users:
#                         subject = "Password Reset Requested"
#                         email_template_name = "signin/reset/password_reset_subject.txt"
#                         c = {
#                             "email": user.email,
#                             'domain': '127.0.0.1:8000',
#                             'site_name': 'Website',
#                             "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                             "user": user,
#                             'token': default_token_generator.make_token(user),
#                             'protocol': 'http',
#                         }
#                         email = render_to_string(email_template_name, c)
#                         try:
#                             send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
#                         except BadHeaderError:
#                             return HttpResponse('Invalid header found.')
#                         return redirect("/password_reset/done/")
#         password_reset_form = PasswordResetForm()
#         return render(request=request, template_name=self.template_name,
#                       context={"password_reset_form": password_reset_form})