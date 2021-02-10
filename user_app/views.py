from django.shortcuts import render


def login(request):
    return render(request, 'signin/login-page.html')


def signin(request):
    return render(request, 'signin/signin-page.html')


def signin2(request):
    return render(request, 'signin/signin-page2.html')