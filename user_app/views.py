from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView
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

    def post(self, request, *args, **kwargs):
        print(self.request.user)
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

    def get(self, request, *args, **kwargs):
        print(self.request.user)
        return render(request, self.template_name)


class PersonalCompanyView(LoginRequiredMixin, TemplateView):

    template_name = 'personal/personal_company.html'

    login_url = '/personal/login'
    redirect_field_name = '/personal/company/'

    def get(self, request, *args, **kwargs):
        base_user = User.objects.get(email=str(self.request.user))
        main_user = models.TypeUser.objects.get(user_id=base_user.id)
        entity = models.ClientsEntity.objects.all().filter(owner_id=main_user.id)

        return render(request, self.template_name, {'entity_list': entity})


class CreateAppView(LoginRequiredMixin, TemplateView):

    template_name = 'personal/create_application.html'

    login_url = '/personal/login'
    redirect_field_name = '/personal/create_application/'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        # load services
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

        return render(request, self.template_name, context)


class CreatePartView(LoginRequiredMixin, TemplateView):

    template_name = 'personal/create_partners.html'

    login_url = '/personal/login'
    redirect_field_name = '/personal/create_partners/'

    def dispatch(self, request, id_app, *args, **kwargs):
        context = {}
        data = {}
        banks = models.Banks.objects.all()
        context['banks'] = banks
        print(id_app)
        if request.POST:
            data['banks'] = request.POST['bank_choice']



            return redirect('personal:personal_application')

        return render(request, self.template_name, context)


class AddCompanyView(LoginRequiredMixin, TemplateView):

    template_name = 'personal/add_face.html'

    login_url = '/personal/login'
    redirect_field_name = '/personal/add_face/'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            base_user = User.objects.get(email=str(self.request.user))
            main_user = models.TypeUser.objects.get(user_id=base_user.id)
            if 'inn' in request.POST:
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
                context['date_request'] = datetime.now()
                context['owner_id'] = main_user.id

                obj = models.ClientsEntity(**context)
                obj.save()
            if 'second__name' in request.POST:
                context['second_name'] = request.POST['second__name']
                context['name'] = request.POST['fist__name']
                context['last_name'] = request.POST['last__name']
                context['city'] = request.POST['city']
                context['phone'] = request.POST['number']
                context['email'] = request.POST['email']
                context['date_request'] = datetime.now()
                context['owner_id'] = main_user.id

                obj = models.ClientsIndividual(**context)
                obj.save()

            return redirect("personal:personal_application")

        return self.render_to_response({})