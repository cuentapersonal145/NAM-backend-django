# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import *
from .serializers import *

from django.db.models.signals import post_save
from .signal import *

post_save.connect(save_or_send_prod_tipo_1, sender=ProductoTipo)
post_save.connect(save_or_send_prod_tipo_2, sender=ProductoTipo)

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializador

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializador

class ProductoTipoViewSet(viewsets.ModelViewSet):
    queryset = ProductoTipo.objects.all()
    serializer_class = ProductoTipoSerializador

class DatosProductoAPI(generics.RetrieveAPIView):
    queryset = ProductoTipo.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = ProductoTipo.objects.filter(producto_id=kwargs['id_producto'])
        serializer = DatosProductoSerializador(queryset, many=True)
        return Response(serializer.data)
