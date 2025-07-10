from django.urls import path

from recipes.views import about, contact, home

#dominio.com/recipes/
urlpatterns = [
    path("", home), #HomePage
    path("sobre/", about), #Sobre
    path('contato/', contact), #Contato
]
