from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def how_to_work(request):
    return render(request, 'main/index_how.html')


def services(request):
    return render(request, 'main/index_services.html')

