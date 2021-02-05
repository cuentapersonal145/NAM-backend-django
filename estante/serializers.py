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

class PrincipalesDatosTipo(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'nombre')

class PrincipalesDatosProducto(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'imagen', 'color')

class DatosProductoSerializador(serializers.ModelSerializer):
    producto = PrincipalesDatosProducto(read_only=True)
    tipo = PrincipalesDatosTipo(read_only=True)
    class Meta:
        model = ProductoTipo
        fields = '__all__'