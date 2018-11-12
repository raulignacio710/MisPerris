from django.db import models
from django.contrib.auth.models import User

# modelo mascota con image field para la foto
class Mascota(models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    fotoMascota=models.ImageField(upload_to='media',null=True,blank=True)
    nombreMascota=models.CharField(max_length=20)
    raza=models.CharField(max_length=20)
    descripcion=models.TextField(max_length=65,default="Sin Descripcion")
    estado=models.CharField(max_length=20)
    def __str__(self):
        return(str(self.codigoMascota)+" "+self.nombreMascota)
    
#usuario que hereda de user para mantener sus metodos y atributos
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    perfil=models.CharField(max_length=20,default="Invitado")
    rutCliente=models.CharField(max_length=20)
