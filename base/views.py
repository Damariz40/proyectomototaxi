from django.shortcuts import render # type: ignore

def index_admin(request):
    titulo="Inicio Administrador"
    context={
        "titulo":titulo,
    }
    return render(request,"index-admin.html",context)

def index_cliente(request):
    titulo="¡Bienvenido a Mototaxi H.!"
    context={
        "titulo":titulo,
    }
    return render(request,"index-cliente.html",context)