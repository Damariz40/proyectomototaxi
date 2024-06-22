from django.urls import path
from . import api_views

urlpatterns = [
    path("clientes/", api_views.agregar_cliente, name="api_agregar_cliente")
]
