from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.Inicio,name='Index'),
    url(r'^Mascotas$',views.ListaMascotas,name='Mascotas'),
    url(r'^quienessomos$',views.quienes,name='quienes'),
    url(r'^Contacto$',views.contacto,name='contacto'),
    url(r'^Login$',views.ingresar,name='ingresar'),
    url(r'^registro$',views.registro,name='registro'),
    url(r'^Recuperar$',views.recuperar,name='recuperar'),
    url(r'^CambioPassword$',views.cambio,name='cambio'),
    url(r'^GestionMascota$',views.gestion_mascota,name='gestion'),
    url(r'^Salir$',views.salir,name='salir'),
    url(r'^RegistroMascota$',views.registrar_mascota,name='reg_masc'),
    url(r'^EliminarMascota$',views.eliminar_mascota,name='eliminar'),
    url(r'^EditarMascotaSegundo$',views.editar_mascota2,name='editar2'),
    url(r'^EditarMascota$',views.editar_mascota,name='editar'),
]
