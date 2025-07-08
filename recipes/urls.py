from django.urls import path

from recipes.views import my_about, my_contact, my_home

#dominio.com/recipes/
urlpatterns = [
    path("", my_home), #HomePage
    path("sobre/", my_about), #Sobre
    path('contato/', my_contact), #Contato
]
