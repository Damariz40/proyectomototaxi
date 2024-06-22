from django.shortcuts import render
from cliente.forms import  ClienteForm
from cliente.models import Cliente
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from PIL import Image

# Create your views here.

def agregar_cliente(request):
    titulo = 'Registrarse como cliente'
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=request.POST.get('documento')).exists():
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                if password1 == password2:                    
                    user = User.objects.create_user('nombre','email@mail','password')
                    user.username= request.POST.get('documento')
                    user.first_name= request.POST.get('primer_nombre')
                    user.last_name= request.POST.get('primer_apellido')
                    user.email= request.POST.get('correo')
                    user.password= make_password(password1)
                    user.save()
                    login(request, user) 
                    
                else:
                    messages.error(request, f'¡Las contraseñas no coinciden!')                      
                
                
                user= User.objects.get(username=request.POST.get('documento'))
                
                cliente = Cliente.objects.create(
                primer_nombre=request.POST.get('primer_nombre'),
                segundo_nombre=request.POST.get('segundo_nombre'),
                primer_apellido=request.POST.get('primer_apellido'),
                segundo_apellido=request.POST.get('segundo_apellido'),
                fecha_nacimiento=request.POST.get('fecha_nacimiento'),
                imagen=request.FILES.get('imagen'),
                correo=request.POST.get('correo'),
                tipo_documento=request.POST.get('tipo_documento'),
                documento=request.POST.get('documento'),
                moto_nombre =request.POST.get('moto_nombre'),
                modelo = request.POST.get('modelo'),
                placa = request.POST.get('placa').upper(),
                user = user                 
                )             
                if cliente.imagen:
                    img= Image.open(cliente.imagen.path)
                    img= img.resize((500,500))
                    img.save(cliente.imagen.path)
            cliente.save()
            messages.success(request, f'¡El Usuario se agregó de forma exitosa!')    
        else:
            form= ClienteForm(request.POST,request.FILES)
            messages.error(request, f'¡Error al agregar cliente!')
    else:
        form= ClienteForm()        
    context={
        "titulo":titulo,
        "form":form,  
    }
    return render(request, 'cliente/registrar_cliente.html', context)    

    
# Create your views here.
