from rest_framework import serializers

from .models import *

class TipoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class ProductoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoTipoSerializador(serializers.ModelSerializer):
    class Meta:
        model = ProductoTipo
        fields = '__all__'