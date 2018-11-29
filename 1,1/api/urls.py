from django.conf.urls import url
from .views import MascotaView

from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^Mascotas$',views.MascotaView.as_view()),
]
