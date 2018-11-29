from django import forms
from api.models import Usuario,Mascota

# los valores de los dos choicefield
tiposUsuarios=(
    ('Administrador','Admin'),
    ('Adoptante','Adopt')
)
estadoMascota=(
    ('Rescatado','Rescatado'),
    ('Disponible','Disponible'),
    ('Adoptado','Adoptado')
)
#formularios de user
class AgregarUsuario(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput(),label="Ingrese su Nombre")
    last_name=forms.CharField(widget=forms.TextInput(),label="Ingrese su Apellido")
    rutCliente=forms.CharField(widget=forms.TextInput(),label="Ingreso de Rut")
    username=forms.CharField(widget=forms.TextInput(),label="Ingreso Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Ingreso de Contraseña")
    email=forms.EmailField(widget=forms.EmailInput(),label="Email")
    perfil=forms.ChoiceField(choices=tiposUsuarios)


class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Ingreso Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Ingreso de Contraseña")

class Recuperar(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(),label="Email")

class CambiarPass(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Ingreso Nombre Usuario")
    newpass=forms.CharField(widget=forms.PasswordInput(),label="Ingrese Nueva Contraseña")
    newpass2=forms.CharField(widget=forms.PasswordInput(),label="Ingrese Nuevamente su Contraseña")
#formularios de mantenedor de mascota
class RegistrarMascota(forms.Form):
    fotoMascota=forms.ImageField(label="Ingrese Foto para la Mascota")
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Ingrese el Nombre de la Mascota")
    raza=forms.CharField(widget=forms.TextInput(),label="Ingrese la raza de la Mascota")
    descripcion=forms.CharField(widget=forms.TextInput(),label="Descripcion")
    estado=forms.ChoiceField(choices=estadoMascota)

class EliminarMascota(forms.Form):
    mascotas=forms.ModelChoiceField(queryset=Mascota.objects.all(),label="Seleccione el Id de la mascota que desea Eliminar")

class EditarMascota(forms.Form):
    mascotas=forms.ModelChoiceField(queryset=Mascota.objects.all(),label="Seleccione el Id de la mascota que desea Editar")

class EditarMascota2(forms.Form):
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Ingrese el Nombre de la Mascota")
    raza=forms.CharField(widget=forms.TextInput(),label="Ingrese la raza de la Mascota")
    descripcion=forms.CharField(widget=forms.TextInput(),label="Descripcion")
    estado=forms.ChoiceField(choices=estadoMascota)
