from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django import forms
import os


# Create your models here.
class TipoServicio(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    
    class Meta:
        db_table = 'Tipo_Servicio'
        verbose_name = "Tipo de servicio"
        verbose_name_plural = "Tipos de servicios"
        ordering = ['id']
    
    def __str__(self):
        return f'{self.id} - {self.nombre}'
    
    def acciones():
        return {
            'accion_eliminar': 'eliminar el Tipo de Servicio',
            'accion_actualizar': 'actualizar el Tipo de Servicio'
        }
    
class Servicio(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, verbose_name='Tipo de Servicio') 
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    imagen = models.ImageField(upload_to="servicios", verbose_name='Imagen')
    precio = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Precio')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    class Meta:
        db_table = 'Servicio'
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['id']
        
    def __str__(self):
        return self.nombre
    
    def acciones():
        return {
            'accion_eliminar': 'eliminar el Servicio',
            'accion_actualizar': 'actualizar el Servicio'
        }
        

class Promocion(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True, verbose_name='Codigo')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion', null=True)
    porcentaje_descuento = models.IntegerField(verbose_name='Porcentaje a Descontar')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(verbose_name='Fecha de termino')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    
    class Meta:
        db_table = 'Promocion'
        verbose_name = "Promocion"
        verbose_name_plural = "Promociones"
        ordering = ['fecha_fin']

    def __str__(self):
        return self.codigo
    
    def acciones():
        return {
            'accion_eliminar': 'eliminar la promocion',
            'accion_actualizar': 'actualizar la promocion'
        }



