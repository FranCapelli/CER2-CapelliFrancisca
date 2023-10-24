from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import django_filters

# Create your models here.

class comunicado(models.Model):
    TIPO_CHOICES = [
        ('S', "Suspension de actividades"),
        ('C', "Suspension de clases"),
        ('I', "Informacion")
    ]

    id= models.BigAutoField(primary_key=True)
    titulo= models.CharField(max_length=300)
    detalle= models.CharField(max_length=600)
    detalle_corto= models.CharField(max_length=300)
    tipo= models.CharField(max_length=5, choices=TIPO_CHOICES, default='.')
    entidad= models.ForeignKey('entidad', on_delete=models.CASCADE)
    visible= models.BooleanField(default=True)
    fecha_publicacion= models.DateTimeField(default=timezone.now)
    fecha_ultima_modificacion= models.DateTimeField(default=timezone.now)
    publicado_por= models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor',null=True)
    
    def __str__(self):
        return self.titulo
    class Meta:
        db_table="Comunicado"
    
    
class entidad(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=500)
    logo=models.ImageField(upload_to="app/fotos")
    
    def __str__(self):
        return self.nombre
    class Meta:
        db_table="Entidad"
        

    
    
