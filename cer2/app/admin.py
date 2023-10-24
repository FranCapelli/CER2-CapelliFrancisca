from django.contrib import admin
from .models import comunicado, entidad

# Register your models here.
class entidad_admin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class comunicado_admin(admin.ModelAdmin):
    list_display = ("id", "titulo","entidad")

admin.site.register(comunicado,comunicado_admin)
admin.site.register(entidad,entidad_admin)
    
