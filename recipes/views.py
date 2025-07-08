from django.http import HttpResponse
from django.shortcuts import render


def my_home(request):
    return render(request, 'home.html')

def my_about(request):
    return HttpResponse('HOME PAGE')

def my_contact(request):
    return HttpResponse('(11)93233-6006')


# Create your views here.
