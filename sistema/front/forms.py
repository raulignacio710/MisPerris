from django import forms
from api.models import Usuario,Mascota

# los valores de los dos choicefield
tiposUsuarios=(
    ('Administrador','Admin'),
    ('Adoptante','Adopt')
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
