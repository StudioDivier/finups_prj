from django.shortcuts import redirect, render
from django.db.utils import IntegrityError
from django.urls import reverse
from django.views.generic import TemplateView
from . import models

from datetime import datetime


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'

    def dispatch(self, request, *args, **kwargs):
        post_request = {}
        context = {}
        menu_serv = models.ClassService.objects.all()[::-1]
        context['menu'] = menu_serv
        if request.method == 'POST':
            try:
                post_request['name'] = request.POST['name']
                post_request['phone'] = request.POST['tel']
                post_request['form_type'] = request.POST['form_type']
                post_request['date_request'] = datetime.now()
                try:
                    post_request['email'] = request.POST['email']
                except Exception as e:
                    print(e)

                print(post_request)
                obj = models.CallbackRequests(**post_request)
                obj.save()
                context['thx'] = 'Спасибо! Мы свяжемся с Вами в ближайшее время.'
            except IntegrityError:
                context['error'] = 'Введеные данные уже находятся в нашей базе!'

        return render(request, self.template_name, context)


class WorkView(TemplateView):
    template_name = 'main/index_how.html'

    def dispatch(self, request, *args, **kwargs):
        post_request = {}
        context = {}
        menu_serv = models.ClassService.objects.all()[::-1]
        context['menu'] = menu_serv
        if request.method == 'POST':
            try:
                post_request['name'] = request.POST['name']
                post_request['phone'] = request.POST['tel']
                post_request['form_type'] = request.POST['form_type']
                post_request['date_request'] = datetime.now()
                try:
                    post_request['email'] = request.POST['email']
                except Exception as e:
                    print(e)

                print(post_request)
                obj = models.CallbackRequests(**post_request)
                obj.save()
                context['thx'] = 'Спасибо! Мы свяжемся с Вами в ближайшее время.'
            except IntegrityError:
                context['error'] = 'Введеные данные уже находятся в нашей базе!'

        return render(request, self.template_name, context)


class ServicesView(TemplateView):
    template_name = 'main/index_services.html'

    def dispatch(self, request, *args, **kwargs):
        post_request = {}
        context = {}
        menu_serv = models.ClassService.objects.all()[::-1]
        context['menu'] = menu_serv
        if request.method == 'POST':
            try:
                post_request['name'] = request.POST['name']
                post_request['phone'] = request.POST['tel']
                post_request['form_type'] = request.POST['form_type']
                post_request['date_request'] = datetime.now()
                try:
                    post_request['email'] = request.POST['email']
                except Exception as e:
                    print(e)

                print(post_request)
                obj = models.CallbackRequests(**post_request)
                obj.save()
                context['thx'] = 'Спасибо! Мы свяжемся с Вами в ближайшее время.'
            except IntegrityError:
                context['error'] = 'Введеные данные уже находятся в нашей базе!'

        return render(request, self.template_name, context)


class PrivacyView(TemplateView):
    template_name = 'main/privacy.html'

    def dispatch(self, request, *args, **kwargs):
        post_request = {}
        context = {}
        menu_serv = models.ClassService.objects.all()[::-1]
        context['menu'] = menu_serv
        if request.method == 'POST':
            try:
                post_request['name'] = request.POST['name']
                post_request['phone'] = request.POST['tel']
                post_request['form_type'] = request.POST['form_type']
                post_request['date_request'] = datetime.now()
                try:
                    post_request['email'] = request.POST['email']
                except Exception as e:
                    print(e)

                print(post_request)
                obj = models.CallbackRequests(**post_request)
                obj.save()
                context['thx'] = 'Спасибо! Мы свяжемся с Вами в ближайшее время.'
            except IntegrityError:
                context['error'] = 'Введеные данные уже находятся в нашей базе!'

        return render(request, self.template_name, context)
