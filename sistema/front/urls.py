from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.Inicio,name='Index'),
    url(r'^Index$',views.ListaMascotas,name='Mascotas'),
]
