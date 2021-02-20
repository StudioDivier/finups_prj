from django.shortcuts import render


def login(request):
    return render(request, 'signin/login-page.html')


def signin(request):
    return render(request, 'signin/signin-page.html')


def signin2(request):
    return render(request, 'signin/signin-page2.html')


def personal_application(request):
    return render(request, 'personal/personal_application.html')


def personal_company(request):
    return render(request, 'personal/personal_company.html')


def create_create_app(request):
    return render(request, 'personal/create_application.html')


def create_partners(request):
    return render(request, 'personal/create_partners.html')


def add_face(request):
    return render(request, 'personal/add_face.html')
