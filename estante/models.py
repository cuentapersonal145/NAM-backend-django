# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from colorfield.fields import ColorField

class Tipo(models.Model):
    """
    Clase usada para registrar los productos usados en el negocio
    - - - - -
    Attributes
    - - - - -
    nombre : str(16)
        Nombre para identificar el tipo de producto que se maneja en el negocio
    date_record : datetime
        Fecha de registro
    date_update : datetime
        Fecha de último cambio realizado
    is_active : boolean
        Indica si el registro esta activo
    - - - - -
    Methods
    - - - - -
    """
    TYPE_CHOICES = (
        (1, ("Indefinido")),
        (2, ("Bulto")),
        (3, ("Kilo")),
        (4, ("Libra")),
        (5, ("Paquete")),
        (6, ("Unidad")),
        (7, ("Media-Libra")),
    )
    nombre = models.CharField(max_length=16, blank=True)

    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Tipo")
        verbose_name_plural = ("Tipos")

    def __str__(self):
        return str(self.id) + ' : ' + self.nombre

class Producto(models.Model):
    """
    Clase usada para registrar los productos usados en el negocio
    - - - - -
    Attributes
    - - - - -
    tipo : MM
        Representa la relacion muchos a muchos con el tipo del producto
    nombre : str(256)
        Nombre para identificar el producto
    tipo : +int
        Tipo correspondiente al producto definido para el negocio
    imagen : file
        Campo donde se almacena una imagen que represente al producto
    color : Color
        Campo que almacena el valor hex correspondiente a un color que represente al producto
    date_record : datetime
        Fecha de registro
    date_update : datetime
        Fecha de último cambio realizado
    is_active : boolean
        Indica si el registro esta activo
    - - - - -
    Methods
    - - - - -
    """
    COLOR_CHOICES = (
        ("#FFFFFF", "Blanco"),
        ("#C0C0C0", "Plateado"),
        ("#808080", "Gris"),
        ("#000000", "Negro"),
        ("#FF0000", "Rojo"),
        ("#800000", "Marron"),
        ("#FFFF00", "Amarillo"),
        ("#808000", "Oliva"),
        ("#00FF00", "Limon"),
        ("#008000", "Verde"),
        ("#00FFFF", "Aqua"),
        ("#008080", "Verde-Azul"),
        ("#0000FF", "Azul"),
        ("#000080", "Azul-Marino"),
        ("#FF00FF", "Fuchsia"),
        ("#800080", "Morado")
    )

    tipo = models.ManyToManyField(Tipo, through='ProductoTipo')

    # nombre = models.CharField(max_length=256, blank=True, default="Alimento para mascotas")
    nombre = models.CharField(max_length=256, blank=True)
    imagen = models.FileField(upload_to="img", blank=True, default="/img/img-default.png")
    color = ColorField(default='#FFFFFF', choices=COLOR_CHOICES)

    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

    def __str__(self):
        return str(self.id) + ' : ' + self.nombre    

class ProductoTipo(models.Model):
    """
    Clase usada para registrar los productos usados en el negocio
    - - - - -
    Attributes
    - - - - -
    producto : FK
        Llave foranea en la relacion con el producto
    tipo : FK
        Llave foranea en la relacion con el tipo
    precio : +int
        Valor del producto segun el tipo
    peso : str(16)
        Peso del producto segun el tipo
    date_record : datetime
        Fecha de registro
    date_update : datetime
        Fecha de último cambio realizado
    is_active : boolean
        Indica si el registro esta activo
    - - - - -
    Methods
    - - - - -
    """
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    # precio = models.PositiveIntegerField(blank=True, default=0)
    precio = models.PositiveIntegerField(blank=True)
    peso = models.CharField(max_length=16, blank=True, default="0kg")

    class Meta:
        verbose_name = ("ProductoTipo")
        verbose_name_plural = ("ProductosTipos")

    def __str__(self):
        return str(self.id) + " : " + self.producto.nombre + " (" + self.tipo.nombre + ") = $" + str(self.precio) 

