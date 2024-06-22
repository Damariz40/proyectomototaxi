from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.documento}.{ext}"
    return f"conductor/conductores/{filename}"

class Conductor(models.Model):
    primer_nombre= models.CharField(max_length=45,verbose_name="Primer Nombre")
    segundo_nombre= models.CharField(max_length=45,verbose_name="Segundo Nombre", blank=True,null=True)

    primer_apellido= models.CharField(max_length=45,verbose_name="Primer Apellido")
    segundo_apellido= models.CharField(max_length=45,verbose_name="Segundo Apellido", blank=True, null=True)
    
    fecha_nacimiento= models.DateField(verbose_name="Fecha de Nacimiento")
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True, default="comunidad\default-user.jpeg")
    correo = models.EmailField(max_length=50, verbose_name="Correo Electrónico")
    
    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento=models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento= models.PositiveIntegerField(verbose_name="Documento", unique=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, default="")
    moto_nombre = models.CharField(max_length=50, verbose_name="Moto", default="")
    modelo = models.PositiveIntegerField(verbose_name="Modelo", default=0000)
    placa = models.CharField(verbose_name="Placa", max_length=6, unique=True, default="")
    estado=models.BooleanField(default=True)    
    password1 = models.CharField(verbose_name="Contraseña", max_length=  128, default="", )
    password2 = models.CharField(verbose_name="Confirme la Contraseña", max_length=  128, default="", )
    
    def clean(self):
        self.primer_nombre= self.primer_nombre.title()
    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"
    class Meta:
        verbose_name_plural="Conductores"
    @property
    def full_name(self):
        if self.segundo_nombre:
            return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"
        else:
            return f"{self.primer_nombre} {self.primer_apellido} {self.segundo_apellido}"
        
    def usuario_activo(self):
        if self.estado:
            return Conductor.objects.filter(usuario=self, estado=True)
        else:
            return Conductor.objects.none()
    
    