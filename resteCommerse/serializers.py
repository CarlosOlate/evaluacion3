from rest_framework import serializers
from eCommerse.models import Proveedor, Giro

class GiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Giro
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'