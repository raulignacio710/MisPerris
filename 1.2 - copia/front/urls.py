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
]
