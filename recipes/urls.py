from django.urls import path

from . import views

app_name = 'recipes'

#dominio.com/recipes/
urlpatterns = [
    path("", views.home, name="home"), #HomePage
    path('recipes/category/<int:category_id>/',views.category, name="category"),
    path("recipes/<int:id>/", views.recipe, name="recipe"),
]
