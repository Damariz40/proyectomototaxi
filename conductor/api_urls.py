from django.urls import path
from . import api_views

urlpatterns = [
    path("conductores/", api_views.agregar_conductor, name="api_agregar_conductor")
]
