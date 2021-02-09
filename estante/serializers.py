from rest_framework import serializers

from .models import *

#--------------------------------------- Serializadores por defecto ----------------------------------------#

class TipoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class CategoriaSerializador(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaSerializador(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ProductoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

#-------------------------------------------------------------------------------#

class PrincipalesDatosTipo(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'nombre')

class PrincipalesDatosCategoria(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')

class PrincipalesDatosMarca(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nombre', 'imagen', 'color')

class DatosProductoSerializador(serializers.ModelSerializer):
    marca = PrincipalesDatosMarca(read_only=True)
    tipo = PrincipalesDatosTipo(read_only=True)
    categoria = PrincipalesDatosCategoria(read_only=True)
    class Meta:
        model = Producto
        fields = '__all__'