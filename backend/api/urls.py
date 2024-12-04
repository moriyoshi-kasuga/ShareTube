from django.urls import path
from .views import get_hc, get_recipes, get_textures

urlpatterns = [
    path("", get_hc, name="hc"),
    path("recipes/", get_recipes, name="recipes"),
    path("textures/", get_textures, name="textures"),
]
