from django.urls import path

from . import views

#dominio.com/recipes/
urlpatterns = [
    path("", views.home), #HomePage
    path("recipes/<int:id>/", views.recipe),
]
