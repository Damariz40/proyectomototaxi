from django import forms;
from django.forms import ModelForm, ModelChoiceField, widgets
from cliente.models import Cliente

class ClienteForm(ModelForm):

    class Meta:
        model= Cliente
        fields= "__all__"
        exclude=["estado", "user"]
        widgets={
            'fecha_nacimiento':widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'password1':widgets.PasswordInput(attrs={'type':'password'}),
            'password2':widgets.PasswordInput(attrs={'type':'password'})
        }
        