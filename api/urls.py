from django.urls import path
from .views import get_hc

urlpatterns = [
    path("", get_hc, name="hc"),
]
