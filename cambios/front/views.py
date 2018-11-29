from django.shortcuts import render,redirect
from django.http import HttpResponse
from api.models import Usuario,Mascota
from django.template import loader
from .forms import AgregarUsuario,Login,Recuperar,CambiarPass
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
from django.contrib import messages

# Create your views here.
def Inicio(request):
    return render(request,"index.html")

def ListaMascotas(request):
    return render(request,"mascotas.html")

def quienes(request):
    return render(request,'quienes.html',{})

def contacto(request):
    return render(request,'contacto.html',{})

def gestion_mascota(request):
    return render(request,'gestion_masc.html',{})

#USUARIO

# el registro de usuario con es como el visto en clases
def registro(request):
    template=loader.get_template("registro.html")
    form=AgregarUsuario(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        if(data.get("perfil")=="Administrador"):
            perf=1
        else:
            perf=0

        user=User.objects.create_user(username=data.get("username"),password=data.get("password"),email=data.get("email"),first_name=data.get("first_name"),last_name=data.get("last_name"),is_staff=perf)
        u=Usuario(user=user,perfil=data.get("perfil"),rutCliente=data.get("rutCliente"))
        user.save()
        u.save()
        return redirect('Index')
    form=AgregarUsuario()
    return render(request,'registro.html',{'form':form,})

#el login utilizando los metodos del modelo user

def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
                login(request,user)
                return redirect('Index')
    return render(request,"login.html",{'form':form,})

#vista de envio de mailpara recuperar contraseña

def recuperar(request):
    form=Recuperar(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        send_mail(
            'no_reply',
            'Recuperacion de contraseña ingrese en el siguiente link: http://localhost:8000/CambioPassword',
            'pruebas.soft710@gmail.com',
            [data.get("email")],
            fail_silently=False,
        )

        messages.info(request,'Mensaje enviado exitosamente')
    return render(request,'Olvido_pass.html',{'form':form,})

# el cambio de contraseña con el metodo set password del modelo user
def cambio(request):
    form=CambiarPass(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        if data.get("newpass")==data.get("newpass2"):
            usuario=User.objects.get(username=data.get("username"))
            usuario.set_password(data.get("newpass"))
            usuario.save()
            return redirect('ingresar')
        else:
            return redirect('cambio')
    return render(request,'Cambio.html',{'form':form,})

    #vista para logout
def salir(request):
    logout(request)
    return redirect("/")
