from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('home_page')

def about(request):
    return HttpResponse('about_page')

def contact(request):
    return HttpResponse('contact (11)93233-6006')


# Create your views here.
