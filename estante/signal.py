from django.db.models.signals import post_save
from .models import *

def save_or_send_prod_tipo_1(sender, instance, created, **kwargs):
    if instance.tipo.id == 4:
        newTipo = Tipo.objects.filter(id=3)
        newProductoTipo = ProductoTipo(producto=instance.producto, tipo=newTipo[0], precio=instance.precio*2)
        newProductoTipo.save()

def save_or_send_prod_tipo_2(sender, instance, created, **kwargs):
    if instance.tipo.id == 7:
        newTipo = Tipo.objects.filter(id=4)
        newProductoTipo = ProductoTipo(producto=instance.producto, tipo=newTipo[0], precio=instance.precio*2)
        newProductoTipo.save()