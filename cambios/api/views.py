from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mascota
from .serializers import MascotaSerializer

class MascotaView(APIView):
    def get(self,request):
        masc=Mascota.objects.all()
        serializer=MascotaSerializer(masc,many=True)
        return Response(serializer.data)