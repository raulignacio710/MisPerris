from rest_framework import serializers
from .models import Usuario,Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            '__all__'
        )
        model=Mascota