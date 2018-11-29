from django.shortcuts import render,redirect
from django.http import HttpResponse
from api.models import Usuario,Mascota
from django.template import loader
from .forms import AgregarUsuario,Login,Recuperar,CambiarPass,RegistrarMascota,EliminarMascota,EditarMascota,EditarMascota2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
from django.contrib import messages
import json

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

def maqueta_layout(request):
	template='front/maqueta.html'
	return render(request,template)
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

#MASCOTA

# registro de mascota con el login requerido y ser administrador, ademas el id de la mascota siempre llenara el id que falte paramantener el orden
@login_required(login_url='ingresar')
def registrar_mascota(request):
    form=RegistrarMascota(request.POST,request.FILES or None)
    if form.is_valid():
        data=form.cleaned_data
        masc=Mascota(fotoMascota=request.FILES['fotoMascota'],nombreMascota=data.get("nombreMascota"),raza=data.get("raza"),descripcion=data.get("descripcion"),estado=data.get("estado"))
        a=False
        b=1
        while a!=True:
                if Mascota.objects.filter(codigoMascota=b).count()<=0:
                    masc.codigoMascota=b
                    masc.save()
                    a=True
                b=b+1
        return redirect('gestion')
    form=RegistrarMascota()
    return render(request,'reg_mascota.html',{'form':form,})

# eliminacion de mascotas con delete con formulario model choice y paginator
def eliminar_mascota(request):
    form=EliminarMascota(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        masc=data.get("mascotas")
        masc.delete()
        return redirect('gestion')
    lista=Mascota.objects.all().order_by('codigoMascota')

    paginator= Paginator(lista,60)
    try:
        pag=int(request.GET.get("page"),1)
    except ValueError:
        pag=1

    try:
        lista=paginator.page(pag)
    except (InvalidPage,EmptyPage):
        lista=paginator.page(paginator.num_pages)
    form=EliminarMascota()
    return render(request,'eliminar_masc.html',{'form':form,'lista':lista,})

# edicion de mascotas con formulario model choice y paginator

def editar_mascota(request):
    form=EditarMascota(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        masco=data.get("mascotas")
        global pk
        pk=masco.codigoMascota
        return redirect('editar2')
    lista=Mascota.objects.all().order_by('codigoMascota')
    paginator= Paginator(lista,60)
    try:
        pag=int(request.GET.get("page"),1)
    except ValueError:
        pag=1

    try:
        lista=paginator.page(pag)
    except (InvalidPage,EmptyPage):
        lista=paginator.page(paginator.num_pages)

    form=EditarMascota()
    return render(request,'editar_masc.html',{'form':form,'lista':lista,})
#segunda ventana de edicion con el formulario

def editar_mascota2(request):
    form=EditarMascota2(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            data=form.cleaned_data
            masc=Mascota.objects.get(codigoMascota=pk)
            masc.nombreMascota=data.get("nombreMascota")
            masc.raza=data.get("raza")
            masc.descripcion=data.get("descripcion")
            masc.estado=data.get("estado")
            masc.save()
            return redirect("gestion")
    else:
        masc=Mascota.objects.get(codigoMascota=pk)
        data2={"nombreMascota":masc.nombreMascota,"raza":masc.raza,"descripcion":masc.descripcion,"estado":masc.estado,}
        form=EditarMascota2(data2)
    #form=EditarMascota2()
    return render(request,'editar_masc2.html',{'form':form,'data2':data2,})
#la lista de mascotas con paginator y foto
