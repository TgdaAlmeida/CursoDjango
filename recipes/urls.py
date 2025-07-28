from django.urls import path

from . import views

#dominio.com/recipes/
urlpatterns = [
    path("", views.home, name="recipes-home"), #HomePage
    path("recipes/<int:id>/", views.recipe, name="recipes-recipe"),
]
